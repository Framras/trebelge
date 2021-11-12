# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class BillingReference(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['InvoiceDocumentReference'] = (
            'cac', 'InvoiceDocumentReference', 'Seçimli (0..1)', True, False, False)
        self._mapping['SelfBilledInvoiceDocumentReference'] = (
            'cac', 'SelfBilledInvoiceDocumentReference', 'Seçimli (0..1)', True, False, False)
        self._mapping['CreditNoteDocumentReference'] = (
            'cac', 'CreditNoteDocumentReference', 'Seçimli (0..1)', True, False, False)
        self._mapping['SelfBilledCreditNoteDocumentReference'] = (
            'cac', 'SelfBilledCreditNoteDocumentReference', 'Seçimli (0..1)', True, False, False)
        self._mapping['DebitNoteDocumentReference'] = (
            'cac', 'DebitNoteDocumentReference', 'Seçimli (0..1)', True, False, False)
        self._mapping['ReminderDocumentReference'] = (
            'cac', 'ReminderDocumentReference', 'Seçimli (0..1)', True, False, False)
        self._mapping['AdditionalDocumentReference'] = (
            'cac', 'AdditionalDocumentReference', 'Seçimli (0..1)', True, False, False)
        self._mapping['BillingReferenceLine'] = ('cac', 'BillingReferenceLine', 'Seçimli (0...n)', True, False, False)
        self._mapping['BillingReference'] = ('cac', 'BillingReference', '', False, False, True)
