from datetime import datetime
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReference import TRUBLBillingReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
from trebelge.TRUBLCommonElementsStrategy.TRUBLInvoiceLine import TRUBLInvoiceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLLegalMonetaryTotal import TRUBLLegalMonetaryTotal
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

    def __init__(self, root: Element, cac_ns: str, cbc_ns: str, uuid: str) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.root = root
        self._cac_ns = cac_ns
        self._cbc_ns = cbc_ns
        self._uuid = uuid
        self._product = None

    def reset(self) -> None:
        if len(frappe.get_all(self._frappeDoctype, filters={'uuid': self._uuid})) == 0:
            invoice_ = frappe.new_doc(self._frappeDoctype)
            invoice_.uuid = self._uuid
            invoice_.ublversionid = self.root.find('./' + self._cbc_ns + 'UBLVersionID').text
            invoice_.customizationid = self.root.find('./' + self._cbc_ns + 'CustomizationID').text
            invoice_.profileid = self.root.find('./' + self._cbc_ns + 'ProfileID').text
            invoice_.id = self.root.find('./' + self._cbc_ns + 'ID').text
            invoice_.copyindicator = self.root.find('./' + self._cbc_ns + 'CopyIndicator').text
            invoice_.issuedate = self.root.find('./' + self._cbc_ns + 'IssueDate').text
            invoice_.invoicetypecode = self.root.find('./' + self._cbc_ns + 'InvoiceTypeCode').text
            invoice_.documentcurrencycode = self.root.find('./' + self._cbc_ns + 'DocumentCurrencyCode').text
            taxcurrencycode_: Element = self.root.find('./' + self._cbc_ns + 'TaxCurrencyCode')
            if taxcurrencycode_ is not None:
                invoice_.taxcurrencycode = taxcurrencycode_.text
            pricingcurrencycode_: Element = self.root.find('./' + self._cbc_ns + 'PricingCurrencyCode')
            if pricingcurrencycode_ is not None:
                invoice_.pricingcurrencycode = pricingcurrencycode_.text
            paymentcurrencycode_: Element = self.root.find('./' + self._cbc_ns + 'PaymentCurrencyCode')
            if paymentcurrencycode_ is not None:
                invoice_.paymentcurrencycode = paymentcurrencycode_.text
            paymentalternativecurrencycode_: Element = self.root.find(
                './' + self._cbc_ns + 'PaymentAlternativeCurrencyCode')
            if paymentalternativecurrencycode_ is not None:
                invoice_.paymentalternativecurrencycode = paymentalternativecurrencycode_.text
            accountingcost_: Element = self.root.find('./' + self._cbc_ns + 'AccountingCost')
            if accountingcost_ is not None:
                invoice_.accountingcost = accountingcost_.text
            invoice_.linecountnumeric = self.root.find('./' + self._cbc_ns + 'LineCountNumeric').text
            invoice_.insert()
        self._product = frappe.get_doc(self._frappeDoctype, self._uuid)

    def build_issuetime(self) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = self.root.find('./' + self._cbc_ns + 'IssueTime')
        if issuetime_ is not None:
            try:
                self._product.issuetime = datetime.strptime(issuetime_.text, '%H:%M:%S')
            except ValueError:
                pass

    def build_note(self) -> None:
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...n)', 'note')
        notes_: list = self.root.findall('./' + self._cbc_ns + 'Note')
        if len(notes_) != 0:
            for note_ in notes_:
                element_ = note_.text
                if element_ is not None and element_.strip() != '':
                    self._product.append("note", dict(note=element_.strip()))

    def build_invoiceperiod(self) -> None:
        # ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)', 'invoiceperiod')
        invoiceperiod_: Element = self.root.find('./' + self._cac_ns + 'InvoicePeriod')
        if invoiceperiod_ is not None:
            tmp: dict = TRUBLPeriod().process_elementasdict(invoiceperiod_, self._cbc_ns, self._cac_ns)
            if tmp != {}:
                try:
                    self._product.startdate = tmp['startdate']
                    self._product.starttime = tmp['starttime']
                except KeyError:
                    pass
                try:
                    self._product.enddate = tmp['enddate']
                    self._product.endtime = tmp['endtime']
                except KeyError:
                    pass
                try:
                    self._product.durationmeasure = tmp['durationmeasure']
                    self._product.durationmeasure_unitcode = tmp['durationmeasure_unitcode']
                except KeyError:
                    pass
                try:
                    self._product.description = tmp['description']
                except KeyError:
                    pass

    def build_discrepancyresponse(self) -> None:
        # TODO : Implement this: maybe a Response of (0..n) cardinality
        pass

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
            doc_append = self._product.append("billingreference", {})
            for billingreference_ in billingreferences_:
                tmp = TRUBLBillingReference().process_element(billingreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.billingreference = tmp.name

    def build_despatchdocumentreference(self) -> None:
        # ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'despatchdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'DespatchDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("despatchdocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name

    def build_receiptdocumentreference(self) -> None:
        # ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'receiptdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ReceiptDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("receiptdocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name

    def build_originatordocumentreference(self) -> None:
        # ['OriginatorDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'originatordocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'OriginatorDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("originatordocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name

    def build_contractdocumentreference(self) -> None:
        # ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'contractdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ContractDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("contractdocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name

    def build_additionaldocumentreference(self) -> None:
        # ['AdditionalDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'additionaldocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'AdditionalDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("additionaldocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name

    def build_statementdocumentreference(self) -> None:
        pass

    def build_accountingsupplierparty(self) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        accountingsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'AccountingSupplierParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = accountingsupplierparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.accountingsupplierparty = party.name

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

    def build_sellersupplierparty(self) -> None:
        # ['SellerSupplierParty'] = ('cac', SupplierParty(), 'Seçimli (0..1)', 'sellersupplierparty')
        sellersupplierparty_: Element = self.root.find('./' + self._cac_ns + 'SellerSupplierParty')
        if sellersupplierparty_ is not None:
            # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
            party_: Element = sellersupplierparty_.find('./' + self._cac_ns + 'Party')
            party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
            self._product.sellersupplierparty = party.name

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
            doc_append = self._product.append("delivery", {})
            for delivery_ in deliveries_:
                tmp = TRUBLDelivery().process_element(delivery_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.delivery = tmp.name

    def build_shipment(self) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Seçimli (0...n)', 'shipment')
        pass

    def build_paymentmeans(self) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)', 'paymentmeans')
        paymentmeans_: list = self.root.findall('./' + self._cac_ns + 'PaymentMeans')
        if len(paymentmeans_) != 0:
            doc_append = self._product.append("paymentmeans", {})
            for payment_means_ in paymentmeans_:
                tmp = TRUBLPaymentMeans().process_element(payment_means_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.paymentmeans = tmp.name

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
            doc_append = self._product.append("allowancecharge", {})
            for allowancecharge_ in allowancecharges_:
                tmp = TRUBLAllowanceCharge().process_element(allowancecharge_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.allowancecharge = tmp.name

    def build_taxexchangerate(self) -> None:
        # ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'taxexchangerate')
        taxexchangerate_: Element = self.root.find('./' + self._cac_ns + 'TaxExchangeRate')
        if taxexchangerate_ is not None:
            tmp: dict = TRUBLExchangeRate().process_elementasdict(taxexchangerate_, self._cbc_ns, self._cac_ns)
            if tmp != {}:
                try:
                    self._product.taxsourcecurrencycode = tmp['sourcecurrencycode']
                    self._product.taxtargetcurrencycode = tmp['targetcurrencycode']
                    self._product.taxcalculationrate = tmp['calculationrate']
                except KeyError:
                    pass
                try:
                    self._product.taxcurrencydate = tmp['date']
                except KeyError:
                    pass

    def build_pricingexchangerate(self) -> None:
        # ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'pricingexchangerate')
        pricingexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PricingExchangeRate')
        if pricingexchangerate_ is not None:
            tmp: dict = TRUBLExchangeRate().process_elementasdict(pricingexchangerate_, self._cbc_ns, self._cac_ns)
            if tmp != {}:
                try:
                    self._product.pricingsourcecurrencycode = tmp['sourcecurrencycode']
                    self._product.pricingtargetcurrencycode = tmp['targetcurrencycode']
                    self._product.pricingcalculationrate = tmp['calculationrate']
                except KeyError:
                    pass
                try:
                    self._product.pricingcurrencydate = tmp['date']
                except KeyError:
                    pass

    def build_paymentexchangerate(self) -> None:
        # ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentexchangerate')
        paymentexchangerate_: Element = self.root.find('./' + self._cac_ns + 'PaymentExchangeRate')
        if paymentexchangerate_ is not None:
            tmp: dict = TRUBLExchangeRate().process_elementasdict(paymentexchangerate_, self._cbc_ns, self._cac_ns)
            if tmp != {}:
                try:
                    self._product.paymentsourcecurrencycode = tmp['sourcecurrencycode']
                    self._product.paymenttargetcurrencycode = tmp['targetcurrencycode']
                    self._product.paymentcalculationrate = tmp['calculationrate']
                except KeyError:
                    pass
                try:
                    self._product.paymentcurrencydate = tmp['date']
                except KeyError:
                    pass

    def build_paymentalternativeexchangerate(self) -> None:
        # ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)',
        # 'paymentalternativeexchangerate')
        paymentalternativeexchangerate_: Element = self.root.find(
            './' + self._cac_ns + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate_ is not None:
            tmp: dict = TRUBLExchangeRate().process_elementasdict(paymentalternativeexchangerate_, self._cbc_ns,
                                                                  self._cac_ns)
            if tmp != {}:
                try:
                    self._product.alternativesourcecurrencycode = tmp['sourcecurrencycode']
                    self._product.alternativetargetcurrencycode = tmp['targetcurrencycode']
                    self._product.alternativecalculationrate = tmp['calculationrate']
                except KeyError:
                    pass
                try:
                    self._product.alternativecurrencydate = tmp['date']
                except KeyError:
                    pass

    def build_taxtotal(self) -> None:
        # ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)', 'taxtotal')
        taxtotals_: list = self.root.findall('./' + self._cac_ns + 'TaxTotal')
        doc_append = self._product.append("taxtotal", {})
        for taxtotal_ in taxtotals_:
            tmp = TRUBLTaxTotal().process_element(taxtotal_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                doc_append.taxtotal = tmp.name

    def build_withholdingtaxtotal(self) -> None:
        # ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'withholdingtaxtotal')
        withholdingtaxtotals_: list = self.root.findall('./' + self._cac_ns + 'WithholdingTaxTotal')
        if len(withholdingtaxtotals_) != 0:
            doc_append = self._product.append("withholdingtaxtotal", {})
            for withholdingtaxtotal_ in withholdingtaxtotals_:
                tmp = TRUBLTaxTotal().process_element(withholdingtaxtotal_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.taxtotal = tmp.name

    def build_legalmonetarytotal(self) -> None:
        # ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        legalmonetarytotal_: Element = self.root.find('./' + self._cac_ns + 'LegalMonetaryTotal')
        tmp = TRUBLLegalMonetaryTotal().process_elementasdict(legalmonetarytotal_, self._cbc_ns, self._cac_ns)
        # ['LineExtensionAmount'] = ('cbc', 'lineextensionamount', 'Zorunlu(1)')
        self._product.lineextensionamount = tmp['lineextensionamount']
        self._product.lineextensionamountcurrencyid = tmp['lineextensionamountcurrencyid']
        # ['TaxExclusiveAmount'] = ('cbc', 'taxexclusiveamount', 'Zorunlu(1)')
        self._product.taxexclusiveamount = tmp['taxexclusiveamount']
        self._product.taxexclusiveamountcurrencyid = tmp['taxexclusiveamountcurrencyid']
        # ['TaxInclusiveAmount'] = ('cbc', 'taxinclusiveamount', 'Zorunlu(1)')
        self._product.taxinclusiveamount = tmp['taxinclusiveamount']
        self._product.taxinclusiveamountcurrencyid = tmp['taxinclusiveamountcurrencyid']
        # ['PayableAmount'] = ('cbc', 'payableamount', 'Zorunlu(1)')
        self._product.payableamount = tmp['payableamount']
        self._product.payableamountcurrencyid = tmp['payableamountcurrencyid']
        # ['AllowanceTotalAmount'] = ('cbc', 'allowancetotalamount', 'Seçimli (0...1)')
        try:
            self._product.allowancetotalamount = tmp['allowancetotalamount']
            self._product.allowancetotalamountcurrencyid = tmp['allowancetotalamountcurrencyid']
        except KeyError:
            pass
        # ['ChargeTotalAmount'] = ('cbc', 'chargetotalamount', 'Seçimli (0...1)')
        try:
            self._product.chargetotalamount = tmp['chargetotalamount']
            self._product.chargetotalamountcurrencyid = tmp['chargetotalamountcurrencyid']
        except KeyError:
            pass
        # ['PayableRoundingAmount'] = ('cbc', 'payableroundingamount', 'Seçimli (0...1)')
        try:
            self._product.payableroundingamount = tmp['payableroundingamount']
            self._product.payableroundingamountcurrencyid = tmp['payableroundingamountcurrencyid']
        except KeyError:
            pass

    def build_invoiceline(self) -> None:
        # ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)', 'invoiceline')
        invoicelines_: list = self.root.findall('./' + self._cac_ns + 'InvoiceLine')
        # doc_append = self._product.append("invoiceline", {})
        for invoiceline_ in invoicelines_:
            tmp = TRUBLInvoiceLine().process_element(invoiceline_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.append("invoicelinesummary",
                                     dict(invoiced=str(tmp.get_value('invoicedquantity')) + " " + frappe.db.get_value(
                                              'UBL TR Unitcodes', tmp.get_value('invoicedquantityunitcode'),
                                              'unitcodename'),
                                          price=str(tmp.get_value('priceamount')) + " " + tmp.get_value(
                                              'priceamountcurrencyid'),
                                          lineextension=str(tmp.get_value('lineextensionamount')) + " " + tmp.get_value(
                                              'lineextensionamountcurrencyid'),
                                          invoiceline=tmp.name))

    def build_despatchline(self) -> None:
        # ['DespatchLine'] = ('cac', DespatchLine(), 'Zorunlu (1...n)', 'despatchline')
        pass

    def build_receiptline(self) -> None:
        pass

    def build_senderparty(self) -> None:
        # ['SenderParty'] = ('cac', Party(), 'Zorunlu (1)', 'senderparty')
        pass

    def build_receiverparty(self) -> None:
        # ['ReceiverParty'] = ('cac', Party(), 'Zorunlu (1)', 'receiverparty')
        pass

    def build_documentresponse(self) -> None:
        # ['DocumentResponse'] = ('cac', DocumentResponse(), 'Zorunlu (1)', 'documentresponse')
        pass

    def build_payeeparty(self) -> None:
        pass

    def build_creditnoteline(self) -> None:
        pass

    def build_deliveryterms(self) -> None:
        pass

    def get_document(self) -> None:
        self._product.save()
