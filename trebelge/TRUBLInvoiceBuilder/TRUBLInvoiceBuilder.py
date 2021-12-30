import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReference import TRUBLBillingReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLCustomerParty import TRUBLCustomerParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLDespatchLine import TRUBLDespatchLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
from trebelge.TRUBLCommonElementsStrategy.TRUBLInvoiceLine import TRUBLInvoiceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLMonetaryTotal import TRUBLMonetaryTotal
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentMeans import TRUBLPaymentMeans
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentTerms import TRUBLPaymentTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment
from trebelge.TRUBLCommonElementsStrategy.TRUBLSupplierParty import TRUBLSupplierParty
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
        self.filepath = filepath
        self._cbc_ns = None
        self._cac_ns = None
        self.root = None
        self._product = None

    def reset(self) -> None:
        _namespaces = dict([node for _, node in ET.iterparse(self.filepath, events=['start-ns'])])
        self._cac_ns = str('{' + _namespaces.get('cac') + '}')
        self._cbc_ns = str('{' + _namespaces.get('cbc') + '}')
        self.root: Element = ET.parse(self.filepath).getroot()
        uuid_ = self.root.find('./' + self._cbc_ns + 'UUID').text
        if len(frappe.get_all(self._frappeDoctype, filters={'uuid': uuid_})) == 0:
            invoice_ = frappe.new_doc(self._frappeDoctype)
            invoice_.uuid = uuid_
            invoice_.insert()
        invoice = frappe.get_doc(self._frappeDoctype, uuid_)
        self._product = invoice

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
        if len(notes_) != 0:
            note: list = []
            for note_ in notes_:
                note.append(TRUBLNote().process_element(note_,
                                                        self._cbc_ns,
                                                        self._cbc_ns))
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
                                                                        self._cac_ns).name

    def build_orderreference(self) -> None:
        # ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...1)', 'orderreference')
        orderreference_: Element = self.root.find('./' + self._cac_ns + 'OrderReference')
        if orderreference_:
            self._product.orderreference = TRUBLOrderReference().process_element(orderreference_,
                                                                                 self._cbc_ns,
                                                                                 self._cac_ns).name

    def build_billingreference(self) -> None:
        # ['BillingReference'] = ('cac', BillingReference(), 'Seçimli (0...n)', 'billingreference')
        billingreferences_: list = self.root.findall('./' + self._cac_ns + 'BillingReference')
        if len(billingreferences_) != 0:
            billingreference: list = []
            for billingreference_ in billingreferences_:
                billingreference.append(TRUBLBillingReference().process_element(billingreference_,
                                                                                self._cbc_ns,
                                                                                self._cac_ns))
            self._product.billingreference = billingreference

    def build_despatchdocumentreference(self) -> None:
        # ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'despatchdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'DespatchDocumentReference')
        if len(documentreferences_) != 0:
            documentreference: list = []
            for documentreference_ in documentreferences_:
                documentreference.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                  self._cbc_ns,
                                                                                  self._cac_ns))
            self._product.despatchdocumentreference = documentreference

    def build_receiptdocumentreference(self) -> None:
        # ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'receiptdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ReceiptDocumentReference')
        if len(documentreferences_) != 0:
            documentreference: list = []
            for documentreference_ in documentreferences_:
                documentreference.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                  self._cbc_ns,
                                                                                  self._cac_ns))
            self._product.receiptdocumentreference = documentreference

    def build_originatordocumentreference(self) -> None:
        # ['OriginatorDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'originatordocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'OriginatorDocumentReference')
        if len(documentreferences_) != 0:
            documentreference: list = []
            for documentreference_ in documentreferences_:
                documentreference.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                  self._cbc_ns,
                                                                                  self._cac_ns))
            self._product.originatordocumentreference = documentreference

    def build_contractdocumentreference(self) -> None:
        # ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'contractdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ContractDocumentReference')
        if len(documentreferences_) != 0:
            documentreference: list = []
            for documentreference_ in documentreferences_:
                documentreference.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                  self._cbc_ns,
                                                                                  self._cac_ns))
            self._product.contractdocumentreference = documentreference

    def build_additionaldocumentreference(self) -> None:
        # ['AdditionalDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'additionaldocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'AdditionalDocumentReference')
        if len(documentreferences_) != 0:
            documentreference: list = []
            for documentreference_ in documentreferences_:
                documentreference.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                  self._cbc_ns,
                                                                                  self._cac_ns))
            self._product.additionaldocumentreference = documentreference

    def build_accountingsupplierparty(self) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        accountingsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'AccountingSupplierParty')
        self._product.accountingsupplierparty = TRUBLSupplierParty().process_element(accountingsupplierparty_,
                                                                                     self._cbc_ns,
                                                                                     self._cac_ns).name

    def build_despatchsupplierparty(self) -> None:
        # ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        despatchsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'DespatchSupplierParty')
        self._product.despatchsupplierparty = TRUBLSupplierParty().process_element(despatchsupplierparty_,
                                                                                   self._cbc_ns,
                                                                                   self._cac_ns).name

    def build_accountingcustomerparty(self) -> None:
        # ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        accountingcustomerparty_: Element = self.root.find('./' + self._cac_ns + 'AccountingCustomerParty')
        self._product.accountingcustomerparty = TRUBLCustomerParty().process_element(accountingcustomerparty_,
                                                                                     self._cbc_ns,
                                                                                     self._cac_ns).name

    def build_deliverycustomerparty(self) -> None:
        # ['DeliveryCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'deliverycustomerparty')
        deliverycustomerparty_: Element = self.root.find('./' + self._cac_ns + 'DeliveryCustomerParty')
        self._product.deliverycustomerparty = TRUBLCustomerParty().process_element(deliverycustomerparty_,
                                                                                   self._cbc_ns,
                                                                                   self._cac_ns).name

    def build_buyercustomerparty(self) -> None:
        # ['BuyerCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'buyercustomerparty')
        buyercustomerparty_: Element = self.root.find('./' + self._cac_ns + 'BuyerCustomerParty')
        if buyercustomerparty_:
            self._product.buyercustomerparty = TRUBLCustomerParty().process_element(buyercustomerparty_,
                                                                                    self._cbc_ns,
                                                                                    self._cac_ns).name

    def build_sellersupplierparty(self) -> None:
        # ['SellerSupplierParty'] = ('cac', SupplierParty(), 'Seçimli (0..1)', 'sellersupplierparty')
        sellersupplierparty_: Element = self.root.find('./' + self._cac_ns + 'SellerSupplierParty')
        if sellersupplierparty_:
            self._product.sellersupplierparty = TRUBLSupplierParty().process_element(sellersupplierparty_,
                                                                                     self._cbc_ns,
                                                                                     self._cac_ns).name

    def build_originatorcustomerparty(self) -> None:
        # ['OriginatorCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'originatorcustomerparty')
        originatorcustomerparty_: Element = self.root.find('./' + self._cac_ns + 'OriginatorCustomerParty')
        if originatorcustomerparty_:
            self._product.originatorcustomerparty = TRUBLCustomerParty().process_element(originatorcustomerparty_,
                                                                                         self._cbc_ns,
                                                                                         self._cac_ns).name

    def build_taxrepresentativeparty(self) -> None:
        # ['TaxRepresentativeParty'] = ('cac', Party(), 'Seçimli (0..1)', 'taxrepresentativeparty')
        taxrepresentativeparty_: Element = self.root.find('./' + self._cac_ns + 'TaxRepresentativeParty')
        if taxrepresentativeparty_:
            self._product.taxrepresentativeparty = TRUBLParty().process_element(taxrepresentativeparty_,
                                                                                self._cbc_ns,
                                                                                self._cac_ns).name

    def build_delivery(self) -> None:
        # ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)', 'delivery')
        deliveries_: list = self.root.findall('./' + self._cac_ns + 'Delivery')
        if len(deliveries_) != 0:
            delivery: list = []
            for delivery_ in deliveries_:
                delivery.append(TRUBLDelivery().process_element(delivery_,
                                                                self._cbc_ns,
                                                                self._cac_ns))
            self._product.delivery = delivery

    def build_shipment(self) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Seçimli (0...n)', 'shipment')
        shipments_: list = self.root.findall('./' + self._cac_ns + 'Shipment')
        if len(shipments_) != 0:
            shipment: list = []
            for shipment_ in shipments_:
                shipment.append(TRUBLShipment().process_element(shipment_,
                                                                self._cbc_ns,
                                                                self._cac_ns))
            self._product.shipment = shipment

    def build_paymentmeans(self) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)', 'paymentmeans')
        paymentmeans_: list = self.root.findall('./' + self._cac_ns + 'PaymentMeans')
        if len(paymentmeans_) != 0:
            paymentmeans: list = []
            for payment_means_ in paymentmeans_:
                paymentmeans.append(TRUBLPaymentMeans().process_element(payment_means_,
                                                                        self._cbc_ns,
                                                                        self._cac_ns))
            self._product.paymentmeans = paymentmeans

    def build_paymentterms(self) -> None:
        # ['PaymentTerms'] = ('cac', PaymentTerms(), 'Seçimli (0..1)')
        paymentterms_: Element = self.root.find('./' + self._cac_ns + 'PaymentTerms')
        if paymentterms_:
            self._product.paymentterms = TRUBLPaymentTerms().process_element(paymentterms_,
                                                                             self._cbc_ns,
                                                                             self._cac_ns).name

    def build_allowancecharge(self) -> None:
        # ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)', 'allowancecharge')
        allowancecharges_: list = self.root.findall('./' + self._cac_ns + 'AllowanceCharge')
        if len(allowancecharges_) != 0:
            allowancecharge: list = []
            for allowancecharge_ in allowancecharges_:
                allowancecharge.append(TRUBLAllowanceCharge().process_element(allowancecharge_,
                                                                              self._cbc_ns,
                                                                              self._cac_ns))
            self._product.allowancecharge = allowancecharge

    def build_taxexchangerate(self) -> None:
        # ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'taxexchangerate')
        taxexchangerate_: Element = self.root.find('./' + self._cac_ns + 'TaxExchangeRate')
        if taxexchangerate_:
            self._product.taxexchangerate = TRUBLExchangeRate().process_element(taxexchangerate_,
                                                                                self._cbc_ns,
                                                                                self._cac_ns).name

    def build_pricingexchangerate(self) -> None:
        # ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'pricingexchangerate')
        pricingexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PricingExchangeRate')
        if pricingexchangerate_:
            self._product.pricingexchangerate = TRUBLExchangeRate().process_element(pricingexchangerate_,
                                                                                    self._cbc_ns,
                                                                                    self._cac_ns).name

    def build_paymentexchangerate(self) -> None:
        # ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentexchangerate')
        paymentexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PaymentExchangeRate')
        if paymentexchangerate_:
            self._product.paymentexchangerate = TRUBLExchangeRate().process_element(paymentexchangerate_,
                                                                                    self._cbc_ns,
                                                                                    self._cac_ns).name

    def build_paymentalternativeexchangerate(self) -> None:
        # ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)',
        # 'paymentalternativeexchangerate')
        paymentalternativeexchangerate_: Element = self.root.find(
            './' + self._cac_ns + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate_:
            self._product.paymentalternativeexchangerate = TRUBLExchangeRate().process_element(
                paymentalternativeexchangerate_,
                self._cbc_ns,
                self._cac_ns).name

    def build_taxtotal(self) -> None:
        # ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)', 'taxtotal')
        taxtotals_: list = self.root.findall('./' + self._cac_ns + 'TaxTotal')
        taxtotal: list = []
        for taxtotal_ in taxtotals_:
            taxtotal.append(TRUBLTaxTotal().process_element(taxtotal_,
                                                            self._cbc_ns,
                                                            self._cac_ns))
        self._product.taxtotal = taxtotal

    def build_withholdingtaxtotal(self) -> None:
        # ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'withholdingtaxtotal')
        withholdingtaxtotals_: list = self.root.findall('./' + self._cac_ns + 'WithholdingTaxTotal')
        if len(withholdingtaxtotals_) != 0:
            withholdingtaxtotal: list = []
            for withholdingtaxtotal_ in withholdingtaxtotals_:
                withholdingtaxtotal.append(TRUBLTaxTotal().process_element(withholdingtaxtotal_,
                                                                           self._cbc_ns,
                                                                           self._cac_ns))
            self._product.withholdingtaxtotal = withholdingtaxtotal

    def build_legalmonetarytotal(self) -> None:
        # ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        legalmonetarytotal_: Element = self.root.find('./' + self._cac_ns + 'LegalMonetaryTotal')
        self._product.legalmonetarytotal = TRUBLMonetaryTotal().process_element(legalmonetarytotal_,
                                                                                self._cbc_ns,
                                                                                self._cac_ns).name

    def build_invoiceline(self) -> None:
        # ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)', 'invoiceline')
        invoicelines_: list = self.root.findall('./' + self._cac_ns + 'InvoiceLine')
        invoiceline: list = []
        for invoiceline_ in invoicelines_:
            invoiceline.append(TRUBLInvoiceLine().process_element(invoiceline_,
                                                                  self._cbc_ns,
                                                                  self._cac_ns))
        self._product.invoiceline = invoiceline

    def build_despatchline(self) -> None:
        # ['DespatchLine'] = ('cac', DespatchLine(), 'Zorunlu (1...n)', 'despatchline')
        despatchlines_: list = self.root.findall('./' + self._cac_ns + 'DespatchLine')
        despatchline: list = []
        for despatchline_ in despatchlines_:
            despatchline.append(TRUBLDespatchLine().process_element(despatchline_,
                                                                    self._cbc_ns,
                                                                    self._cac_ns))
        self._product.despatchline = despatchline

    def get_document(self) -> None:
        product = self._product.save()
        self.reset()
        return product
