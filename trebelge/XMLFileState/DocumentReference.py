# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class DocumentReference(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'AdditionalDocumentReference'

    def find_ebelge_status(self):
        pass

    def define_mappings(self, tag: str, initiator: AbstractXMLFileState):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Zorunlu(1): IssueDate
        self._mapping['IssueDate'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Seçimli(0..1) : DocumentTypeCode
        self._mapping['DocumentTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : DocumentType
        self._mapping['DocumentType'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n) : DocumentDescription
        self._mapping['DocumentDescription'] = ('cbc', '', 'Seçimli(0..n)', False, False, True)
        # Seçimli(0..1): Attachment
        self._mapping['Attachment'] = ('cac', 'Attachment', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): ValidityPeriod:Period
        self._mapping['ValidityPeriod'] = ('cac', 'Period', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): IssuerParty:Party
        self._mapping['IssuerParty'] = ('cac', 'Party', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)

    def read_element_by_action(self, event: str, element: ET.Element):
        pass
