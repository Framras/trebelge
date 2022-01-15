import time
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReference import TRUBLBillingReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLMonetaryTotal import TRUBLMonetaryTotal
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentMeans import TRUBLPaymentMeans
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentTerms import TRUBLPaymentTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal


class TRUBLInvoiceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """
    _frappeDoctype: str = 'UBL TR Invoice'

    def __init__(self, filepath: str) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.filepath = filepath
        self._cbc_ns = None
        self._cac_ns = None
        self.root = None
        self._product = None

    def reset(self) -> None:
        _namespaces = dict([node for _, node in ET.iterparse(self.filepath, events=['start-ns'])])
        self._cac_ns = str('{' + _namespaces.get('cac') + '}')
        self._cbc_ns = str('{' + _namespaces.get('cbc') + '}')
        root_: Element = ET.parse(self.filepath).getroot()
        uuid_ = root_.find('./' + self._cbc_ns + 'UUID').text
        if len(frappe.get_all(self._frappeDoctype, filters={'uuid': uuid_})) == 0:
            invoice_ = frappe.new_doc(self._frappeDoctype)
            invoice_.uuid = uuid_
            invoice_.ublversionid = root_.find('./' + self._cbc_ns + 'UBLVersionID').text
            invoice_.customizationid = root_.find('./' + self._cbc_ns + 'CustomizationID').text
            invoice_.profileid = root_.find('./' + self._cbc_ns + 'ProfileID').text
            invoice_.id = root_.find('./' + self._cbc_ns + 'ID').text
            invoice_.copyindicator = root_.find('./' + self._cbc_ns + 'CopyIndicator').text
            invoice_.issuedate = root_.find('./' + self._cbc_ns + 'IssueDate').text
            invoice_.invoicetypecode = root_.find('./' + self._cbc_ns + 'InvoiceTypeCode').text
            invoice_.documentcurrencycode = root_.find('./' + self._cbc_ns + 'DocumentCurrencyCode').text
            taxcurrencycode_: Element = root_.find('./' + self._cbc_ns + 'TaxCurrencyCode')
            if taxcurrencycode_ is not None:
                invoice_.taxcurrencycode = taxcurrencycode_.text
            pricingcurrencycode_: Element = root_.find('./' + self._cbc_ns + 'PricingCurrencyCode')
            if pricingcurrencycode_ is not None:
                invoice_.pricingcurrencycode = pricingcurrencycode_.text
            paymentcurrencycode_: Element = root_.find('./' + self._cbc_ns + 'PaymentCurrencyCode')
            if paymentcurrencycode_ is not None:
                invoice_.paymentcurrencycode = paymentcurrencycode_.text
            paymentalternativecurrencycode_: Element = root_.find(
                './' + self._cbc_ns + 'PaymentAlternativeCurrencyCode')
            if paymentalternativecurrencycode_ is not None:
                invoice_.paymentalternativecurrencycode = paymentalternativecurrencycode_.text
            accountingcost_: Element = root_.find('./' + self._cbc_ns + 'AccountingCost')
            if accountingcost_ is not None:
                invoice_.accountingcost = accountingcost_.text
            invoice_.linecountnumeric = root_.find('./' + self._cbc_ns + 'LineCountNumeric').text
            invoice_.insert()
        self.root = root_
        self._product = frappe.get_doc(self._frappeDoctype, uuid_)

    def build_issuetime(self) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = self.root.find('./' + self._cbc_ns + 'IssueTime')
        if issuetime_ is not None:
            try:
                time.strptime(issuetime_.text, '%H:%M:%S')
                self._product.issuetime = issuetime_.text
            except ValueError:
                pass
        else:
            self._product.issuetime = ""

    def build_note(self) -> None:
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...n)', 'note')
        notes_: list = self.root.findall('./' + self._cbc_ns + 'Note')
        if len(notes_) != 0:
            note = list()
            for note_ in notes_:
                tmp = TRUBLNote().process_element(note_, self._cbc_ns, self._cbc_ns)
                if tmp is not None:
                    note.append(tmp)
            self._product.note = note

    def build_invoiceperiod(self) -> None:
        # ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)', 'invoiceperiod')
        invoiceperiod_: Element = self.root.find('./' + self._cac_ns + 'InvoicePeriod')
        if invoiceperiod_ is not None:
            tmp = TRUBLPeriod().process_element(invoiceperiod_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.invoiceperiod = tmp.name

    def build_orderreference(self) -> None:
        # ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...1)', 'orderreference')
        orderreference_: Element = self.root.find('./' + self._cac_ns + 'OrderReference')
        if orderreference_ is not None:
            tmp = TRUBLOrderReference().process_element(orderreference_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.orderreference = tmp.name

    def build_billingreference(self) -> None:
        # ['BillingReference'] = ('cac', BillingReference(), 'Seçimli (0...n)', 'billingreference')
        billingreferences_: list = self.root.findall('./' + self._cac_ns + 'BillingReference')
        if len(billingreferences_) != 0:
            billingreference = list()
            for billingreference_ in billingreferences_:
                tmp = TRUBLBillingReference().process_element(billingreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    billingreference.append(tmp)
            self._product.billingreference = billingreference

    def build_despatchdocumentreference(self) -> None:
        # ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'despatchdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'DespatchDocumentReference')
        if len(documentreferences_) != 0:
            documentreference = list()
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    documentreference.append(tmp)
            self._product.despatchdocumentreference = documentreference

    def build_receiptdocumentreference(self) -> None:
        # ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'receiptdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ReceiptDocumentReference')
        if len(documentreferences_) != 0:
            documentreference = list()
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    documentreference.append(tmp)
            self._product.receiptdocumentreference = documentreference

    def build_originatordocumentreference(self) -> None:
        # ['OriginatorDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'originatordocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'OriginatorDocumentReference')
        if len(documentreferences_) != 0:
            documentreference = list()
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    documentreference.append(tmp)
            self._product.originatordocumentreference = documentreference

    def build_contractdocumentreference(self) -> None:
        # ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'contractdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ContractDocumentReference')
        if len(documentreferences_) != 0:
            documentreference = list()
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    documentreference.append(tmp)
            self._product.contractdocumentreference = documentreference

    def build_additionaldocumentreference(self) -> None:
        # ['AdditionalDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'additionaldocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'AdditionalDocumentReference')
        if len(documentreferences_) != 0:
            documentreference = list()
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    documentreference.append(tmp)
            self._product.additionaldocumentreference = documentreference

    def build_accountingsupplierparty(self) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        accountingsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'AccountingSupplierParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = accountingsupplierparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.accountingsupplierparty = party.name
        # ['DespatchContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'despatchcontact')
        despatchcontact_: Element = accountingsupplierparty_.find('./' + self._cac_ns + 'DespatchContact')
        if despatchcontact_ is not None:
            contact = TRUBLContact().process_element(despatchcontact_, self._cbc_ns, self._cac_ns)
            if contact is not None:
                self._product.accountingsuppliercontact = contact.name

    def build_despatchsupplierparty(self) -> None:
        # ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        pass

    def build_accountingcustomerparty(self) -> None:
        # ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        accountingcustomerparty_: Element = self.root.find('./' + self._cac_ns + 'AccountingCustomerParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = accountingcustomerparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.accountingcustomerparty = party.name
        # ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
        deliverycontact_: Element = accountingcustomerparty_.find('./' + self._cac_ns + 'DeliveryContact')
        if deliverycontact_ is not None:
            contact = TRUBLContact().process_element(deliverycontact_, self._cbc_ns, self._cac_ns)
            if contact is not None:
                self._product.accountingcustomercontact = contact.name

    def build_deliverycustomerparty(self) -> None:
        # ['DeliveryCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'deliverycustomerparty')
        pass

    def build_buyercustomerparty(self) -> None:
        # ['BuyerCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'buyercustomerparty')
        buyercustomerparty_: Element = self.root.find('./' + self._cac_ns + 'BuyerCustomerParty')
        if buyercustomerparty_ is not None:
            # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
            party_: Element = buyercustomerparty_.find('./' + self._cac_ns + 'Party')
            party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
            self._product.buyercustomerparty = party.name
            # ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
            deliverycontact_: Element = buyercustomerparty_.find('./' + self._cac_ns + 'DeliveryContact')
            if deliverycontact_ is not None:
                contact = TRUBLContact().process_element(deliverycontact_, self._cbc_ns, self._cac_ns)
                if contact is not None:
                    self._product.buyercustomercontact = contact.name

    def build_sellersupplierparty(self) -> None:
        # ['SellerSupplierParty'] = ('cac', SupplierParty(), 'Seçimli (0..1)', 'sellersupplierparty')
        sellersupplierparty_: Element = self.root.find('./' + self._cac_ns + 'SellerSupplierParty')
        if sellersupplierparty_ is not None:
            # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
            party_: Element = sellersupplierparty_.find('./' + self._cac_ns + 'Party')
            party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
            self._product.sellersupplierparty = party.name
            # ['DespatchContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'despatchcontact')
            despatchcontact_: Element = sellersupplierparty_.find('./' + self._cac_ns + 'DespatchContact')
            if despatchcontact_ is not None:
                contact = TRUBLContact().process_element(despatchcontact_, self._cbc_ns, self._cac_ns)
                if contact is not None:
                    self._product.sellersuppliercontact = contact.name

    def build_originatorcustomerparty(self) -> None:
        # ['OriginatorCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'originatorcustomerparty')
        pass

    def build_taxrepresentativeparty(self) -> None:
        # ['TaxRepresentativeParty'] = ('cac', Party(), 'Seçimli (0..1)', 'taxrepresentativeparty')
        taxrepresentativeparty_: Element = self.root.find('./' + self._cac_ns + 'TaxRepresentativeParty')
        if taxrepresentativeparty_ is not None:
            tmp = TRUBLParty().process_element(taxrepresentativeparty_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.taxrepresentativeparty = tmp.name

    def build_delivery(self) -> None:
        # ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)', 'delivery')
        deliveries_: list = self.root.findall('./' + self._cac_ns + 'Delivery')
        if len(deliveries_) != 0:
            delivery = list()
            for delivery_ in deliveries_:
                tmp = TRUBLDelivery().process_element(delivery_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    delivery.append(tmp)
            self._product.delivery = delivery

    def build_shipment(self) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Seçimli (0...n)', 'shipment')
        pass

    def build_paymentmeans(self) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)', 'paymentmeans')
        paymentmeans_: list = self.root.findall('./' + self._cac_ns + 'PaymentMeans')
        if len(paymentmeans_) != 0:
            paymentmeans = list()
            for payment_means_ in paymentmeans_:
                tmp = TRUBLPaymentMeans().process_element(payment_means_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    paymentmeans.append(tmp)
            self._product.paymentmeans = paymentmeans

    def build_paymentterms(self) -> None:
        # ['PaymentTerms'] = ('cac', PaymentTerms(), 'Seçimli (0..1)')
        paymentterms_: Element = self.root.find('./' + self._cac_ns + 'PaymentTerms')
        if paymentterms_ is not None:
            tmp = TRUBLPaymentTerms().process_element(paymentterms_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.paymentterms = tmp.name

    def build_allowancecharge(self) -> None:
        # ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)', 'allowancecharge')
        allowancecharges_: list = self.root.findall('./' + self._cac_ns + 'AllowanceCharge')
        if len(allowancecharges_) != 0:
            allowancecharge = list()
            for allowancecharge_ in allowancecharges_:
                tmp = TRUBLAllowanceCharge().process_element(allowancecharge_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    allowancecharge.append(tmp)
            self._product.allowancecharge = allowancecharge

    def build_taxexchangerate(self) -> None:
        # ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'taxexchangerate')
        taxexchangerate_: Element = self.root.find('./' + self._cac_ns + 'TaxExchangeRate')
        if taxexchangerate_ is not None:
            tmp = TRUBLExchangeRate().process_element(taxexchangerate_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.taxexchangerate = tmp.name

    def build_pricingexchangerate(self) -> None:
        # ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'pricingexchangerate')
        pricingexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PricingExchangeRate')
        if pricingexchangerate_ is not None:
            tmp = TRUBLExchangeRate().process_element(pricingexchangerate_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.pricingexchangerate = tmp.name

    def build_paymentexchangerate(self) -> None:
        # ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentexchangerate')
        paymentexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PaymentExchangeRate')
        if paymentexchangerate_ is not None:
            tmp = TRUBLExchangeRate().process_element(paymentexchangerate_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.paymentexchangerate = tmp.name

    def build_paymentalternativeexchangerate(self) -> None:
        # ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)',
        # 'paymentalternativeexchangerate')
        paymentalternativeexchangerate_: Element = self.root.find(
            './' + self._cac_ns + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate_ is not None:
            tmp = TRUBLExchangeRate().process_element(paymentalternativeexchangerate_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.paymentalternativeexchangerate = tmp.name

    def build_taxtotal(self) -> None:
        # ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)', 'taxtotal')
        taxtotals_: list = self.root.findall('./' + self._cac_ns + 'TaxTotal')
        taxtotal = list()
        for taxtotal_ in taxtotals_:
            tmp = TRUBLTaxTotal().process_element(taxtotal_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                taxtotal.append(tmp)
        self._product.taxtotal = taxtotal

    def build_withholdingtaxtotal(self) -> None:
        # ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'withholdingtaxtotal')
        withholdingtaxtotals_: list = self.root.findall('./' + self._cac_ns + 'WithholdingTaxTotal')
        if len(withholdingtaxtotals_) != 0:
            withholdingtaxtotal = list()
            for withholdingtaxtotal_ in withholdingtaxtotals_:
                tmp = TRUBLTaxTotal().process_element(withholdingtaxtotal_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    withholdingtaxtotal.append(tmp)
            self._product.withholdingtaxtotal = withholdingtaxtotal

    def build_legalmonetarytotal(self) -> None:
        # ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        legalmonetarytotal_: Element = self.root.find('./' + self._cac_ns + 'LegalMonetaryTotal')
        self._product.legalmonetarytotal = TRUBLMonetaryTotal().process_element(legalmonetarytotal_,
                                                                                self._cbc_ns,
                                                                                self._cac_ns).name

    def build_invoiceline(self) -> None:
        invoicelines = list()
        # ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)', 'invoiceline')
        invoicelines_: list = self.root.findall('./' + self._cac_ns + 'InvoiceLine')
        for invoiceline_ in invoicelines_:
            tmp = self._process_invoiceline(invoiceline_)
            if tmp is not None:
                invoicelines.append(tmp)
        for invoiceline in invoicelines:
            doc_append = self._product.append("invoiceline", invoiceline)
            self._product.save()

    def _process_invoiceline(self, element: Element):
        frappedoc = dict()
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        # ['InvoicedQuantity'] = ('cbc', '', 'Zorunlu (1)')
        # ['LineExtensionAmount'] = ('cbc', '', 'Zorunlu (1)')
        id_: Element = element.find('./' + self._cbc_ns + 'ID')
        invoicedquantity: Element = element.find('./' + self._cbc_ns + 'InvoicedQuantity')
        lineextensionamount: Element = element.find('./' + self._cbc_ns + 'LineExtensionAmount')
        if id_ is None or id_.text is None:
            return None
        frappedoc['id'] = id_.text
        if invoicedquantity is None or invoicedquantity.text is None:
            return None
        frappedoc['invoicedquantity'] = invoicedquantity.text
        frappedoc['invoicedquantityunitcode'] = invoicedquantity.attrib.get('unitCode')
        if lineextensionamount is None or lineextensionamount.text is None:
            return None
        frappedoc['lineextensionamount'] = lineextensionamount.text
        frappedoc['lineextensionamountcurrencyid'] = lineextensionamount.attrib.get('currencyID')
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        note_: Element = element.find('./' + self._cbc_ns + 'Note')
        if note_ is not None and note_.text is not None:
            frappedoc['note'] = note_.text
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        item_: Element = element.find('./' + self._cac_ns + 'Item')
        tmp = TRUBLItem().process_element(item_, self._cbc_ns, self._cac_ns)
        if tmp is None:
            return None
        frappedoc['item'] = tmp.name
        # ['Price'] = ('cac', 'Price', 'Zorunlu (1)')
        price_: Element = element.find('./' + self._cac_ns + 'Price')
        # self._mapping['PriceAmount'] = ('cbc', '', 'Zorunlu(1)')
        priceamount = price_.find('./' + self._cbc_ns + 'PriceAmount')
        if priceamount is None or priceamount.text is None:
            return None
        frappedoc['priceamount'] = priceamount.text
        frappedoc['priceamountcurrencyid'] = priceamount.attrib.get('currencyID')
        # ['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)')
        taxtotal_: Element = element.find('./' + self._cac_ns + 'TaxTotal')
        if taxtotal_ is not None:
            tmp = TRUBLTaxTotal().process_element(taxtotal_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                frappedoc['taxtotal'] = tmp.name
        orderlinereference = list()
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + self._cac_ns + 'OrderLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLOrderLineReference().process_element(tagelement_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    orderlinereference.append(tmp)
            if len(orderlinereference) != 0:
                frappedoc['orderlinereference'] = orderlinereference
        despatchlinereference = list()
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + self._cac_ns + 'DespatchLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    despatchlinereference.append(tmp)
            if len(despatchlinereference) != 0:
                frappedoc['despatchlinereference'] = despatchlinereference
        receiptlinereference = list()
        # ['ReceiptLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + self._cac_ns + 'ReceiptLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    receiptlinereference.append(tmp)
            if len(receiptlinereference) != 0:
                frappedoc['receiptlinereference'] = receiptlinereference
        delivery = list()
        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + self._cac_ns + 'Delivery')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLDelivery().process_element(tagelement_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    delivery.append(tmp)
            if len(delivery) != 0:
                frappedoc['delivery'] = delivery
        withholdingtaxtotal = list()
        # ['WithholdingTaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + self._cac_ns + 'WithholdingTaxTotal')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLTaxTotal().process_element(tagelement_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    withholdingtaxtotal.append(tmp)
            if len(withholdingtaxtotal) != 0:
                frappedoc['withholdingtaxtotal'] = withholdingtaxtotal
        allowancecharge = list()
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + self._cac_ns + 'AllowanceCharge')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLAllowanceCharge().process_element(tagelement_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    allowancecharge.append(tmp)
            if len(allowancecharge) != 0:
                frappedoc['allowancecharge'] = allowancecharge
        subinvoiceline = list()
        # ['SubInvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + self._cac_ns + 'SubInvoiceLine')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLInvoiceLine().process_element(tagelement_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    subinvoiceline.append(tmp)
            if len(subinvoiceline) != 0:
                frappedoc['subinvoiceline'] = subinvoiceline
        return frappedoc

    def build_despatchline(self) -> None:
        # ['DespatchLine'] = ('cac', DespatchLine(), 'Zorunlu (1...n)', 'despatchline')
        pass

    def get_document(self) -> None:
        product = self._product.save()
