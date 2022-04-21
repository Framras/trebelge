from datetime import datetime
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLReceiptLine import TRUBLReceiptLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLReceiptAdviceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    _frappeDoctype: str = 'UBL TR Receipt Advice'

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
            receiptadvice_ = frappe.new_doc(self._frappeDoctype)
            receiptadvice_.uuid = self._uuid
            receiptadvice_.ublversionid = self.root.find('./' + self._cbc_ns + 'UBLVersionID').text
            receiptadvice_.customizationid = self.root.find('./' + self._cbc_ns + 'CustomizationID').text
            receiptadvice_.profileid = self.root.find('./' + self._cbc_ns + 'ProfileID').text
            receiptadvice_.id = self.root.find('./' + self._cbc_ns + 'ID').text
            receiptadvice_.copyindicator = self.root.find('./' + self._cbc_ns + 'CopyIndicator').text
            receiptadvice_.issuedate = self.root.find('./' + self._cbc_ns + 'IssueDate').text
            receiptadvice_.receiptadvicetypecode = self.root.find('./' + self._cbc_ns + 'ReceiptAdviceTypeCode').text
            receiptadvice_.linecountnumeric = self.root.find('./' + self._cbc_ns + 'LineCountNumeric').text
            receiptadvice_.insert()
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
                    self._product.save()

    def build_invoiceperiod(self) -> None:
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
                    self._product.save()

    def build_billingreference(self) -> None:
        pass

    def build_despatchdocumentreference(self) -> None:
        # ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Zorunlu (1)', 'despatchdocumentreference')
        despatchdocumentreference_: Element = self.root.find('./' + self._cac_ns + 'DespatchDocumentReference')
        self._product.despatchdocumentreference = TRUBLDocumentReference().process_element(despatchdocumentreference_,
                                                                                           self._cbc_ns,
                                                                                           self._cac_ns).name

    def build_receiptdocumentreference(self) -> None:
        pass

    def build_originatordocumentreference(self) -> None:
        pass

    def build_contractdocumentreference(self) -> None:
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
                    self._product.save()

    def build_accountingsupplierparty(self) -> None:
        pass

    def build_despatchsupplierparty(self) -> None:
        # ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        despatchsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'DespatchSupplierParty')
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = despatchsupplierparty_.find('./' + self._cac_ns + 'Party')
        party = TRUBLParty().process_element(party_, self._cbc_ns, self._cac_ns)
        self._product.despatchsupplierparty = party.name

    def build_accountingcustomerparty(self) -> None:
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
        pass

    def build_taxrepresentativeparty(self) -> None:
        pass

    def build_delivery(self) -> None:
        pass

    def build_shipment(self) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Zorunlu (1)', 'shipment')
        shipment_: Element = self.root.find('./' + self._cac_ns + 'Shipment')
        shipment = TRUBLShipment().process_element(shipment_, self._cbc_ns, self._cac_ns)
        if shipment is not None:
            self._product.shipment = shipment.name

    def build_paymentmeans(self) -> None:
        pass

    def build_paymentterms(self) -> None:
        pass

    def build_allowancecharge(self) -> None:
        pass

    def build_taxexchangerate(self) -> None:
        pass

    def build_pricingexchangerate(self) -> None:
        pass

    def build_paymentexchangerate(self) -> None:
        pass

    def build_paymentalternativeexchangerate(self) -> None:
        pass

    def build_taxtotal(self) -> None:
        pass

    def build_withholdingtaxtotal(self) -> None:
        pass

    def build_legalmonetarytotal(self) -> None:
        pass

    def build_invoiceline(self) -> None:
        pass

    def build_despatchline(self) -> None:
        pass

    def build_receiptline(self) -> None:
        # ['ReceiptLine'] = ('cac', ReceiptLine(), 'Zorunlu (1...n)', 'receiptline')
        receiptlines_: list = self.root.findall('./' + self._cac_ns + 'ReceiptLine')
        doc_append = self._product.append("receiptline", {})
        for receiptline_ in receiptlines_:
            tmp = TRUBLReceiptLine().process_element(receiptline_, self._cbc_ns, self._cac_ns)
            if tmp is not None:
                doc_append.receiptline = tmp.name
                self._product.save()

    def build_senderparty(self) -> None:
        pass

    def build_receiverparty(self) -> None:
        pass

    def build_documentresponse(self) -> None:
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
        product = self._product.save()
