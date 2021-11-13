# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Despatch(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Despatch'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ActualDespatchDate
        self._mapping['ActualDespatchDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ActualDespatchTime
        self._mapping['ActualDespatchTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Instructions
        self._mapping['Instructions'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): DespatchAddress:Address
        self._mapping['DespatchAddress'] = ('cac', 'Address', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): DespatchParty:Party
        self._mapping['DespatchParty'] = ('cac', 'Party', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): Contact:Contact
        self._mapping['Contact'] = ('cac', 'Contact', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): EstimatedDespatchPeriod:Period
        self._mapping['EstimatedDespatchPeriod'] = ('cac', 'Period', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
