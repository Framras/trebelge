from xml.etree.ElementTree import XMLParser

import frappe
from trebelge.EbelgeUsers import EbelgeUsers
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler


@frappe.whitelist()
def check_all_ebelge_parties():
    ebelge_users = get_ebelge_users()
    store_ebelge_users(ebelge_users)
    for party_type in ["Customer", "Supplier"]:
        for party in frappe.get_all(party_type, filters={"tax_id": ["not in", None], "disabled": 0},
                                    fields={"name", "tax_id", "is_efatura_user", "is_eirsaliye_user"}):
            if party["tax_id"] in ebelge_users:
                if ebelge_users[party["tax_id"]]["is_efatura_user"]:
                    if party["is_efatura_user"] != 1:
                        doc = frappe.get_doc(party_type, party.name)
                        doc.db_set("is_efatura_user", 1)
                else:
                    if party["is_efatura_user"] == 1:
                        doc = frappe.get_doc(party_type, party.name)
                        doc.db_set("is_efatura_user", 0)
                if ebelge_users[party["tax_id"]]["is_eirsaliye_user"]:
                    if party["is_eirsaliye_user"] != 1:
                        doc = frappe.get_doc(party_type, party.name)
                        doc.db_set("is_eirsaliye_user", 1)
                else:
                    if party["is_eirsaliye_user"] == 1:
                        doc = frappe.get_doc(party_type, party.name)
                        doc.db_set("is_eirsaliye_user", 0)
            else:
                if party["is_efatura_user"] == 1:
                    doc = frappe.get_doc(party_type, party.name)
                    doc.db_set("is_efatura_user", 0)
                if party["is_eirsaliye_user"] == 1:
                    doc = frappe.get_doc(party_type, party.name)
                    doc.db_set("is_eirsaliye_user", 0)
    return frappe.utils.now_datetime()


def get_ebelge_users():
    parser = XMLParser(target=EbelgeUsers())
    parser.feed(
        frappe.read_file(frappe.get_site_path("private", "files", "KullaniciListesiXml", "newUserPkList.xml")))
    return parser.close()


def store_ebelge_users(ebelge_users: dict):
    _doctype = "UBL TR User List"
    for legacy in frappe.get_all(doctype=_doctype, fields=["name"]):
        frappe.delete_doc(doctype=_doctype, name=legacy.name)
    for tax_id in ebelge_users.keys():
        ebelge_user = ebelge_users.get(tax_id)
        # create a new document
        doc = frappe.new_doc(_doctype)
        doc.tax_id = tax_id
        doc.is_efatura_user = ebelge_user.get("is_efatura_user")
        doc.is_eirsaliye_user = ebelge_user.get("is_eirsaliye_user")
        doc.company_title = ebelge_user.get("company_title")
        doc.insert()
    return ""


@frappe.whitelist()
def check_all_xml_files():
    hXMLFileHandler = InvoiceHandler()
    # for all *.xml files
    for xmlFile in frappe.get_all('File',
                                  filters={"file_name": ["like", "%.xml"], "is_folder": 0},
                                  fields={"file_url"}):
        # retrieve file path of xmlFile
        filePath: str = frappe.get_site_path() + xmlFile.get('file_url')
        hXMLFileHandler.handle_xml_file(filePath)

    return frappe.utils.now_datetime()
