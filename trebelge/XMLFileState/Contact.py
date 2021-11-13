# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Contact(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['UBLVersionID'] = ('cbc', 'ublversionid', 'Zorunlu (1)', False, False, True)
        self._mapping['CustomizationID'] = ('cbc', 'customizationid', 'Zorunlu (1)', False, False, True)
        self._mapping['ProfileID'] = ('cbc', 'profileid', 'Zorunlu (1)', False, False, True)
        self._mapping['ID'] = ('cbc', 'id', 'Zorunlu (1)', False, False, True)
        self._mapping['CopyIndicator'] = ('cbc', 'copyindicator', 'Zorunlu (1)', False, False, True)
        self._mapping['UUID'] = ('cbc', 'uuid', 'Zorunlu (1)', False, False, True)
        self._mapping['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu (1)', False, False, True)
        self._mapping['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)', False, False, True)
        self._mapping['InvoiceTypeCode'] = ('cbc', 'invoicetypecode', 'Zorunlu (1)', False, False, True)
        self._mapping['Note'] = ('cbc', 'note', 'Seçimli (0...n)', False, False, True)
        self._mapping['DocumentCurrencyCode'] = ('cbc', 'documentcurrencycode', 'Zorunlu (1)', False, False, True)
        self._mapping['TaxCurrencyCode'] = ('cbc', 'taxcurrencycode', 'Seçimli (0...1)', False, False, True)
        self._mapping['PricingCurrencyCode'] = ('cbc', 'pricingcurrencycode', 'Seçimli (0...1)', False, False, True)
        self._mapping['PaymentCurrencyCode'] = ('cbc', 'paymentcurrencycode', 'Seçimli (0...1)', False, False, True)
        self._mapping['PaymentAlternativeCurrencyCode'] = (
            'cbc', 'paymentalternativecurrencycode', 'Seçimli (0...1)', False, False, True)
        self._mapping['AccountingCost'] = ('cbc', 'accountingcost', 'Seçimli (0...1)', False, False, True)
        self._mapping['LineCountNumeric'] = ('cbc', 'linecountnumeric', 'Zorunlu (1)', False, False, True)
        self._mapping['InvoicePeriod'] = ('cac', 'InvoicePeriod', 'Seçimli (0...1)', True, False, False)
        self._mapping['OrderReference'] = ('cac', 'OrderReference', 'Seçimli (0...1)', True, False, False)
        self._mapping['BillingReference'] = ('cac', 'BillingReference', 'Seçimli (0...n)', True, False, False)
        self._mapping['DespatchDocumentReference'] = (
            'cac', 'DespatchDocumentReference', 'Seçimli (0...n)', True, False, False)
        self._mapping['ReceiptDocumentReference'] = (
            'cac', 'ReceiptDocumentReference', 'Seçimli (0...n)', True, False, False)
        self._mapping['OriginatorDocumentReference'] = (
            'cac', 'OriginatorDocumentReference', 'Seçimli (0...n)', True, False, False)
        self._mapping['ContractDocumentReference'] = (
            'cac', 'ContractDocumentReference', 'Seçimli (0...n)', True, False, False)
        self._mapping['AdditionalDocumentReference'] = (
            'cac', 'AdditionalDocumentReference', 'Seçimli (0...n)', True, False, False)
        self._mapping['Signature'] = ('cac', 'Signature', 'Zorunlu (1...n)', True, False, False)
        self._mapping['AccountingSupplierParty'] = ('cac', 'AccountingSupplierParty', 'Zorunlu (1)', True, False, False)
        self._mapping['AccountingCustomerParty'] = ('cac', 'AccountingCustomerParty', 'Zorunlu (1)', True, False, False)
        self._mapping['BuyerCustomerParty'] = ('cac', 'BuyerCustomerParty', 'Seçimli (0..1)', True, False, False)
        self._mapping['SellerSupplierParty'] = ('cac', 'SellerSupplierParty', 'Seçimli (0..1)', True, False, False)
        self._mapping['TaxRepresentativeParty'] = (
            'cac', 'TaxRepresentativeParty', 'Seçimli (0..1)', True, False, False)
        self._mapping['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)', True, False, False)
        self._mapping['PaymentMeans'] = ('cac', 'PaymentMeans', 'Seçimli (0...n)', True, False, False)
        self._mapping['PaymentTerms'] = ('cac', 'PaymentTerms', 'Seçimli (0..1)', True, False, False)
        self._mapping['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)', True, False, False)
        self._mapping['TaxExchangeRate'] = ('cac', 'TaxExchangeRate', 'Seçimli (0..1)', True, False, False)
        self._mapping['PricingExchangeRate'] = ('cac', 'PricingExchangeRate', 'Seçimli (0..1)', True, False, False)
        self._mapping['PaymentExchangeRate'] = ('cac', 'PaymentExchangeRate', 'Seçimli (0..1)', True, False, False)
        self._mapping['PaymentAlternativeExchangeRate'] = (
            'cac', 'PaymentAlternativeExchangeRate', 'Seçimli (0..1)', True, False, False)
        self._mapping['TaxTotal'] = ('cac', 'TaxTotal', 'Zorunlu (1...n)', True, False, False)
        self._mapping['WithholdingTaxTotal'] = ('cac', 'WithholdingTaxTotal', 'Seçimli (0...n)', True, False, False)
        self._mapping['LegalMonetaryTotal'] = ('cac', 'LegalMonetaryTotal', 'Zorunlu (1)', True, False, False)
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
        "column_break_vergi_doviz_kuru"
        "taxexchangerate_targetcurrencycode"
        "taxexchangerate_calculationrate"

        "pricingexchangerate_sourcecurrencycode"
        "pricingexchangerate_date"
        "column_break_fiyatlandirma_doviz_kuru"
        "pricingexchangerate_targetcurrencycode"
        "pricingexchangerate_calculationrate"

        "paymentexchangerate_sourcecurrencycode"
        "paymentexchangerate_date"
        "column_break_odeme_doviz_kuru"
        "paymentexchangerate_targetcurrencycode"
        "paymentexchangerate_calculationrate"

        "paymentalternativeexchangerate_sourcecurrencycode"
        "paymentalternativeexchangerate_date"
        "column_break_alternatif_odeme_doviz_kuru"
        "paymentalternativeexchangerate_targetcurrencycode"
        "paymentalternativeexchangerate_calculationrate"
