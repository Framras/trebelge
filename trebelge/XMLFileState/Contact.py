# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Contact(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Contact'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Name
        self._mapping['Name'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Telephone
        self._mapping['Telephone'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Telefax
        self._mapping['Telefax'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ElectronicMail
        self._mapping['ElectronicMail'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Note
        self._mapping['Note'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): OtherCommunication:Communication
        self._mapping['OtherCommunication'] = ('cac', 'Communication', 'Seçimli(0..n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
