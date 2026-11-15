from xml.etree.ElementTree import XMLParser

import frappe
from trebelge.EbelgeUsers import EbelgeUsers
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler


@frappe.whitelist()
def check_all_ebelge_parties():
    # Collect our own parties first: the GIB list holds every registered
    # user in Turkey, so get_ebelge_users() only keeps the tax ids we
    # actually have to check instead of one dict entry per user.
    parties_by_type = {}
    wanted_tax_ids = set()
    for party_type in ["Customer", "Supplier"]:
        parties = frappe.get_all(party_type, filters={"tax_id": ["not in", None], "disabled": 0},
                                 fields={"name", "tax_id", "is_efatura_user", "is_eirsaliye_user"})
        parties_by_type[party_type] = parties
        wanted_tax_ids.update(party["tax_id"] for party in parties)
    ebelge_users = get_ebelge_users(wanted_tax_ids)
    for party_type, parties in parties_by_type.items():
        for party in parties:
            if party["tax_id"] in ebelge_users:
                if ebelge_users[party["tax_id"]]["is_efatura_user"]:
                    if party["is_efatura_user"] != 1:
                        frappe.db.set_value(party_type, party.name,"is_efatura_user", 1)
                else:
                    if party["is_efatura_user"] == 1:
                        frappe.db.set_value(party_type, party.name,"is_efatura_user", 0)
                if ebelge_users[party["tax_id"]]["is_eirsaliye_user"]:
                    if party["is_eirsaliye_user"] != 1:
                        frappe.db.set_value(party_type, party.name,"is_eirsaliye_user", 1)
                else:
                    if party["is_eirsaliye_user"] == 1:
                        frappe.db.set_value(party_type, party.name,"is_eirsaliye_user", 0)
            else:
                if party["is_efatura_user"] == 1:
                    frappe.db.set_value(party_type, party.name,"is_efatura_user", 0)
                if party["is_eirsaliye_user"] == 1:
                    frappe.db.set_value(party_type, party.name,"is_eirsaliye_user", 0)
    return frappe.utils.now_datetime()


def get_ebelge_users(tax_ids=None):
    """Stream the GIB registered-users list without loading it into memory.

    The list (``private/files/KullaniciListesiXml/newUserPkList.xml``) holds
    every registered e-Fatura/e-Irsaliye user in Turkey, so it grows to
    hundreds of MB. The old code did ``frappe.read_file(...)`` -- the whole
    file as one bytes object -- and ``EbelgeUsers`` kept one dict entry per
    user, which together exhausted the worker's memory once the file grew.

    Now the file is fed to the parser in 1 MiB chunks (``XMLParser.feed``
    accepts arbitrary chunk boundaries, including mid-character), and only
    the tax ids in ``tax_ids`` are kept. Memory stays flat regardless of
    file size; only the result dict grows, and only with wanted users.

    :param tax_ids: optional iterable of tax ids to keep; None keeps all.
    """
    wanted = set(tax_ids) if tax_ids else None
    parser = XMLParser(target=EbelgeUsers(wanted=wanted))
    file_path = frappe.get_site_path("private", "files", "KullaniciListesiXml", "newUserPkList.xml")
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            parser.feed(chunk)
    return parser.close()


@frappe.whitelist()
def check_all_xml_files():
    hXMLFileHandler = InvoiceHandler()
    # for all *.xml files
    for xmlFile in frappe.get_all('File',
                                  filters={"file_name": ["like", "%.xml"], "is_folder": 0},
                                  fields={"file_url"}):
        file_url = xmlFile.get('file_url')
        # Strip leading slash to prevent absolute path resolution issues
        file_path = frappe.get_site_path(file_url.lstrip('/'))
        hXMLFileHandler.handle_xml_file(file_path)

    return frappe.utils.now_datetime()
