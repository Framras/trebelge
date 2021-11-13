# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Signature(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Signature'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Zorunlu(1): SignatoryParty:Party
        self._mapping['SignatoryParty'] = (
            'cac', 'Party', 'Zorunlu(1)', True, False, False)
        # Zorunlu(1): DigitalSignatureAttachment:Attachment
        self._mapping['DigitalSignatureAttachment'] = (
            'cac', 'Attachment', 'Zorunlu(1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
