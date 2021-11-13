# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class ItemInstance(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'ItemInstance'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ProductTraceID
        self._mapping['ProductTraceID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ManufacturedDate
        self._mapping['ManufacturedDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ManufacturedTime
        self._mapping['ManufacturedTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): BestBeforeDate
        self._mapping['BestBeforeDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): RegistrationID
        self._mapping['RegistrationID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): SerialID
        self._mapping['SerialID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): AdditionalItemProperty:AdditionalItemProperty
        self._mapping['AdditionalItemProperty'] = (
            'cac', 'AdditionalItemProperty', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): LotIdentification:LotIdentification
        self._mapping['LotIdentification'] = (
            'cac', 'LotIdentification', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
