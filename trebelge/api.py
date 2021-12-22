from xml.etree.ElementTree import XMLParser

import frappe
from trebelge.EbelgeUsers import EbelgeUsers
from trebelge.XMLFileCoR import AbstractXMLFileHandler
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler


@frappe.whitelist()
def check_all_ebelge_parties():
    ebelge_users = get_ebelge_users()
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


@frappe.whitelist()
def check_all_xml_files():
    # for all *.xml files
    for xmlFile in frappe.get_all('File', filters={"file_name": ["like", "%.xml"], "is_folder": 0},
                                  fields={"file_url"}):
        # retrieve file path of xmlFile
        filePath: str = frappe.get_site_path() + xmlFile.get('file_url')
        hXMLFileHandler: AbstractXMLFileHandler = InvoiceHandler()
        hXMLFileHandler.handle_xml_file(filePath)
        # initiate Context of State pattern
        # stateContext = XMLFileStateContext()
        # handle file by CoR to determine State
        # stateContext.set_state(hXMLFileHandler.handle_xml_file(filePath))
        # initiate Context of State pattern for FileType
        # stateContext.set_file_path(filePath)
        # check on State if file is previously processed and recorded
        # stateContext.find_ebelge_status()
        # process xml file
        # stateContext.read_xml_file()

    return frappe.utils.now_datetime()
