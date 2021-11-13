# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Person(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Person'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): FirstName
        self._mapping['FirstName'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Zorunlu(1): FamilyName
        self._mapping['FamilyName'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): Title
        self._mapping['Title'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): MiddleName
        self._mapping['MiddleName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): NameSuffix
        self._mapping['NameSuffix'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): NationalityID
        self._mapping['NationalityID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): FinancialAccount:FinancialAccount
        self._mapping['FinancialAccount'] = (
            'cac', 'FinancialAccount', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): IdentityDocumentReference:DocumentReference
        self._mapping['IdentityDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
