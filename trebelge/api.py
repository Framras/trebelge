import frappe
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import XMLParser
from trebelge.EbelgeUsers import EbelgeUsers


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
    cac_namespace: str = '{' + namespaces.get('cac') + '}'
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
        PaymentCurrencyCode = ''  # Seçimli (0...1)
        PaymentAlternativeCurrencyCode = ''  # Seçimli (0...1)
        AccountingCost = ''  # Seçimli (0...1)
        LineCountNumeric = ""  # Zorunlu (1)
        is_InvoicePeriod_data = False
        InvoicePeriod_StartDate = ""  # Seçimli(0..1)
        InvoicePeriod_StartTime = ""  # Seçimli(0..1)
        InvoicePeriod_EndDate = ""  # Seçimli(0..1)
        InvoicePeriod_EndTime = ""  # Seçimli(0..1)
        InvoicePeriod_DurationMeasure = ""  # Seçimli(0..1)
        InvoicePeriod_Description = ''  # Seçimli(0..1)
        is_OrderReference_data = False
        OrderReference_ID = ''  # Zorunlu(1)
        OrderReference_SalesOrderID = ''  # Seçimli(0..1)
        OrderReference_IssueDate = ""  # Zorunlu(1)
        OrderReference_OrderTypeCode = ''  # Seçimli(0..1)
        OrderReference_DocumentReferences = list()  # Seçimli(0..n)
        is_BillingReference_data = False

        for event, elem in ET.iterparse(filename, events=("start", "end")):
            if event == 'start':
                if elem.tag == cac_namespace + 'InvoicePeriod':
                    # start processing InvoicePeriod
                    # Seçimli (0...1)
                    is_InvoicePeriod_data = True
                    InvoicePeriod_StartDate = ""
                    InvoicePeriod_StartTime = ""
                    InvoicePeriod_EndDate = ""
                    InvoicePeriod_EndTime = ""
                    InvoicePeriod_DurationMeasure = ""
                    InvoicePeriod_Description = ''
                if elem.tag == cac_namespace + 'OrderReference':
                    # start processing OrderReference
                    # Seçimli (0...1)
                    is_OrderReference_data = True
                    OrderReference_ID = ''  # Zorunlu(1)
                    OrderReference_SalesOrderID = ''  # Seçimli(0..1)
                    OrderReference_IssueDate = ""  # Zorunlu(1)
                    OrderReference_OrderTypeCode = ''  # Seçimli(0..1)
                    OrderReference_DocumentReferences = list()  # Seçimli(0..n)
                if elem.tag == cac_namespace + 'BillingReference':
                    # start processing BillingReference
                    # Seçimli(0...n)
                    is_BillingReference_data = True
                if elem.tag == cac_namespace + 'PricingExchangeRate':
                    # start processing PricingExchangeRate
                    # Seçimli (0...1)
                    is_PricingExchangeRate_data = True
                    PricingExchangeRate_SourceCurrencyCode = ''  # Zorunlu(1)
                    PricingExchangeRate_TargetCurrencyCode = ''  # Zorunlu(1)
                    PricingExchangeRate_CalculationRate = ""  # Zorunlu(1)
                    PricingExchangeRate_Date = ""  # Seçimli(0..1)

            elif event == 'end':
                # process the tags
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
                elif elem.tag == cbc_namespace + 'PaymentCurrencyCode':
                    PaymentCurrencyCode = elem.text
                elif elem.tag == cbc_namespace + 'PaymentAlternativeCurrencyCode':
                    PaymentAlternativeCurrencyCode = elem.text
                elif elem.tag == cbc_namespace + 'AccountingCost':
                    AccountingCost = elem.text
                elif elem.tag == cbc_namespace + 'LineCountNumeric':
                    LineCountNumeric = elem.text
                # process InvoicePeriod
                if elem.tag == cbc_namespace + 'StartDate' and is_InvoicePeriod_data:
                    InvoicePeriod_StartDate = elem.text
                elif elem.tag == cbc_namespace + 'StartTime' and is_InvoicePeriod_data:
                    InvoicePeriod_StartTime = elem.text
                elif elem.tag == cbc_namespace + 'EndDate' and is_InvoicePeriod_data:
                    InvoicePeriod_EndDate = elem.text
                elif elem.tag == cbc_namespace + 'EndTime' and is_InvoicePeriod_data:
                    InvoicePeriod_EndTime = elem.text
                elif elem.tag == cbc_namespace + 'DurationMeasure' and is_InvoicePeriod_data:
                    InvoicePeriod_DurationMeasure = elem.text
                elif elem.tag == cbc_namespace + 'InvoicePeriod_Description' and is_InvoicePeriod_data:
                    InvoicePeriod_Description = elem.text
                # end of InvoicePeriod processing
                if elem.tag == cac_namespace + 'InvoicePeriod':
                    is_InvoicePeriod_data = False
                # process OrderReference
                if elem.tag == cbc_namespace + 'ID' and is_OrderReference_data:
                    OrderReference_ID = elem.text
                elif elem.tag == cbc_namespace + 'SalesOrderID' and is_OrderReference_data:
                    OrderReference_SalesOrderID = elem.text
                elif elem.tag == cbc_namespace + 'IssueDate' and is_OrderReference_data:
                    OrderReference_IssueDate = elem.text
                elif elem.tag == cbc_namespace + 'OrderTypeCode' and is_OrderReference_data:
                    OrderReference_OrderTypeCode = elem.text
                # end of OrderReference processing
                if elem.tag == cac_namespace + 'OrderReference':
                    is_OrderReference_data = False
