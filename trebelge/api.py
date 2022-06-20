from xml.etree.ElementTree import XMLParser

import frappe
from trebelge.EbelgeUsers import EbelgeUsers
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler


@frappe.whitelist()
def check_all_ebelge_parties():
    parser = XMLParser(target=EbelgeUsers())
    parser.feed(
        frappe.read_file(frappe.get_site_path("private", "files", "KullaniciListesiXml", "newUserPkList.xml")))
    return parser.close()


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
