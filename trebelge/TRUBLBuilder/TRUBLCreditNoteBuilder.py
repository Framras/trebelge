import time
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReference import TRUBLBillingReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLDeliveryTerms import TRUBLDeliveryTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
from trebelge.TRUBLCommonElementsStrategy.TRUBLMonetaryTotal import TRUBLMonetaryTotal
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentMeans import TRUBLPaymentMeans
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentTerms import TRUBLPaymentTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal


class TRUBLCreditNoteBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    _frappeDoctype: str = 'UBL TR Credit Note'

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
            creditnote_ = frappe.new_doc(self._frappeDoctype)
            creditnote_.uuid = uuid_
            creditnote_.ublversionid = root_.find('./' + self._cbc_ns + 'UBLVersionID').text
            creditnote_.customizationid = root_.find('./' + self._cbc_ns + 'CustomizationID').text
            creditnote_.profileid = root_.find('./' + self._cbc_ns + 'ProfileID').text
            profileexecutionid_: Element = root_.find('./' + self._cbc_ns + 'ProfileExecutionID')
            if profileexecutionid_ is not None:
                creditnote_.profileexecutionid = profileexecutionid_.text
            creditnote_.id = root_.find('./' + self._cbc_ns + 'ID').text
            creditnote_.copyindicator = root_.find('./' + self._cbc_ns + 'CopyIndicator').text
            creditnote_.issuedate = time.strptime(root_.find('./' + self._cbc_ns + 'IssueDate').text,
                                                  "%Y-%m-%d")
            taxpointdate_ = root_.find('./' + self._cbc_ns + 'TaxPointDate')
            if taxpointdate_ is not None:
                creditnote_.taxpointdate = time.strptime(taxpointdate_.text, "%Y-%m-%d")
            creditnote_.creditnotetypecode = root_.find('./' + self._cbc_ns + 'CreditNoteTypeCode').text
            documentcurrencycode_: Element = root_.find('./' + self._cbc_ns + 'DocumentCurrencyCode')
            if documentcurrencycode_ is not None:
                creditnote_.documentcurrencycode = documentcurrencycode_.text
            taxcurrencycode_: Element = root_.find('./' + self._cbc_ns + 'TaxCurrencyCode')
            if taxcurrencycode_ is not None:
                creditnote_.taxcurrencycode = taxcurrencycode_.text
            pricingcurrencycode_: Element = root_.find('./' + self._cbc_ns + 'PricingCurrencyCode')
            if pricingcurrencycode_ is not None:
                creditnote_.pricingcurrencycode = pricingcurrencycode_.text
            paymentcurrencycode_: Element = root_.find('./' + self._cbc_ns + 'PaymentCurrencyCode')
            if paymentcurrencycode_ is not None:
                creditnote_.paymentcurrencycode = paymentcurrencycode_.text
            paymentalternativecurrencycode_: Element = root_.find(
                './' + self._cbc_ns + 'PaymentAlternativeCurrencyCode')
            if paymentalternativecurrencycode_ is not None:
                creditnote_.paymentalternativecurrencycode = paymentalternativecurrencycode_.text
            accountingcostcode_: Element = root_.find('./' + self._cbc_ns + 'AccountingCostCode')
            if accountingcostcode_ is not None:
                creditnote_.accountingcostcode = accountingcostcode_.text
            accountingcost_: Element = root_.find('./' + self._cbc_ns + 'AccountingCost')
            if accountingcost_ is not None:
                creditnote_.accountingcost = accountingcost_.text
            creditnote_.linecountnumeric = root_.find('./' + self._cbc_ns + 'LineCountNumeric').text
            buyerreference_: Element = root_.find('./' + self._cbc_ns + 'BuyerReference')
            if buyerreference_ is not None:
                creditnote_.buyerreference = buyerreference_.text
            creditnote_.insert()
        self.root = root_
        self._product = frappe.get_doc(self._frappeDoctype, uuid_)

    def build_issuetime(self) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = self.root.find('./' + self._cbc_ns + 'IssueTime')
        if issuetime_ is not None:
            try:
                self._product.issuetime = time.strptime(issuetime_.text, "%H:%M:%S")
            except ValueError:
                pass
        else:
            self._product.issuetime = ""

    def build_note(self) -> None:
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...n)', 'note')
        notes_: list = self.root.findall('./' + self._cbc_ns + 'Note')
        if len(notes_) != 0:
            doc_append = self._product.append("note", {})
            for note_ in notes_:
                tmp = TRUBLNote().process_element(note_, self._cbc_ns, self._cbc_ns)
                if tmp is not None:
                    doc_append.note = tmp.name
                    self._product.save()

    def build_invoiceperiod(self) -> None:
        # ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)', 'invoiceperiod')
        invoiceperiod_: Element = self.root.find('./' + self._cac_ns + 'InvoicePeriod')
        if invoiceperiod_ is not None:
            tmp = TRUBLPeriod().process_element(invoiceperiod_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.invoiceperiod = tmp.name

    def build_discrepancyresponse(self) -> None:
        # TODO : Implement this
        # <xsd:element ref="cac:DiscrepancyResponse" minOccurs="0" maxOccurs="unbounded"/>
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
                    self._product.save()

    def build_despatchdocumentreference(self) -> None:
        # ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'despatchdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'DespatchDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("despatchdocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name
                    self._product.save()

    def build_receiptdocumentreference(self) -> None:
        # ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'receiptdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ReceiptDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("receiptdocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name
                    self._product.save()

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
                    self._product.save()

    def build_contractdocumentreference(self) -> None:
        # ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'contractdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'ContractDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("contractdocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name
                    self._product.save()

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
                    self._product.save()

    def build_statementdocumentreference(self) -> None:
        # ['StatementDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'statementdocumentreference')
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'StatementDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("statementdocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name
                    self._product.save()

    def build_accountingsupplierparty(self) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        accountingsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'AccountingSupplierParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = accountingsupplierparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.accountingsupplierparty = party.name

    def build_accountingcustomerparty(self) -> None:
        # ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        accountingcustomerparty_: Element = self.root.find('./' + self._cac_ns + 'AccountingCustomerParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = accountingcustomerparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.accountingcustomerparty = party.name

    def build_payeeparty(self) -> None:
        # <xsd:element ref="cac:PayeeParty" minOccurs="0" maxOccurs="1"/>
        payeeparty_: Element = self.root.find('./' + self._cac_ns + 'PayeeParty')
        if payeeparty_ is not None:
            # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
            party_: Element = payeeparty_.find('./' + self._cac_ns + 'Party')
            party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
            self._product.payeeparty = party.name

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
                    self._product.save()

    def build_deliveryterms(self) -> None:
        # ['DeliveryTerms'] = ('cac', DeliveryTerms(), 'Seçimli (0...n)', 'deliveryterms')
        deliveryterms_: list = self.root.findall('./' + self._cac_ns + 'DeliveryTerms')
        if len(deliveryterms_) != 0:
            doc_append = self._product.append("deliveryterms", {})
            for deliveryterm_ in deliveryterms_:
                tmp = TRUBLDeliveryTerms().process_element(deliveryterm_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.deliveryterms = tmp.name
                    self._product.save()

    def build_paymentmeans(self) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)', 'paymentmeans')
        paymentmeans_: list = self.root.findall('./' + self._cac_ns + 'PaymentMeans')
        if len(paymentmeans_) != 0:
            doc_append = self._product.append("paymentmeans", {})
            for payment_means_ in paymentmeans_:
                tmp = TRUBLPaymentMeans().process_element(payment_means_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.paymentmeans = tmp.name
                    self._product.save()

    def build_paymentterms(self) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)', 'paymentmeans')
        paymentterms_: list = self.root.findall('./' + self._cac_ns + 'PaymentTerms')
        if len(paymentterms_) != 0:
            doc_append = self._product.append("paymentterms", {})
            for payment_terms_ in paymentterms_:
                tmp = TRUBLPaymentTerms().process_element(payment_terms_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.paymentterms = tmp.name
                    self._product.save()

    def build_allowancecharge(self) -> None:
        # ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)', 'allowancecharge')
        allowancecharges_: list = self.root.findall('./' + self._cac_ns + 'AllowanceCharge')
        if len(allowancecharges_) != 0:
            doc_append = self._product.append("allowancecharge", {})
            for allowancecharge_ in allowancecharges_:
                tmp = TRUBLAllowanceCharge().process_element(allowancecharge_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.allowancecharge = tmp.name
                    self._product.save()

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
        # ['TaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'taxtotal')
        taxtotals_: list = self.root.findall('./' + self._cac_ns + 'TaxTotal')
        if len(taxtotals_) != 0:
            doc_append = self._product.append("taxtotal", {})
            for taxtotal_ in taxtotals_:
                tmp = TRUBLTaxTotal().process_element(taxtotal_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.taxtotal = tmp.name
                    self._product.save()

    def build_withholdingtaxtotal(self) -> None:
        pass

    def build_legalmonetarytotal(self) -> None:
        # ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        legalmonetarytotal_: Element = self.root.find('./' + self._cac_ns + 'LegalMonetaryTotal')
        self._product.legalmonetarytotal = TRUBLMonetaryTotal().process_element(legalmonetarytotal_,
                                                                                self._cbc_ns,
                                                                                self._cac_ns).name

    def build_invoiceline(self) -> None:
        pass

    def build_despatchline(self) -> None:
        pass

    def build_receiptline(self) -> None:
        pass

    def build_creditnoteline(self) -> None:
        # TODO : Implement this
        # <xsd:element ref="cac:CreditNoteLine" minOccurs="1" maxOccurs="unbounded"/>
        pass

    def build_senderparty(self) -> None:
        pass

    def build_receiverparty(self) -> None:
        pass

    def build_documentresponse(self) -> None:
        pass

    def build_shipment(self) -> None:
        pass

    def build_originatorcustomerparty(self) -> None:
        pass

    def build_deliverycustomerparty(self) -> None:
        pass

    def build_despatchsupplierparty(self) -> None:
        pass

    def get_document(self) -> None:
        product = self._product.save()
