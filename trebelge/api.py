import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler


@frappe.whitelist()
def check_all_ebelge_parties():
    file_path = frappe.get_site_path("private", "files", "KullaniciListesiXml", "newUserPkList.xml")
    root_: Element = ET.parse(file_path).getroot()
    party_types = ["Customer", "Supplier"]
    for party_type in party_types:
        parties: list = frappe.get_all(party_type,
                                       filters={"tax_id": ["not in", None], "disabled": 0},
                                       fields={"name"})
        if len(parties) != 0:
            for party in parties:
                doc: Document = frappe.get_doc(party_type, party.name)
                save_doc = False
                user_: Element = root_.find("./User/[Identifier='" + doc.get_value("tax_id") + "']")
                if user_ is not None:
                    invoice_: Element = user_.find("./Documents/Document/[@type=""Invoice""]")
                    if invoice_ is not None:
                        created_times = len(invoice_.findall('./Alias/CreationTime'))
                        deleted_times = len(invoice_.findall('./Alias/DeletionTime'))
                        if created_times > deleted_times:
                            if doc.is_efatura_user == 0:
                                doc.is_efatura_user = 1
                                save_doc = True
                        elif created_times == deleted_times:
                            if doc.is_efatura_user == 1:
                                doc.is_efatura_user = 0
                                save_doc = True
                    despatchadvice_: Element = user_.find("./Documents/Document/[@type=""DespatchAdvice""]")
                    if despatchadvice_ is not None:
                        created_times = len(invoice_.findall('./Alias/CreationTime'))
                        deleted_times = len(invoice_.findall('./Alias/DeletionTime'))
                        if created_times > deleted_times:
                            if doc.is_eirsaliye_user == 0:
                                doc.is_eirsaliye_user = 1
                                save_doc = True
                        elif created_times == deleted_times:
                            if doc.is_eirsaliye_user == 1:
                                doc.is_eirsaliye_user = 0
                                save_doc = True
                else:
                    if doc.is_efatura_user == 1:
                        doc.is_efatura_user = 0
                        save_doc = True
                    if doc.is_eirsaliye_user == 1:
                        doc.is_eirsaliye_user = 0
                        save_doc = True

                if save_doc:
                    doc.save()

    return frappe.utils.now_datetime()


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
