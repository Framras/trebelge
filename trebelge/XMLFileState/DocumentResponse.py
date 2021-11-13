# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class DocumentResponse(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'DocumentResponse'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): Response:Response
        self._mapping['Response'] = ('cac', 'Response', 'Zorunlu(1)', True, False, False)
        # Zorunlu(1): DocumentReference:DocumentReference
        self._mapping['DocumentReference'] = ('cac', 'DocumentReference', 'Zorunlu(1)', True, False, False)
        # Seçimli(0..1): LineResponse:LineResponse
        self._mapping['LineResponse'] = ('cac', 'LineResponse', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
