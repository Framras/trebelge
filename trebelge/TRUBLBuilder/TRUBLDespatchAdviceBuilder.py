from datetime import datetime
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLDespatchLine import TRUBLDespatchLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLDespatchAdviceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    _frappeDoctype: str = 'UBL TR Despatch Advice'

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
            despatchadvice_ = frappe.new_doc(self._frappeDoctype)
            despatchadvice_.uuid = self._uuid
            despatchadvice_.ublversionid = self.root.find('./' + self._cbc_ns + 'UBLVersionID').text
            despatchadvice_.customizationid = self.root.find('./' + self._cbc_ns + 'CustomizationID').text
            despatchadvice_.profileid = self.root.find('./' + self._cbc_ns + 'ProfileID').text
            despatchadvice_.id = self.root.find('./' + self._cbc_ns + 'ID').text
            despatchadvice_.copyindicator = self.root.find('./' + self._cbc_ns + 'CopyIndicator').text
            despatchadvice_.issuedate = self.root.find('./' + self._cbc_ns + 'IssueDate').text
            despatchadvice_.despatchadvicetypecode = self.root.find('./' + self._cbc_ns + 'DespatchAdviceTypeCode').text
            despatchadvice_.linecountnumeric = self.root.find('./' + self._cbc_ns + 'LineCountNumeric').text
            despatchadvice_.insert()
        self._product = frappe.get_doc(self._frappeDoctype, self._uuid)

    def build_issuetime(self) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = self.root.find('./' + self._cbc_ns + 'IssueTime')
        if issuetime_ is not None:
            try:
                self._product.issuetime = datetime.strptime(issuetime_.text, '%H:%M:%S')
            except ValueError:
                pass
        else:
            self._product.issuetime = ""

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
        pass

    def build_orderreference(self) -> None:
        # ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...n)', 'orderreference')
        orderreferences_: list = self.root.findall('./' + self._cac_ns + 'OrderReference')
        if len(orderreferences_) != 0:
            doc_append = self._product.append("orderreference", {})
            for orderreference_ in orderreferences_:
                tmp = TRUBLOrderReference().process_element(orderreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.orderreference = tmp.name

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
        documentreferences_: list = self.root.findall('./' + self._cac_ns + 'AdditionalDocumentReference')
        if len(documentreferences_) != 0:
            doc_append = self._product.append("additionaldocumentreference", {})
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, self._cbc_ns, self._cac_ns)
                if tmp is not None:
                    doc_append.documentreference = tmp.name

    def build_accountingsupplierparty(self) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        pass

    def build_despatchsupplierparty(self) -> None:
        # ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        despatchsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'DespatchSupplierParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = despatchsupplierparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.despatchsupplierparty = party.name

    def build_accountingcustomerparty(self) -> None:
        # ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        pass

    def build_deliverycustomerparty(self) -> None:
        # ['DeliveryCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'deliverycustomerparty')
        deliverycustomerparty_: Element = self.root.find('./' + self._cac_ns + 'DeliveryCustomerParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = deliverycustomerparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.deliverycustomerparty = party.name

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
        originatorcustomerparty_: Element = self.root.find('./' + self._cac_ns + 'OriginatorCustomerParty')
        if originatorcustomerparty_ is not None:
            # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
            party_: Element = originatorcustomerparty_.find('./' + self._cac_ns + 'Party')
            party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
            self._product.originatorcustomerparty = party.name

    def build_taxrepresentativeparty(self) -> None:
        # ['TaxRepresentativeParty'] = ('cac', Party(), 'Seçimli (0..1)', 'taxrepresentativeparty')
        pass

    def build_delivery(self) -> None:
        # ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)', 'delivery')
        pass

    def build_shipment(self) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Zorunlu (1)', 'shipment')
        shipment_: Element = self.root.find('./' + self._cac_ns + 'Shipment')
        shipment = TRUBLShipment().process_element(shipment_, self._cbc_ns, self._cac_ns)
        if shipment is not None:
            self._product.shipment = shipment.name

    def build_paymentmeans(self) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)', 'paymentmeans')
        pass

    def build_paymentterms(self) -> None:
        # ['PaymentTerms'] = ('cac', PaymentTerms(), 'Seçimli (0..1)')
        pass

    def build_allowancecharge(self) -> None:
        # ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)', 'allowancecharge')
        pass

    def build_taxexchangerate(self) -> None:
        # ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'taxexchangerate')
        pass

    def build_pricingexchangerate(self) -> None:
        # ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'pricingexchangerate')
        pass

    def build_paymentexchangerate(self) -> None:
        # ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentexchangerate')
        pass

    def build_paymentalternativeexchangerate(self) -> None:
        # ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)',
        # 'paymentalternativeexchangerate')
        pass

    def build_taxtotal(self) -> None:
        # ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)', 'taxtotal')
        pass

    def build_withholdingtaxtotal(self) -> None:
        # ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'withholdingtaxtotal')
        pass

    def build_legalmonetarytotal(self) -> None:
        # ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        pass

    def build_invoiceline(self) -> None:
        # ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)', 'invoiceline')
        pass

    def build_despatchline(self) -> None:
        # ['DespatchLine'] = ('cac', DespatchLine(), 'Zorunlu (1...n)', 'despatchline')
        despatchlines_: list = self.root.findall('./' + self._cac_ns + 'DespatchLine')
        for despatchline_ in despatchlines_:
            tmp = TRUBLDespatchLine().process_element(despatchline_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                self._product.append("despatchline",
                                     dict(delivered=str(tmp.get_value('deliveredquantity')) + " " + frappe.db.get_value(
                                              'UBL TR Unitcodes', tmp.get_value('deliveredquantityunitcode'),
                                              'unitcodename'),
                                          despatchline=tmp.name))

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

    def build_discrepancyresponse(self) -> None:
        pass

    def build_statementdocumentreference(self) -> None:
        pass

    def build_deliveryterms(self) -> None:
        pass

    def build_creditnoteline(self) -> None:
        pass

    def build_payeeparty(self) -> None:
        pass

    def get_document(self) -> None:
        self._product.save()
