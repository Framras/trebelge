import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
from trebelge.TRUBLCommonElementsStrategy.TRUBLInvoiceLine import TRUBLInvoiceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLMonetaryTotal import TRUBLMonetaryTotal
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentTerms import TRUBLPaymentTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal
from trebelge.TRUBLInvoiceBuilder.TRUBLBuilder import TRUBLBuilder


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
        self._namespaces = dict([node for _, node in ET.iterparse(filepath, events=['start-ns'])])
        self._cac_ns = str('{' + self._namespaces.get('cac') + '}')
        self._cbc_ns = str('{' + self._namespaces.get('cbc') + '}')
        self._product = None
        self.root: Element = ET.parse(filepath).getroot()
        self.reset()

    def reset(self) -> None:
        uuid_ = self.root.find('./' + self._cbc_ns + 'UUID').text
        if len(frappe.get_all(self._frappeDoctype, filters={'uuid': uuid_})) == 0:
            invoice_: Document = frappe.new_doc(self._frappeDoctype)
            invoice_.uuid = uuid_
            invoice_.insert()
        invoice: Document = frappe.get_doc(self._frappeDoctype, uuid_)
        self._product = invoice

    @property
    def product(self) -> Document:
        product: Document = self._product.save()
        self.reset()
        return product

    def build_ublversionid(self) -> None:
        # ['UBLVersionID'] = ('cbc', 'ublversionid', 'Zorunlu (1)')
        self._product.ublversionid = self.root.find('./' + self._cbc_ns + 'UBLVersionID').text

    def build_customizationid(self) -> None:
        # ['CustomizationID'] = ('cbc', 'customizationid', 'Zorunlu (1)')
        self._product.customizationid = self.root.find('./' + self._cbc_ns + 'CustomizationID').text

    def build_profileid(self) -> None:
        # ['ProfileID'] = ('cbc', 'profileid', 'Zorunlu (1)')
        self._product.profileid = self.root.find('./' + self._cbc_ns + 'ProfileID').text

    def build_id(self) -> None:
        # ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        self._product.id = self.root.find('./' + self._cbc_ns + 'ID').text

    def build_copyindicator(self) -> None:
        # ['CopyIndicator'] = ('cbc', 'copyindicator', 'Zorunlu (1)')
        self._product.copyindicator = self.root.find('./' + self._cbc_ns + 'CopyIndicator').text

    def build_issuedate(self) -> None:
        # ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu (1)')
        self._product.issuedate = self.root.find('./' + self._cbc_ns + 'IssueDate').text

    def build_issuetime(self) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = self.root.find('./' + self._cbc_ns + 'IssueTime')
        if issuetime_:
            self._product.issuetime = issuetime_.text

    def build_invoicetypecode(self) -> None:
        # ['InvoiceTypeCode'] = ('cbc', 'invoicetypecode', 'Zorunlu (1)')
        self._product.invoicetypecode = self.root.find('./' + self._cbc_ns + 'InvoiceTypeCode').text

    def build_despatchadvicetypecode(self) -> None:
        # ['DespatchAdviceTypeCode'] = ('cbc', 'despatchadvicetypecode', 'Zorunlu (1)')
        pass

    def build_note(self) -> None:
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...n)', 'note')
        notes_: list = self.root.findall('./' + self._cbc_ns + 'Note')
        if notes_:
            note: list = []
            for note_ in notes_:
                note.append(TRUBLNote().process_element(note_,
                                                        self._cbc_ns,
                                                        self._cbc_ns).name)
            self._product.note = note

    def build_documentcurrencycode(self) -> None:
        # ['DocumentCurrencyCode'] = ('cbc', 'documentcurrencycode', 'Zorunlu (1)')
        self._product.documentcurrencycode = self.root.find('./' + self._cbc_ns + 'DocumentCurrencyCode').text

    def build_taxcurrencycode(self) -> None:
        # ['TaxCurrencyCode'] = ('cbc', 'taxcurrencycode', 'Seçimli (0...1)')
        taxcurrencycode_: Element = self.root.find('./' + self._cbc_ns + 'TaxCurrencyCode')
        if taxcurrencycode_:
            self._product.taxcurrencycode = taxcurrencycode_.text

    def build_pricingcurrencycode(self) -> None:
        # ['PricingCurrencyCode'] = ('cbc', 'pricingcurrencycode', 'Seçimli (0...1)')
        pricingcurrencycode_: Element = self.root.find('./' + self._cbc_ns + 'PricingCurrencyCode')
        if pricingcurrencycode_:
            self._product.pricingcurrencycode = pricingcurrencycode_.text

    def build_paymentcurrencycode(self) -> None:
        # ['PaymentCurrencyCode'] = ('cbc', 'paymentcurrencycode', 'Seçimli (0...1)')
        paymentcurrencycode_: Element = self.root.find('./' + self._cbc_ns + 'PaymentCurrencyCode')
        if paymentcurrencycode_:
            self._product.paymentcurrencycode = paymentcurrencycode_.text

    def build_paymentalternativecurrencycode(self) -> None:
        # ['PaymentAlternativeCurrencyCode'] = ('cbc', 'paymentalternativecurrencycode', 'Seçimli (0...1)')
        paymentalternativecurrencycode_: Element = self.root.find(
            './' + self._cbc_ns + 'PaymentAlternativeCurrencyCode')
        if paymentalternativecurrencycode_:
            self._product.paymentalternativecurrencycode = paymentalternativecurrencycode_.text

    def build_accountingcost(self) -> None:
        # ['AccountingCost'] = ('cbc', 'accountingcost', 'Seçimli (0...1)')
        accountingcost_: Element = self.root.find('./' + self._cbc_ns + 'AccountingCost')
        if accountingcost_:
            self._product.accountingcost = accountingcost_.text

    def build_linecountnumeric(self) -> None:
        # ['LineCountNumeric'] = ('cbc', 'linecountnumeric', 'Zorunlu (1)')
        self._product.linecountnumeric = self.root.find('./' + self._cbc_ns + 'LineCountNumeric').text

    def build_invoiceperiod(self) -> None:
        # ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)', 'invoiceperiod')
        invoiceperiod_: Element = self.root.find('./' + self._cac_ns + 'InvoicePeriod')
        if invoiceperiod_:
            self._product.invoiceperiod = TRUBLPeriod().process_element(invoiceperiod_,
                                                                        self._cbc_ns,
                                                                        self._cbc_ns)

    def build_orderreference(self) -> None:
        # ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...1)', 'orderreference')
        orderreference_: Element = self.root.find('./' + self._cac_ns + 'OrderReference')
        if orderreference_:
            self._product.orderreference = TRUBLOrderReference().process_element(orderreference_,
                                                                                 self._cbc_ns,
                                                                                 self._cbc_ns)

    def build_billingreference(self) -> None:
        # ['BillingReference'] = ('cac', BillingReference(), 'Seçimli (0...n)', 'billingreference')
        pass

    def build_despatchdocumentreference(self) -> None:
        # ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'despatchdocumentreference')
        pass

    def build_receiptdocumentreference(self) -> None:
        # ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'receiptdocumentreference')
        pass

    def build_originatordocumentreference(self) -> None:
        # ['OriginatorDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'originatordocumentreference')
        pass

    def build_contractdocumentreference(self) -> None:
        # ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'contractdocumentreference')
        pass

    def build_additionaldocumentreference(self) -> None:
        # ['AdditionalDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'additionaldocumentreference')
        pass

    def build_accountingsupplierparty(self) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        pass

    def build_despatchsupplierparty(self) -> None:
        # ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        pass

    def build_accountingcustomerparty(self) -> None:
        # ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        pass

    def build_deliverycustomerparty(self) -> None:
        # ['DeliveryCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'deliverycustomerparty')
        pass

    def build_buyercustomerparty(self) -> None:
        # ['BuyerCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'buyercustomerparty')
        pass

    def build_sellersupplierparty(self) -> None:
        # ['SellerSupplierParty'] = ('cac', SupplierParty(), 'Seçimli (0..1)', 'sellersupplierparty')
        pass

    def build_originatorcustomerparty(self) -> None:
        # ['OriginatorCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'originatorcustomerparty')
        pass

    def build_taxrepresentativeparty(self) -> None:
        # ['TaxRepresentativeParty'] = ('cac', Party(), 'Seçimli (0..1)', 'taxrepresentativeparty')
        pass

    def build_delivery(self) -> None:
        # ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)', 'delivery')
        pass

    def build_shipment(self) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Seçimli (0...n)', 'shipment')
        pass

    def build_paymentmeans(self) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)')
        pass

    def build_paymentterms(self) -> None:
        # ['PaymentTerms'] = ('cac', PaymentTerms(), 'Seçimli (0..1)')
        paymentterms_: Element = self.root.find('./' + self._cac_ns + 'PaymentTerms')
        if paymentterms_:
            self._product.paymentterms = TRUBLPaymentTerms().process_element(paymentterms_,
                                                                             self._cbc_ns,
                                                                             self._cbc_ns)

    def build_allowancecharge(self) -> None:
        # ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)', 'allowancecharge')
        pass

    def build_taxexchangerate(self) -> None:
        # ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'taxexchangerate')
        taxexchangerate_: Element = self.root.find('./' + self._cac_ns + 'TaxExchangeRate')
        if taxexchangerate_:
            self._product.taxexchangerate = TRUBLExchangeRate().process_element(taxexchangerate_,
                                                                                self._cbc_ns,
                                                                                self._cbc_ns)

    def build_pricingexchangerate(self) -> None:
        # ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'pricingexchangerate')
        pricingexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PricingExchangeRate')
        if pricingexchangerate_:
            self._product.pricingexchangerate = TRUBLExchangeRate().process_element(pricingexchangerate_,
                                                                                    self._cbc_ns,
                                                                                    self._cbc_ns)

    def build_paymentexchangerate(self) -> None:
        # ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentexchangerate')
        paymentexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PaymentExchangeRate')
        if paymentexchangerate_:
            self._product.paymentexchangerate = TRUBLExchangeRate().process_element(paymentexchangerate_,
                                                                                    self._cbc_ns,
                                                                                    self._cbc_ns)

    def build_paymentalternativeexchangerate(self) -> None:
        # ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)',
        # 'paymentalternativeexchangerate')
        paymentalternativeexchangerate_: Element = self.root.find(
            './' + self._cac_ns + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate_:
            self._product.paymentalternativeexchangerate = TRUBLExchangeRate().process_element(
                paymentalternativeexchangerate_,
                self._cbc_ns,
                self._cbc_ns)

    def build_taxtotal(self) -> None:
        # ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)', 'taxtotal')
        taxtotals_: list = self.root.findall('./' + self._cac_ns + 'TaxTotal')
        taxtotal: list = []
        for taxtotal_ in taxtotals_:
            taxtotal.append(TRUBLTaxTotal().process_element(taxtotal_,
                                                            self._cbc_ns,
                                                            self._cbc_ns))
        self._product.taxtotal = taxtotal

    def build_withholdingtaxtotal(self) -> None:
        # ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'withholdingtaxtotal')
        withholdingtaxtotals_: list = self.root.findall('./' + self._cac_ns + 'WithholdingTaxTotal')
        if withholdingtaxtotals_:
            withholdingtaxtotal: list = []
            for withholdingtaxtotal_ in withholdingtaxtotals_:
                withholdingtaxtotal.append(TRUBLTaxTotal().process_element(withholdingtaxtotal_,
                                                                           self._cbc_ns,
                                                                           self._cbc_ns))
            self._product.withholdingtaxtotal = withholdingtaxtotal

    def build_legalmonetarytotal(self) -> None:
        # ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        legalmonetarytotal_: Element = self.root.find('./' + self._cac_ns + 'LegalMonetaryTotal')
        self._product.legalmonetarytotal = TRUBLMonetaryTotal().process_element(legalmonetarytotal_,
                                                                                self._cbc_ns,
                                                                                self._cbc_ns)

    def build_invoiceline(self) -> None:
        # ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)', 'invoiceline')
        invoicelines_: list = self.root.findall('./' + self._cac_ns + 'InvoiceLine')
        invoiceline: list = []
        for invoiceline_ in invoicelines_:
            invoiceline.append(TRUBLInvoiceLine().process_element(invoiceline_,
                                                                  self._cbc_ns,
                                                                  self._cbc_ns))
        self._product.invoiceline = invoiceline

    def build_despatchline(self) -> None:
        # ['DespatchLine'] = ('cac', DespatchLine(), 'Zorunlu (1...n)', 'despatchline')
        pass
