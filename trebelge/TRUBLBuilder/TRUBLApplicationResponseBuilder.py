import time
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentResponse import TRUBLDocumentResponse
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLApplicationResponseBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """
    _frappeDoctype: str = 'UBL TR Application Response'

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
            applicationresponse_ = frappe.new_doc(self._frappeDoctype)
            applicationresponse_.uuid = uuid_
            applicationresponse_.ublversionid = root_.find('./' + self._cbc_ns + 'UBLVersionID').text
            applicationresponse_.customizationid = root_.find('./' + self._cbc_ns + 'CustomizationID').text
            applicationresponse_.profileid = root_.find('./' + self._cbc_ns + 'ProfileID').text
            applicationresponse_.id = root_.find('./' + self._cbc_ns + 'ID').text
            applicationresponse_.issuedate = root_.find('./' + self._cbc_ns + 'IssueDate').text
            applicationresponse_.insert()
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
            for note_ in notes_:
                tmp = TRUBLNote().process_element(note_, self._cbc_ns, self._cbc_ns)
                doc_append = self._product.append("note", {})
                if tmp is not None:
                    doc_append.note = tmp.name
                    self._product.save()

    def build_invoiceperiod(self) -> None:
        pass

    def build_orderreference(self) -> None:
        pass

    def build_billingreference(self) -> None:
        pass

    def build_despatchdocumentreference(self) -> None:
        pass

    def build_receiptdocumentreference(self) -> None:
        pass

    def build_originatordocumentreference(self) -> None:
        pass

    def build_contractdocumentreference(self) -> None:
        pass

    def build_additionaldocumentreference(self) -> None:
        pass

    def build_accountingsupplierparty(self) -> None:
        pass

    def build_despatchsupplierparty(self) -> None:
        pass

    def build_accountingcustomerparty(self) -> None:
        pass

    def build_deliverycustomerparty(self) -> None:
        pass

    def build_buyercustomerparty(self) -> None:
        pass

    def build_sellersupplierparty(self) -> None:
        pass

    def build_originatorcustomerparty(self) -> None:
        pass

    def build_taxrepresentativeparty(self) -> None:
        pass

    def build_delivery(self) -> None:
        pass

    def build_shipment(self) -> None:
        pass

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
        pass

    def build_senderparty(self) -> None:
        # ['SenderParty'] = ('cac', Party(), 'Zorunlu (1)', 'senderparty')
        senderparty_: Element = self.root.find('./' + self._cac_ns + 'SenderParty')
        self._product.senderparty = TRUBLParty().process_element(senderparty_,
                                                                 self._cbc_ns,
                                                                 self._cac_ns).name

    def build_receiverparty(self) -> None:
        # ['ReceiverParty'] = ('cac', Party(), 'Zorunlu (1)', 'receiverparty')
        receiverparty_: Element = self.root.find('./' + self._cac_ns + 'ReceiverParty')
        self._product.receiverparty = TRUBLParty().process_element(receiverparty_,
                                                                   self._cbc_ns,
                                                                   self._cac_ns).name

    def build_documentresponse(self) -> None:
        # ['DocumentResponse'] = ('cac', DocumentResponse(), 'Zorunlu (1)', 'documentresponse')
        documentresponse_: Element = self.root.find('./' + self._cac_ns + 'DocumentResponse')
        self._product.documentresponse = TRUBLDocumentResponse().process_element(documentresponse_,
                                                                                 self._cbc_ns,
                                                                                 self._cac_ns).name

    def get_document(self) -> None:
        product = self._product.save()
