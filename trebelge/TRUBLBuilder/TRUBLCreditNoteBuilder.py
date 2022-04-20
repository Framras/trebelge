from datetime import datetime
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReference import TRUBLBillingReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLReceiptLine import TRUBLReceiptLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


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
            creditnote_.profileexecutionid = root_.find('./' + self._cbc_ns + 'ProfileExecutionID').text
            creditnote_.id = root_.find('./' + self._cbc_ns + 'ID').text
            creditnote_.copyindicator = root_.find('./' + self._cbc_ns + 'CopyIndicator').text
            creditnote_.issuedate = datetime.strptime(root_.find('./' + self._cbc_ns + 'IssueDate').text,
                                                      "%Y-%m-%d")
            creditnote_.taxpointdate = datetime.strptime(root_.find('./' + self._cbc_ns + 'TaxPointDate').text,
                                                         "%Y-%m-%d")
            creditnote_.creditnotetypecode = root_.find('./' + self._cbc_ns + 'CreditNoteTypeCode').text
            creditnote_.documentcurrencycode = root_.find('./' + self._cbc_ns + 'DocumentCurrencyCode').text
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
            accountingcost_: Element = root_.find('./' + self._cbc_ns + 'AccountingCost')
            if accountingcost_ is not None:
                creditnote_.accountingcost = accountingcost_.text
            creditnote_.linecountnumeric = root_.find('./' + self._cbc_ns + 'LineCountNumeric').text
            creditnote_.insert()
        self.root = root_
        self._product = frappe.get_doc(self._frappeDoctype, uuid_)

    def build_issuetime(self) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = self.root.find('./' + self._cbc_ns + 'IssueTime')
        if issuetime_ is not None:
            try:
                self._product.issuetime = datetime.strptime(issuetime_.text, "%H:%M:%S")
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
        pass

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
        despatchsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'DespatchSupplierParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = despatchsupplierparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.despatchsupplierparty = party.name
        # ['DespatchContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'despatchcontact')
        despatchcontact_: Element = despatchsupplierparty_.find('./' + self._cac_ns + 'DespatchContact')
        if despatchcontact_ is not None:
            contact = TRUBLContact().process_element(despatchcontact_, self._cbc_ns, self._cac_ns)
            if contact is not None:
                self._product.despatchsuppliercontact = contact.name

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
        deliverycustomerparty_: Element = self.root.find('./' + self._cac_ns + 'DeliveryCustomerParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = deliverycustomerparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.deliverycustomerparty = party.name
        # ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
        deliverycontact_: Element = deliverycustomerparty_.find('./' + self._cac_ns + 'DeliveryContact')
        if deliverycontact_ is not None:
            contact = TRUBLContact().process_element(deliverycontact_, self._cbc_ns, self._cac_ns)
            if contact is not None:
                self._product.deliverycustomercontact = contact.name

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
                    self._product.save()

    def build_shipment(self) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Zorunlu (1)', 'shipment')
        shipment_: Element = self.root.find('./' + self._cac_ns + 'Shipment')
        shipment = TRUBLShipment().process_element(shipment_, self._cbc_ns, self._cac_ns)
        if shipment is not None:
            self._product.shipment = shipment.name

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
        # ['PaymentTerms'] = ('cac', PaymentTerms(), 'Seçimli (0..1)')
        paymentterms_: Element = self.root.find('./' + self._cac_ns + 'PaymentTerms')
        if paymentterms_ is not None:
            tmp = TRUBLPaymentTerms().process_element(paymentterms_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.paymentterms = tmp.name

    def build_allowancecharge(self) -> None:
        pass

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

    def build_creditnote(self) -> None:
        pass

    def build_senderparty(self) -> None:
        pass

    def build_receiverparty(self) -> None:
        pass

    def build_documentresponse(self) -> None:
        pass

    def get_document(self) -> None:
        product = self._product.save()
