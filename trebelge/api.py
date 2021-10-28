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


@frappe.whitelist()
def check_all_ebelge_files():
    for xmlFile in frappe.get_all('File', filters={"file_name": ["like", "%.xml"], "is_folder": 0},
                                  fields={"name", "content_hash"}):
        # check if record exists by filters
        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "file": xmlFile.get('name'),
                                 "content_hash": xmlFile.get('content_hash')}):
            read_ebelge_file()
    return frappe.utils.nowdate()


def read_ebelge_file():
    filename = '/home/tufankaynak/bench/sites/trgibebelgedev/private/files/13D2021000002726.xml'
    # read all namespaces
    namespaces = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
    default_namespace: str = '{' + namespaces.get('') + '}'
    cbc_namespace: str = '{' + namespaces.get('cbc') + '}'
    cac_namespace: str = '{' + namespaces.get('cac') + '}'
    # check if ebelge is Invoice
    if ET.parse(filename).getroot().tag == default_namespace + 'Invoice':
        is_Invoice_data = True
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
        InvoicePeriod_DurationMeasure_unitCode = ''  # Seçimli(0..1)
        InvoicePeriod_Description = ''  # Seçimli(0..1)
        is_OrderReference_data = False
        OrderReference_ID = ''  # Zorunlu(1)
        OrderReference_SalesOrderID = ''  # Seçimli(0..1)
        OrderReference_IssueDate = ""  # Zorunlu(1)
        OrderReference_OrderTypeCode = ''  # Seçimli(0..1)
        OrderReference_DocumentReferences = list()  # Seçimli(0..n)
        is_BillingReference_data = False
        is_PricingExchangeRate_data = False
        PricingExchangeRate_SourceCurrencyCode = ''  # Zorunlu(1)
        PricingExchangeRate_TargetCurrencyCode = ''  # Zorunlu(1)
        PricingExchangeRate_CalculationRate = ""  # Zorunlu(1)
        PricingExchangeRate_Date = ""  # Seçimli(0..1)
        is_AccountingSupplierParty_data = False
        is_AccountingSupplierPartyParty_data = False
        AccountingSupplierPartyParty_WebsiteURI = ''  # Seçimli(0..1)
        AccountingSupplierPartyParty_EndpointID = ''  # Seçimli(0..1)
        AccountingSupplierPartyParty_IndustryClassificationCode = ''  # Seçimli(0..1)
        is_AccountingSupplierPartyPartyPartyIdentification_data = False
        AccountingSupplierPartyPartyPartyIdentification_schemeID = ''  # Zorunlu(1..n)
        is_AccountingSupplierPartyPartyPartyName_data = False
        is_AccountingSupplierPartyPartyPostalAddress_data = False
        AccountingSupplierPartyPartyPostalAddress_ID = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_Postbox = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_Room = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_StreetName = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_BlockName = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_BuildingName = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_BuildingNumbers = list()  # Seçimli(0..n)
        AccountingSupplierPartyPartyPostalAddress_CitySubdivisionName = ''  # Zorunlu(1)
        AccountingSupplierPartyPartyPostalAddress_CityName = ''  # Zorunlu(1)
        AccountingSupplierPartyPartyPostalAddress_PostalZone = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_Region = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_District = ''  # Seçimli(0..1)
        AccountingSupplierPartyPartyPostalAddress_Country = ''  # Zorunlu(1)

        for event, elem in ET.iterparse(filename, events=("start", "end")):
            if event == 'start':
                if elem.tag == cac_namespace + 'InvoicePeriod':
                    # start processing InvoicePeriod
                    # Seçimli (0...1)
                    is_InvoicePeriod_data = True
                    is_Invoice_data = False
                    InvoicePeriod_DurationMeasure_unitCode = elem.attrib.get('unitCode')
                if elem.tag == cac_namespace + 'OrderReference':
                    # start processing OrderReference
                    # Seçimli (0...1)
                    is_OrderReference_data = True
                    is_Invoice_data = False
                if elem.tag == cac_namespace + 'BillingReference':
                    # start processing BillingReference
                    # Seçimli(0...n)
                    is_BillingReference_data = True
                    is_Invoice_data = False
                    # TODO: BillingReference variables must be reinitialized here
                if elem.tag == cac_namespace + 'PricingExchangeRate':
                    # start processing PricingExchangeRate
                    # Seçimli (0...1)
                    is_PricingExchangeRate_data = True
                    is_Invoice_data = False
                if elem.tag == cac_namespace + 'AccountingSupplierParty':
                    # start processing AccountingSupplierParty
                    # Zorunlu (1)
                    # Bu elemanda faturayı düzenleyen tarafın bilgileri yer alacaktır.
                    is_AccountingSupplierParty_data = True
                    is_Invoice_data = False
                if elem.tag == cac_namespace + 'Party' and is_AccountingSupplierParty_data:
                    # start processing AccountingSupplierParty\Party
                    # Zorunlu (1)
                    # Tarafları (kurum ve şahıslar) tanımlamak için kullanılır.
                    is_AccountingSupplierPartyParty_data = True
                if elem.tag == cac_namespace + 'PartyIdentification' and is_AccountingSupplierPartyParty_data:
                    # start processing AccountingSupplierParty\Party\PartyIdentification
                    # Zorunlu(1..n)
                    # Tarafın vergi kimlik numarası veya TC kimlik numarası metin olarak girilir.
                    is_AccountingSupplierPartyPartyPartyIdentification_data = True
                    AccountingSupplierPartyPartyPartyIdentification_ID = ''
                    AccountingSupplierPartyPartyPartyIdentification_schemeID = elem.attrib.get('schemeID')
                if elem.tag == cac_namespace + 'PartyName' and is_AccountingSupplierPartyParty_data:
                    # start processing AccountingSupplierParty\Party\PartyName
                    # Seçimli(0..1)
                    # Taraf eğer kurum ise kurum ismi bu elemana metin olarak girilir.
                    is_AccountingSupplierPartyPartyPartyName_data = True
                if elem.tag == 'PostalAddress' and is_AccountingSupplierPartyParty_data:
                    # start sprocessing
                    # Zorunlu(1)
                    # Bu eleman adres bilgilerinin tanımlanmasında kullanılacaktır.
                    is_AccountingSupplierPartyPartyPostalAddress_data = True

            elif event == 'end':
                # process Invoice
                if is_Invoice_data:
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
                if is_InvoicePeriod_data:
                    if elem.tag == cbc_namespace + 'StartDate':
                        InvoicePeriod_StartDate = elem.text
                    elif elem.tag == cbc_namespace + 'StartTime':
                        InvoicePeriod_StartTime = elem.text
                    elif elem.tag == cbc_namespace + 'EndDate':
                        InvoicePeriod_EndDate = elem.text
                    elif elem.tag == cbc_namespace + 'EndTime':
                        InvoicePeriod_EndTime = elem.text
                    elif elem.tag == cbc_namespace + 'DurationMeasure':
                        InvoicePeriod_DurationMeasure = elem.text
                    elif elem.tag == cbc_namespace + 'Description':
                        InvoicePeriod_Description = elem.text
                # end of InvoicePeriod processing
                if elem.tag == cac_namespace + 'InvoicePeriod':
                    is_InvoicePeriod_data = False
                    is_Invoice_data = True
                # process OrderReference
                if is_OrderReference_data:
                    if elem.tag == cbc_namespace + 'ID':
                        OrderReference_ID = elem.text
                    elif elem.tag == cbc_namespace + 'SalesOrderID':
                        OrderReference_SalesOrderID = elem.text
                    elif elem.tag == cbc_namespace + 'IssueDate':
                        OrderReference_IssueDate = elem.text
                    elif elem.tag == cbc_namespace + 'OrderTypeCode':
                        OrderReference_OrderTypeCode = elem.text
                    elif elem.tag == cbc_namespace + 'DocumentReference':
                        OrderReference_DocumentReferences.append(elem.text)
                # end of OrderReference processing
                if elem.tag == cac_namespace + 'OrderReference':
                    is_OrderReference_data = False
                    is_Invoice_data = True
                # process AccountingSupplierParty\Party
                if is_AccountingSupplierPartyParty_data:
                    if elem.tag == cbc_namespace + 'WebsiteURI':
                        AccountingSupplierPartyParty_WebsiteURI = elem.text
                    elif elem.tag == cbc_namespace + 'EndpointID':
                        AccountingSupplierPartyParty_EndpointID = elem.text
                    elif elem.tag == cbc_namespace + 'IndustryClassificationCode':
                        AccountingSupplierPartyParty_IndustryClassificationCode = elem.text
                # process AccountingSupplierParty\Party\PartyIdentification
                if is_AccountingSupplierPartyPartyPartyIdentification_data:
                    if elem.tag == cbc_namespace + 'ID':
                        AccountingSupplierPartyPartyPartyIdentification_ID = elem.text
                # end of AccountingSupplierParty\Party\PartyIdentification processing
                if elem.tag == cac_namespace + 'PartyIdentification' and is_AccountingSupplierPartyParty_data:
                    is_AccountingSupplierPartyParty_data = False
                # process AccountingSupplierParty\Party\PartyName
                if is_AccountingSupplierPartyPartyPartyName_data:
                    if elem.tag == cbc_namespace + 'Name':
                        AccountingSupplierPartyPartyPartyName_Name = elem.text
                # end of AccountingSupplierParty\Party\PartyName processing
                if elem.tag == cac_namespace + 'PartyName' and is_AccountingSupplierPartyParty_data:
                    is_AccountingSupplierPartyPartyPartyName_data = False
                # process AccountingSupplierParty\Party\PostalAddress
                if is_AccountingSupplierPartyPartyPostalAddress_data:
                    if elem.tag == cbc_namespace + 'ID':
                        AccountingSupplierPartyPartyPostalAddress_ID = elem.text
                    elif elem.tag == cbc_namespace + 'Postbox':
                        AccountingSupplierPartyPartyPostalAddress_Postbox = elem.text
                    elif elem.tag == cbc_namespace + 'Room':
                        AccountingSupplierPartyPartyPostalAddress_Room = elem.text
                    elif elem.tag == cbc_namespace + 'StreetName':
                        AccountingSupplierPartyPartyPostalAddress_StreetName = elem.text
                    elif elem.tag == cbc_namespace + 'BlockName':
                        AccountingSupplierPartyPartyPostalAddress_BlockName = elem.text
                    elif elem.tag == cbc_namespace + 'BuildingName':
                        AccountingSupplierPartyPartyPostalAddress_BuildingName = elem.text
                    elif elem.tag == cbc_namespace + 'BuildingNumber':
                        AccountingSupplierPartyPartyPostalAddress_BuildingNumbers.append(elem.text)
                    elif elem.tag == cbc_namespace + 'CitySubdivisionName':
                        AccountingSupplierPartyPartyPostalAddress_CitySubdivisionName = elem.text
                    elif elem.tag == cbc_namespace + 'CityName':
                        AccountingSupplierPartyPartyPostalAddress_CityName = elem.text
                    elif elem.tag == cbc_namespace + 'PostalZone':
                        AccountingSupplierPartyPartyPostalAddress_PostalZone = elem.text
                    elif elem.tag == cbc_namespace + 'Region':
                        AccountingSupplierPartyPartyPostalAddress_Region = elem.text
                    elif elem.tag == cbc_namespace + 'District':
                        AccountingSupplierPartyPartyPostalAddress_District = elem.text
                    elif elem.tag == cbc_namespace + 'Country':
                        AccountingSupplierPartyPartyPostalAddress_Country = elem.text
                # end of AccountingSupplierParty\Party\PartyName processing
                if elem.tag == cac_namespace + 'PostalAddress' and is_AccountingSupplierPartyParty_data:
                    is_AccountingSupplierPartyPartyPostalAddress_data = False
