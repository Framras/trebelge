# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class BillingReferenceLine(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'BillingReferenceLine'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): Amount
        self._mapping['Amount'] = ('cbc', '', 'Seçimli (0..1)', True, True, True)
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', True, False, False)
        # Seçimli(0..n): AllowanceCharge:AllowanceCharge
        self._mapping['AllowanceCharge.'] = ('cac', 'AllowanceCharge.', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
