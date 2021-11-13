# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class RoadTransport(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'RoadTransport'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): LicensePlateID
        self._mapping['LicensePlateID'] = ('cbc', '', 'Zorunlu (1)', True, True, True)
        self._mapping['schemeID'] = ('', '', 'Seçimli (0...1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
