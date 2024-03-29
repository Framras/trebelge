from datetime import datetime
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentResponse import TRUBLDocumentResponse
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLApplicationResponseBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    _frappeDoctype: str = 'UBL TR Application Response'

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
            applicationresponse_ = frappe.new_doc(self._frappeDoctype)
            applicationresponse_.uuid = self._uuid
            applicationresponse_.ublversionid = self.root.find('./' + self._cbc_ns + 'UBLVersionID').text
            applicationresponse_.customizationid = self.root.find('./' + self._cbc_ns + 'CustomizationID').text
            applicationresponse_.profileid = self.root.find('./' + self._cbc_ns + 'ProfileID').text
            applicationresponse_.id = self.root.find('./' + self._cbc_ns + 'ID').text
            applicationresponse_.issuedate = self.root.find('./' + self._cbc_ns + 'IssueDate').text
            applicationresponse_.insert()
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
        tmp = TRUBLDocumentResponse().process_element(documentresponse_,
                                                      self._cbc_ns,
                                                      self._cac_ns)
        if tmp is not None:
            self._product.documentresponse = tmp.name

    def build_discrepancyresponse(self) -> None:
        pass

    def build_statementdocumentreference(self) -> None:
        pass

    def build_payeeparty(self) -> None:
        pass

    def build_deliveryterms(self) -> None:
        pass

    def build_creditnoteline(self) -> None:
        pass

    def get_document(self) -> None:
        self._product.save()
