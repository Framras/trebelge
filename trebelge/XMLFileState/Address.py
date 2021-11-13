# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Address(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Address'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Postbox'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Room'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['StreetName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['BlockName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['BuildingName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['BuildingNumber'] = ('cbc', '', 'Seçimli(0..n)', False, False, True)
        self._mapping['CitySubdivisionName'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        self._mapping['CityName'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        self._mapping['PostalZone'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Region'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['District'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Country'] = ('cac', '', 'Zorunlu(1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
