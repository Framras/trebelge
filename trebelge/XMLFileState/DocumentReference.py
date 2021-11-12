# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class DocumentReference(AbstractXMLFileState):
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
        self._mapping['ID'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        self._mapping['IssueDate'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        self._mapping['DocumentTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['DocumentType'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['DocumentDescription'] = ('cbc', '', 'Seçimli(0..n)', False, False, True)
        self._mapping['Attachment'] = ('cac', 'Attachment', 'Seçimli (0...1)', True, False, False)
        self._mapping['ValidityPeriod'] = ('cac', 'ValidityPeriod', 'Seçimli (0...1)', True, False, False)
        self._mapping['IssuerParty'] = ('cac', 'IssuerParty', 'Seçimli (0...1)', True, False, False)
        self._mapping['DocumentReference'] = ('cac', 'DocumentReference', '', False, False, True)
