from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialAccount import TRUBLFinancialAccount


class TRUBLBillingReference(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportMeans'
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
        # ['BillingReferenceLine'] = ('cac', 'BillingReferenceLine', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
