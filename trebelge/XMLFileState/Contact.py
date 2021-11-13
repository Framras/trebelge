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
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Name'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Telephone'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Telefax'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['ElectronicMail'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Note'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['OtherCommunication'] = ('cac', 'OtherCommunication', 'Seçimli(0..n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
