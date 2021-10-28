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
            read_ebelge_file(xmlFile.get('name'), xmlFile.get('content_hash'))
    return frappe.utils.nowdate()


def read_ebelge_file(file_name, content_hash):
    filename = '/home/tufankaynak/bench/sites/trgibebelgedev/private/files/13D2021000002726.xml'
    # read all namespaces
    namespaces = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
    default_namespace: str = '{' + namespaces.get('') + '}'
    cbc_namespace: str = '{' + namespaces.get('cbc') + '}'
    cac_namespace: str = '{' + namespaces.get('cac') + '}'
    # check if ebelge is Invoice
    if ET.parse(filename).getroot().tag == default_namespace + 'Invoice':
        newdoc = frappe.new_doc('TR GIB eFatura Gelen')
        newdoc.file = file_name
        newdoc.content_hash = content_hash
        is_Invoice_data = True
        Notes = list()  # Seçimli (0...n)
        is_InvoicePeriod_data = False
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
        is_AccountingSupplierPartyPartyPartyIdentification_data = False
        is_AccountingSupplierPartyPartyPartyName_data = False
        is_AccountingSupplierPartyPartyPostalAddress_data = False
        AccountingSupplierPartyPartyPostalAddress_BuildingNumbers = list()  # Seçimli(0..n)

        for event, elem in ET.iterparse(filename, events=("start", "end")):
            if event == 'start':
                if elem.tag == cac_namespace + 'InvoicePeriod':  # Seçimli (0...1)
                    # start processing InvoicePeriod
                    is_InvoicePeriod_data = True
                    is_Invoice_data = False
                    newdoc.invoiceperiod_durationmeasure_unitcode = elem.attrib.get('unitCode')  # Seçimli(0..1)
                if elem.tag == cac_namespace + 'OrderReference':  # Seçimli (0...1)
                    # start processing OrderReference
                    is_OrderReference_data = True
                    is_Invoice_data = False
                if elem.tag == cac_namespace + 'BillingReference':  # Seçimli(0...n)
                    # start processing BillingReference
                    is_BillingReference_data = True
                    is_Invoice_data = False
                    # TODO: BillingReference variables must be reinitialized here
                if elem.tag == cac_namespace + 'PricingExchangeRate':  # Seçimli (0...1)
                    # start processing PricingExchangeRate
                    is_PricingExchangeRate_data = True
                    is_Invoice_data = False
                if elem.tag == cac_namespace + 'AccountingSupplierParty':  # Zorunlu (1)
                    # start processing AccountingSupplierParty
                    # Bu elemanda faturayı düzenleyen tarafın bilgileri yer alacaktır.
                    is_AccountingSupplierParty_data = True
                    is_Invoice_data = False
                if elem.tag == cac_namespace + 'Party' \
                        and is_AccountingSupplierParty_data:
                    # Zorunlu (1)
                    # start processing AccountingSupplierParty\Party
                    # Tarafları (kurum ve şahıslar) tanımlamak için kullanılır.
                    is_AccountingSupplierPartyParty_data = True
                if elem.tag == cac_namespace + 'PartyIdentification' \
                        and is_AccountingSupplierPartyParty_data:
                    # Zorunlu(1..n)
                    # start processing AccountingSupplierParty\Party\PartyIdentification
                    # Tarafın vergi kimlik numarası veya TC kimlik numarası metin olarak girilir.
                    is_AccountingSupplierPartyPartyPartyIdentification_data = True
                    AccountingSupplierPartyPartyPartyIdentification_ID = ''
                    newdoc.accountingsupplierparty_partyidentification_schemeid = elem.attrib.get('schemeID')
                    # Zorunlu(1..n)
                if elem.tag == cac_namespace + 'PartyName' \
                        and is_AccountingSupplierPartyParty_data:
                    # Seçimli(0..1)
                    # start processing AccountingSupplierParty\Party\PartyName
                    # Taraf eğer kurum ise kurum ismi bu elemana metin olarak girilir.
                    is_AccountingSupplierPartyPartyPartyName_data = True
                if elem.tag == cac_namespace + 'PostalAddress' \
                        and is_AccountingSupplierPartyParty_data:
                    # Zorunlu(1)
                    # start sprocessing
                    # Bu eleman adres bilgilerinin tanımlanmasında kullanılacaktır.
                    is_AccountingSupplierPartyPartyPostalAddress_data = True
                if elem.tag == cac_namespace + 'PartyTaxScheme' \
                        and is_AccountingSupplierPartyParty_data:
                    # Zorunlu(1)
                    # start sprocessing
                    # Bu eleman adres bilgilerinin tanımlanmasında kullanılacaktır.
                    is_AccountingSupplierPartyPartyPartyTaxScheme_data = True
                if elem.tag == cac_namespace + 'TaxScheme' \
                        and is_AccountingSupplierPartyParty_data:
                    # Zorunlu(1)
                    # start sprocessing
                    # Bu eleman adres bilgilerinin tanımlanmasında kullanılacaktır.
                    is_AccountingSupplierPartyPartyTaxScheme_data = True

            elif event == 'end':
                # process Invoice
                if is_Invoice_data:
                    if elem.tag == cbc_namespace + 'UBLVersionID':  # Zorunlu (1)
                        newdoc.ublversionid = elem.text
                    elif elem.tag == cbc_namespace + 'CustomizationID':  # Zorunlu (1)
                        newdoc.customizationid = elem.text
                    elif elem.tag == cbc_namespace + 'ProfileID':  # Zorunlu (1)
                        newdoc.profileid = elem.text
                    elif elem.tag == cbc_namespace + 'ID':  # Zorunlu (1)
                        newdoc.id = elem.text
                    elif elem.tag == cbc_namespace + 'CopyIndicator':  # Zorunlu (1)
                        newdoc.copyindicator = elem.text
                    elif elem.tag == cbc_namespace + 'UUID':  # Zorunlu (1)
                        newdoc.uuid = elem.text
                    elif elem.tag == cbc_namespace + 'IssueDate':  # Zorunlu (1)
                        newdoc.issuedate = elem.text
                    elif elem.tag == cbc_namespace + 'IssueTime':  # Seçimli (0...1)
                        newdoc.issuetime = elem.text
                    elif elem.tag == cbc_namespace + 'InvoiceTypeCode':  # Zorunlu (1)
                        newdoc.invoicetypecode = elem.text
                    # TODO: implement this
                    elif elem.tag == cbc_namespace + 'Note':
                        Notes.append(elem.text)
                    elif elem.tag == cbc_namespace + 'DocumentCurrencyCode':  # Zorunlu (1)
                        newdoc.documentcurrencycode = elem.text
                    elif elem.tag == cbc_namespace + 'TaxCurrencyCode':  # Seçimli (0...1)
                        newdoc.taxcurrencycode = elem.text
                    elif elem.tag == cbc_namespace + 'PricingCurrencyCode':  # Seçimli (0...1)
                        newdoc.pricingcurrencycode = elem.text
                    elif elem.tag == cbc_namespace + 'PaymentCurrencyCode':  # Seçimli (0...1)
                        newdoc.paymentcurrencycode = elem.text
                    elif elem.tag == cbc_namespace + 'PaymentAlternativeCurrencyCode':  # Seçimli (0...1)
                        newdoc.paymentalternativecurrencycode = elem.text
                    elif elem.tag == cbc_namespace + 'AccountingCost':  # Seçimli (0...1)
                        newdoc.accountingcost = elem.text
                    elif elem.tag == cbc_namespace + 'LineCountNumeric':  # Zorunlu (1)
                        newdoc.linecountnumeric = elem.text
                        # commit the invoice
                        newdoc.insert()
                # process InvoicePeriod
                if is_InvoicePeriod_data:
                    if elem.tag == cbc_namespace + 'StartDate':  # Seçimli(0..1)
                        newdoc.invoiceperiod_startdate = elem.text
                    elif elem.tag == cbc_namespace + 'StartTime':  # Seçimli(0..1)
                        newdoc.invoiceperiod_starttime = elem.text
                    elif elem.tag == cbc_namespace + 'EndDate':  # Seçimli(0..1)
                        newdoc.invoiceperiod_enddate = elem.text
                    elif elem.tag == cbc_namespace + 'EndTime':  # Seçimli(0..1)
                        newdoc.invoiceperiod_endtime = elem.text
                    elif elem.tag == cbc_namespace + 'DurationMeasure':  # Seçimli(0..1)
                        newdoc.invoiceperiod_durationmeasure = elem.text
                    elif elem.tag == cbc_namespace + 'Description':  # Seçimli(0..1)
                        newdoc.invoiceperiod_description = elem.text
                # end of InvoicePeriod processing
                if elem.tag == cac_namespace + 'InvoicePeriod':
                    is_InvoicePeriod_data = False
                    is_Invoice_data = True
                    newdoc.save()
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
                    if elem.tag == cbc_namespace + 'WebsiteURI':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_websiteuri = elem.text
                    elif elem.tag == cbc_namespace + 'EndpointID':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_endpointid = elem.text
                    elif elem.tag == cbc_namespace + 'IndustryClassificationCode':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_industryclassificationcode = elem.text
                # process AccountingSupplierParty\Party\PartyIdentification
                if is_AccountingSupplierPartyPartyPartyIdentification_data:
                    if elem.tag == cbc_namespace + 'ID':
                        newdoc.accountingsupplierparty_partyidentificationid = elem.text
                # end of AccountingSupplierParty\Party\PartyIdentification processing
                if elem.tag == cac_namespace + 'PartyIdentification' and is_AccountingSupplierPartyParty_data:
                    is_AccountingSupplierPartyParty_data = False
                    newdoc.save()
                # process AccountingSupplierParty\Party\PartyName
                if is_AccountingSupplierPartyPartyPartyName_data:
                    if elem.tag == cbc_namespace + 'Name':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_partyname = elem.text
                # end of AccountingSupplierParty\Party\PartyName processing
                if elem.tag == cac_namespace + 'PartyName' and is_AccountingSupplierPartyParty_data:
                    is_AccountingSupplierPartyPartyPartyName_data = False
                    newdoc.save()
                # process AccountingSupplierParty\Party\PostalAddress
                if is_AccountingSupplierPartyPartyPostalAddress_data:
                    if elem.tag == cbc_namespace + 'ID':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_id = elem.text
                    elif elem.tag == cbc_namespace + 'Postbox':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_postbox = elem.text
                    elif elem.tag == cbc_namespace + 'Room':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_room = elem.text
                    elif elem.tag == cbc_namespace + 'StreetName':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_streetname = elem.text
                    elif elem.tag == cbc_namespace + 'BlockName':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_blockname = elem.text
                    elif elem.tag == cbc_namespace + 'BuildingName':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_buildingname = elem.text
                    elif elem.tag == cbc_namespace + 'BuildingNumber':
                        AccountingSupplierPartyPartyPostalAddress_BuildingNumbers.append(elem.text)
                    elif elem.tag == cbc_namespace + 'CitySubdivisionName':  # Zorunlu(1)
                        newdoc.accountingsupplierparty_postaladdress_citysubdivisionname = elem.text
                    elif elem.tag == cbc_namespace + 'CityName':  # Zorunlu(1)
                        newdoc.accountingsupplierparty_postaladdress_cityname = elem.text
                    elif elem.tag == cbc_namespace + 'PostalZone':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_postalzone = elem.text
                    elif elem.tag == cbc_namespace + 'Region':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_region = elem.text
                    elif elem.tag == cbc_namespace + 'District':  # Seçimli(0..1)
                        newdoc.accountingsupplierparty_postaladdress_district = elem.text
                    elif elem.tag == cbc_namespace + 'Country':  # Zorunlu(1)
                        newdoc.accountingsupplierparty_postaladdress_country = elem.text
                # end of AccountingSupplierParty\Party\PartyName processing
                if elem.tag == cac_namespace + 'PostalAddress' and is_AccountingSupplierPartyParty_data:
                    is_AccountingSupplierPartyPartyPostalAddress_data = False
                    newdoc.save()
