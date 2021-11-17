# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Attachment(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Attachment'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli (0..1): ExternalReference:ExternalReference
        self._mapping['ExternalReference'] = ('cac', 'ExternalReference', 'Seçimli (0..1)', True, False, False)
        # Seçimli (0..1): EmbeddedDocumentBinaryObject
        self._mapping['EmbeddedDocumentBinaryObject'] = (
            'cbc', '', 'Seçimli (0..1)', True, True, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
