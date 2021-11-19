# from __future__ import annotations
import xml.etree.ElementTree as ET

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class NewInvoiceState(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR UBL Received Invoice'
    _mapping = dict()

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu (1): UBLVersionID
        self._mapping['UBLVersionID'] = ('cbc', 'ublversionid', 'Zorunlu (1)', False, False, True)
        # Zorunlu (1): CustomizationID
        self._mapping['CustomizationID'] = ('cbc', 'customizationid', 'Zorunlu (1)', False, False, True)
        # Zorunlu (1): ProfileID
        self._mapping['ProfileID'] = ('cbc', 'profileid', 'Zorunlu (1)', False, False, True)
        # Zorunlu (1): ID
        self._mapping['ID'] = ('cbc', 'id', 'Zorunlu (1)', False, False, True)
        # Zorunlu (1): CopyIndicator
        self._mapping['CopyIndicator'] = ('cbc', 'copyindicator', 'Zorunlu (1)', False, False, True)
        # Zorunlu (1): UUID
        self._mapping['UUID'] = ('cbc', 'uuid', 'Zorunlu (1)', False, False, True)
        # Zorunlu (1): IssueDate
        self._mapping['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu (1)', False, False, True)
        # Zorunlu (1): IssueTime
        self._mapping['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)', False, False, True)
        # Zorunlu (1): InvoiceTypeCode
        self._mapping['InvoiceTypeCode'] = ('cbc', 'invoicetypecode', 'Zorunlu (1)', False, False, True)
        # Seçimli (0...n): Note
        self._mapping['Note'] = ('cbc', 'notes', 'Seçimli (0...n)', False, False, True)
        # Zorunlu (1): DocumentCurrencyCode
        self._mapping['DocumentCurrencyCode'] = ('cbc', 'documentcurrencycode', 'Zorunlu (1)', False, False, True)
        # Seçimli (0...1): TaxCurrencyCode
        self._mapping['TaxCurrencyCode'] = ('cbc', 'taxcurrencycode', 'Seçimli (0...1)', False, False, True)
        # Seçimli (0...1): PricingCurrencyCode
        self._mapping['PricingCurrencyCode'] = ('cbc', 'pricingcurrencycode', 'Seçimli (0...1)', False, False, True)
        # Seçimli (0...1): PaymentCurrencyCode
        self._mapping['PaymentCurrencyCode'] = ('cbc', 'paymentcurrencycode', 'Seçimli (0...1)', False, False, True)
        # Seçimli (0...1): PaymentAlternativeCurrencyCode
        self._mapping['PaymentAlternativeCurrencyCode'] = (
            'cbc', 'paymentalternativecurrencycode', 'Seçimli (0...1)', False, False, True)
        # Seçimli (0...1): AccountingCost
        self._mapping['AccountingCost'] = ('cbc', 'accountingcost', 'Seçimli (0...1)', False, False, True)
        # Zorunlu (1): LineCountNumeric
        self._mapping['LineCountNumeric'] = ('cbc', 'linecountnumeric', 'Zorunlu (1)', False, False, True)
        # Seçimli (0...1): InvoicePeriod:Period
        self._mapping['InvoicePeriod'] = ('cac', 'Period', 'Seçimli (0...1)', True, False, False)
        # Seçimli (0...1): OrderReference:OrderReference
        self._mapping['OrderReference'] = ('cac', 'OrderReference', 'Seçimli (0...1)', True, False, False)
        # Seçimli (0...n): BillingReference:BillingReference
        self._mapping['BillingReference'] = ('cac', 'BillingReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli (0...n): DespatchDocumentReference:DocumentReference
        self._mapping['DespatchDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli (0...n): ReceiptDocumentReference:DocumentReference
        self._mapping['ReceiptDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli (0...n): OriginatorDocumentReference:DocumentReference
        self._mapping['OriginatorDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli (0...n): ContractDocumentReference:DocumentReference
        self._mapping['ContractDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli (0...n): AdditionalDocumentReference:DocumentReference
        self._mapping['AdditionalDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        # Zorunlu (1...n): Signature:Signature
        self._mapping['Signature'] = ('cac', 'Signature', 'Zorunlu (1...n)', True, False, False)
        # Zorunlu (1): AccountingSupplierParty:SupplierParty
        self._mapping['AccountingSupplierParty'] = ('cac', 'SupplierParty', 'Zorunlu (1)', True, False, False)
        # Zorunlu (1): AccountingCustomerParty:CustomerParty
        self._mapping['AccountingCustomerParty'] = ('cac', 'CustomerParty', 'Zorunlu (1)', True, False, False)
        # Seçimli (0..1): BuyerCustomerParty:CustomerParty
        self._mapping['BuyerCustomerParty'] = ('cac', 'CustomerParty', 'Seçimli (0..1)', True, False, False)
        # Seçimli (0..1): SellerSupplierParty:SupplierParty
        self._mapping['SellerSupplierParty'] = ('cac', 'SupplierParty', 'Seçimli (0..1)', True, False, False)
        # Seçimli (0..1): TaxRepresentativeParty:Party
        self._mapping['TaxRepresentativeParty'] = (
            'cac', 'Party', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..n): Delivery:Delivery
        self._mapping['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): PaymentMeans:PaymentMeans
        self._mapping['PaymentMeans'] = ('cac', 'PaymentMeans', 'Seçimli (0...n)', True, False, False)
        # Seçimli (0..1): PaymentTerms:PaymentTerms
        self._mapping['PaymentTerms'] = ('cac', 'PaymentTerms', 'Seçimli (0..1)', True, False, False)
        # Seçimli (0...n): AllowanceCharge:AllowanceCharge
        self._mapping['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)', True, False, False)
        # Seçimli (0...1): TaxExchangeRate:ExchangeRate
        self._mapping['TaxExchangeRate'] = ('cac', 'ExchangeRate', 'Seçimli (0..1)', True, False, False)
        # Seçimli (0...1): PricingExchangeRate:ExchangeRate
        self._mapping['PricingExchangeRate'] = ('cac', 'ExchangeRate', 'Seçimli (0..1)', True, False, False)
        # Seçimli (0...1): PaymentExchangeRate:ExchangeRate
        self._mapping['PaymentExchangeRate'] = ('cac', 'ExchangeRate', 'Seçimli (0..1)', True, False, False)
        # Seçimli (0...1): PaymentAlternativeExchangeRate:ExchangeRate
        self._mapping['PaymentAlternativeExchangeRate'] = (
            'cac', 'ExchangeRate', 'Seçimli (0..1)', True, False, False)
        # Zorunlu (1...n): TaxTotal:TaxTotal
        self._mapping['TaxTotal'] = ('cac', 'TaxTotal', 'Zorunlu (1...n)', True, False, False)
        # Seçimli (0...n): WithholdingTaxTotal:TaxTotal
        self._mapping['WithholdingTaxTotal'] = ('cac', 'WithholdingTaxTotal', 'Seçimli (0...n)', True, False, False)
        # Zorunlu (1): LegalMonetaryTotal:LegalMonetaryTotal
        self._mapping['LegalMonetaryTotal'] = ('cac', 'LegalMonetaryTotal', 'Zorunlu (1)', True, False, False)
        # Zorunlu (1...n): InvoiceLine:InvoiceLine
        self._mapping['InvoiceLine'] = ('cac', 'InvoiceLine', 'Zorunlu (1...n)', True, False, False)

        "invoiceperiod_startdate"
        "invoiceperiod_starttime"
        "invoiceperiod_durationmeasure"
        "invoiceperiod_enddate"
        "invoiceperiod_endtime"
        "invoiceperiod_durationmeasure_unitcode"
        "invoiceperiod_description"

        "orderreference_id"
        "orderreference_salesorderid"
        "orderreference_issuedate"
        "orderreference_ordertypecode"
        "orderreference_documentreference"

        "billingreference"
        "despatchdocumentreference"
        "receiptdocumentreference"
        "originatordocumentreference"
        "contractdocumentreference"
        "additionaldocumentreference"
        "signature"

        "accountingsupplierparty_websiteuri"
        "accountingsupplierparty_partyidentification_schemeid"
        "accountingsupplierparty_partyidentificationid"
        "accountingsupplierparty_partyname"
        "accountingsupplierparty_industryclassificationcode"
        "accountingsupplierparty_endpointid"
        "accountingsupplierparty_postaladdress_id"
        "accountingsupplierparty_postaladdress_postbox"
        "accountingsupplierparty_postaladdress_room"
        "accountingsupplierparty_postaladdress_streetname"
        "accountingsupplierparty_postaladdress_blockname"
        "accountingsupplierparty_postaladdress_buildingname"
        "accountingsupplierparty_postaladdress_buildingnumber"
        "accountingsupplierparty_postaladdress_citysubdivisionname"
        "accountingsupplierparty_postaladdress_cityname"
        "accountingsupplierparty_postaladdress_postalzone"
        "accountingsupplierparty_postaladdress_region"
        "accountingsupplierparty_postaladdress_district"
        "accountingsupplierparty_postaladdress_country"
        "accountingcustomerparty"
        "buyercustomerparty"
        "sellersupplierparty"
        "taxrepresentativeparty"

        "taxexchangerate_sourcecurrencycode"
        "taxexchangerate_date"
        "taxexchangerate_targetcurrencycode"
        "taxexchangerate_calculationrate"

        "pricingexchangerate_sourcecurrencycode"
        "pricingexchangerate_date"
        "pricingexchangerate_targetcurrencycode"
        "pricingexchangerate_calculationrate"

        "paymentexchangerate_sourcecurrencycode"
        "paymentexchangerate_date"
        "paymentexchangerate_targetcurrencycode"
        "paymentexchangerate_calculationrate"

        "paymentalternativeexchangerate_sourcecurrencycode"
        "paymentalternativeexchangerate_date"
        "paymentalternativeexchangerate_targetcurrencycode"
        "paymentalternativeexchangerate_calculationrate"

    def read_element_by_action(self, event: str, element: ET.Element):
        tag: str = ''
        if element.tag.startswith(self.get_context().get_cac_namespace()):
            tag = element.tag[len(self.get_context().get_cac_namespace()):]
        elif element.tag.startswith(self.get_context().get_cbc_namespace()):
            tag = element.tag[len(self.get_context().get_cbc_namespace()):]
        if self._mapping[tag] is not None:
            if event == 'start' and self._mapping[tag][3]:
                if self._mapping[tag][4]:
                    for key in element.attrib.keys():
                        if self._mapping[key] is not None:
                            self.get_context().set_new_frappe_doc(
                                self._mapping[key][1], element.attrib.get(key))
            elif event == 'end' and self._mapping[tag][5]:

    def read_xml_file(self):
        self.get_context().set_new_frappe_doc('doctype', self._frappeDoctype)
        for event, elem in ET.iterparse(self.get_context().get_file_path(), events=("start", "end")):
            self.get_context().read_element_by_action(event, elem)
