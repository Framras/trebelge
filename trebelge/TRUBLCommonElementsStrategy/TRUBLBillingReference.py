from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReferenceLine import TRUBLBillingReferenceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference


class TRUBLBillingReference(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR BillingReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['InvoiceDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'InvoiceDocumentReference')
        if tagelement_ is not None:
            tmp = TRUBLDocumentReference().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['invoice'] = tmp.name
        # ['SelfBilledInvoiceDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'SelfBilledInvoiceDocumentReference')
        if tagelement_ is not None:
            tmp = TRUBLDocumentReference().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['selfbilledinvoice'] = tmp.name
        # ['CreditNoteDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'CreditNoteDocumentReference')
        if tagelement_ is not None:
            tmp = TRUBLDocumentReference().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['creditnote'] = tmp.name
        # ['SelfBilledCreditNoteDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'SelfBilledCreditNoteDocumentReference')
        if tagelement_ is not None:
            tmp = TRUBLDocumentReference().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['selfbilledcreditnote'] = tmp.name
        # ['DebitNoteDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'DebitNoteDocumentReference')
        if tagelement_ is not None:
            tmp = TRUBLDocumentReference().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['debitnote'] = tmp.name
        # ['ReminderDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'ReminderDocumentReference')
        if tagelement_ is not None:
            tmp = TRUBLDocumentReference().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['reminder'] = tmp.name
        # ['AdditionalDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'AdditionalDocumentReference')
        if tagelement_ is not None:
            tmp = TRUBLDocumentReference().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['additionaldocument'] = tmp.name
        if frappedoc == {}:
            return None
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        billingreferencelines = list()
        # ['BillingReferenceLine'] = ('cac', 'BillingReferenceLine', 'Seçimli (0...n)')
        billingreferencelines_: list = element.findall('./' + cacnamespace + 'BillingReferenceLine')
        if len(billingreferencelines_) != 0:
            for billingreferenceline_ in billingreferencelines_:
                tmp = TRUBLBillingReferenceLine().process_element(billingreferenceline_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    billingreferencelines.append(tmp.name)
        if len(billingreferencelines) != 0:
            doc_append = document.append("billingreferenceline", {})
            for billingreferenceline in billingreferencelines:
                doc_append.billingreferenceline = billingreferenceline
                document.save()
        return document
