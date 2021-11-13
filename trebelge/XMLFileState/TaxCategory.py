# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class TaxCategory(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'TaxCategory'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): Name
        self._mapping['Name'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TaxExemptionReasonCode
        self._mapping['TaxExemptionReasonCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TaxExemptionReason
        self._mapping['TaxExemptionReason'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Zorunlu(1): TaxScheme:TaxScheme
        self._mapping['TaxScheme'] = ('cac', 'TaxScheme', 'Zorunlu(1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
