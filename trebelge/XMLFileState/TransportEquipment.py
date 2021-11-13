# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class TransportEquipment(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'TransportEquipment'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): TransportEquipmentTypeCode
        self._mapping['TransportEquipmentTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Description
        self._mapping['Description'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # schemeID
        self._mapping['schemeID'] = ('', '', 'Seçimli (0...1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
