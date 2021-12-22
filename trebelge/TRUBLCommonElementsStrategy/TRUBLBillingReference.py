from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLBillingReferenceLine import TRUBLBillingReferenceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference


class TRUBLBillingReference(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR BillingReference'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

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
            tagelement_: Element = element.find(cacnamespace + element_.get('Tag'))
            if tagelement_:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]
        # ['BillingReferenceLine'] = ('cac', 'BillingReferenceLine', 'Seçimli (0...n)')
        cacsecimli0n: list = \
            [{'Tag': 'BillingReferenceLine', 'strategy': TRUBLBillingReferenceLine(),
              'fieldName': 'billingreferenceline'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall(cacnamespace + element_.get('Tag'))
            if tagelements_:
                tagelements: list = []
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                for tagelement in tagelements_:
                    tagelements.append(self._strategyContext.return_element_data(tagelement,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
