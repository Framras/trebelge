# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Response(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Response'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ReferenceID
        self._mapping['ReferenceID'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Seçimli(0..1): ResponseCode
        self._mapping['ResponseCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): Description
        self._mapping['Description'] = ('cbc', '', 'Seçimli (0...n)', False, False, True)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
