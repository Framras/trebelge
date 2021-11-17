# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class BillingReference(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'BillingReference'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): InvoiceDocumentReference:DocumentReference
        self._mapping['InvoiceDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..1): SelfBilledInvoiceDocumentReference:DocumentReference
        self._mapping['SelfBilledInvoiceDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..1): CreditNoteDocumentReference:DocumentReference
        self._mapping['CreditNoteDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..1): SelfBilledCreditNoteDocumentReference:DocumentReference
        self._mapping['SelfBilledCreditNoteDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..1): DebitNoteDocumentReference:DocumentReference
        self._mapping['DebitNoteDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..1): ReminderDocumentReference:DocumentReference
        self._mapping['ReminderDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..1): AdditionalDocumentReference:DocumentReference
        self._mapping['AdditionalDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli(0..n): BillingReferenceLine:BillingReferenceLine
        self._mapping['BillingReferenceLine'] = ('cac', 'BillingReferenceLine', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
