import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReference import TRUBLBillingReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLCustomerParty import TRUBLCustomerParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLDespatchLine import TRUBLDespatchLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment
from trebelge.TRUBLCommonElementsStrategy.TRUBLSupplierParty import TRUBLSupplierParty


class TRUBLDespatchAdviceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """
    _frappeDoctype: str = 'UBL TR Despatch Advice'

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
            despatchadvice_ = frappe.new_doc(self._frappeDoctype)
            despatchadvice_.uuid = uuid_
            despatchadvice_.ublversionid = root_.find('./' + self._cbc_ns + 'UBLVersionID').text
            despatchadvice_.customizationid = root_.find('./' + self._cbc_ns + 'CustomizationID').text
            despatchadvice_.profileid = root_.find('./' + self._cbc_ns + 'ProfileID').text
            despatchadvice_.id = root_.find('./' + self._cbc_ns + 'ID').text
            despatchadvice_.copyindicator = root_.find('./' + self._cbc_ns + 'CopyIndicator').text
            despatchadvice_.issuedate = root_.find('./' + self._cbc_ns + 'IssueDate').text
            despatchadvice_.despatchadvicetypecode = root_.find('./' + self._cbc_ns + 'DespatchAdviceTypeCode').text
            despatchadvice_.linecountnumeric = root_.find('./' + self._cbc_ns + 'LineCountNumeric').text
            despatchadvice_.insert()
        self.root = root_
        self._product = frappe.get_doc(self._frappeDoctype, uuid_)

    def build_issuetime(self) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = self.root.find('./' + self._cbc_ns + 'IssueTime')
        if issuetime_:
            self._product.issuetime = issuetime_.text
        else:
            self._product.issuetime = ""

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

    def build_invoiceperiod(self) -> None:
        # ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)', 'invoiceperiod')
        pass

    def build_orderreference(self) -> None:
        # ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...n)', 'orderreference')
        orderreferences_: list = self.root.findall('./' + self._cac_ns + 'OrderReference')
        if len(orderreferences_) != 0:
            orderreference: list = []
            for orderreference_ in orderreferences_:
                orderreference.append(TRUBLBillingReference().process_element(orderreference_,
                                                                              self._cbc_ns,
                                                                              self._cac_ns))
            self._product.orderreference = orderreference

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
            documentreference: list = []
            for documentreference_ in documentreferences_:
                documentreference.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                  self._cbc_ns,
                                                                                  self._cac_ns))
            self._product.additionaldocumentreference = documentreference

    def build_accountingsupplierparty(self) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        pass

    def build_despatchsupplierparty(self) -> None:
        # ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        despatchsupplierparty_: Element = self.root.find('./' + self._cac_ns + 'DespatchSupplierParty')
        self._product.despatchsupplierparty = TRUBLSupplierParty().process_element(despatchsupplierparty_,
                                                                                   self._cbc_ns,
                                                                                   self._cac_ns).name

    def build_accountingcustomerparty(self) -> None:
        # ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        pass

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
        pass

    def build_delivery(self) -> None:
        # ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)', 'delivery')
        pass

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
