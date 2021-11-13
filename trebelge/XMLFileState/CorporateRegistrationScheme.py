# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class CorporateRegistrationScheme(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'CorporateRegistrationScheme'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Name'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['CorporateRegistrationTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['JurisdictionRegionAddress'] = (
            'cac', 'JurisdictionRegionAddress', 'Seçimli(0..n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
