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
        # ['SelfBilledInvoiceDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        # ['CreditNoteDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        # ['SelfBilledCreditNoteDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        # ['DebitNoteDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        # ['ReminderDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        # ['AdditionalDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0..1)')
        cacsecimli01: list = \
            [{'Tag': 'InvoiceDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'invoicedocumentreference'},
             {'Tag': 'SelfBilledInvoiceDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'selfbilledinvoicedocumentreference'},
             {'Tag': 'CreditNoteDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'creditnotedocumentreference'},
             {'Tag': 'SelfBilledCreditNoteDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'selfbilledcreditnotedocumentreference'},
             {'Tag': 'DebitNoteDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'debitnotedocumentreference'},
             {'Tag': 'ReminderDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'reminderdocumentreference'},
             {'Tag': 'AdditionalDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'additionaldocumentreference'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_:
                frappedoc[element_.get('fieldName')] = element_.get('strategy').process_element(tagelement_,
                                                                                                cbcnamespace,
                                                                                                cacnamespace).name
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['BillingReferenceLine'] = ('cac', 'BillingReferenceLine', 'Seçimli (0...n)')
        billingreferencelines_: list = element.findall('./' + cacnamespace + 'BillingReferenceLine')
        if len(billingreferencelines_) != 0:
            billingreferencelines: list = []
            for billingreferenceline_ in billingreferencelines_:
                billingreferencelines.append(TRUBLBillingReferenceLine().process_element(billingreferenceline_,
                                                                                         cbcnamespace,
                                                                                         cacnamespace))
            document.billingreferenceline = billingreferencelines
            document.save()

        return document
