import frappe
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import XMLParser
from trebelge.EbelgeUsers import EbelgeUsers
from trebelge.incomingEfaturaReader import incomingEfaturaReader


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
    return frappe.utils.nowdate()


def get_ebelge_users():
    parser = XMLParser(target=EbelgeUsers())
    parser.feed(
        frappe.read_file(frappe.get_site_path("private", "files", "KullaniciListesiXml", "newUserPkList.xml")))
    return parser.close()


def read_ebelge_file():
    filename = '/home/tufankaynak/bench/sites/trgibebelgedev/private/files/13D2021000002726.xml'
    # read all namespaces
    namespaces = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
    default_namespace: str = '{' + namespaces.get('') + '}'
    cbc_namespace: str = '{' + namespaces.get('cbc') + '}'
    # check if ebelge is Invoice
    if ET.parse(filename).getroot().tag == default_namespace + 'Invoice':
        UBLVersionID = ''  # Zorunlu (1)
        CustomizationID = ''  # Zorunlu (1)
        ProfileID = ''  # Zorunlu (1)
        ID = ''  # Zorunlu (1)
        CopyIndicator = ""  # Zorunlu (1)
        UUID = ''  # Zorunlu (1)
        IssueDate = ""  # Zorunlu (1)
        IssueTime = ""  # Seçimli (0...1)
        InvoiceTypeCode = ''  # Zorunlu (1)
        Notes = list()  # Seçimli (0...n)
        DocumentCurrencyCode = ''  # Zorunlu (1)
        TaxCurrencyCode = ''  # Seçimli (0...1)
        PricingCurrencyCode = ''  # Seçimli (0...1)
        LineCountNumeric = ""

        for event, elem in ET.iterparse(filename, events=("start", "end")):
            if event == 'start':
                pass
            elif event == 'end':
                # process the tag
                if elem.tag == cbc_namespace + 'UBLVersionID':
                    UBLVersionID = elem.text
                elif elem.tag == cbc_namespace + 'CustomizationID':
                    CustomizationID = elem.text
                elif elem.tag == cbc_namespace + 'ProfileID':
                    ProfileID = elem.text
                elif elem.tag == cbc_namespace + 'ID':
                    ID = elem.text
                elif elem.tag == cbc_namespace + 'CopyIndicator':
                    CopyIndicator = elem.text
                elif elem.tag == cbc_namespace + 'UUID':
                    UUID = elem.text
                elif elem.tag == cbc_namespace + 'IssueDate':
                    IssueDate = elem.text
                elif elem.tag == cbc_namespace + 'IssueTime':
                    IssueTime = elem.text
                elif elem.tag == cbc_namespace + 'InvoiceTypeCode':
                    InvoiceTypeCode = elem.text
                elif elem.tag == cbc_namespace + 'Note':
                    Notes.append(elem.text)
                elif elem.tag == cbc_namespace + 'DocumentCurrencyCode':
                    DocumentCurrencyCode = elem.text
                elif elem.tag == cbc_namespace + 'TaxCurrencyCode':
                    TaxCurrencyCode = elem.text
                elif elem.tag == cbc_namespace + 'PricingCurrencyCode':
                    PricingCurrencyCode = elem.text
                elif elem.tag == cbc_namespace + 'LineCountNumeric':
                    LineCountNumeric = elem.text
