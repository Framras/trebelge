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
        # Seçimli(0..1) : ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : Postbox
        self._mapping['Postbox'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : Room
        self._mapping['Room'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : StreetName
        self._mapping['StreetName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : BlockName
        self._mapping['BlockName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : BuildingName
        self._mapping['BuildingName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n) : BuildingNumber
        self._mapping['BuildingNumber'] = ('cbc', '', 'Seçimli(0..n)', False, False, True)
        # Zorunlu(1): CitySubdivisionName
        self._mapping['CitySubdivisionName'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Zorunlu(1): CityName
        self._mapping['CityName'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1) : PostalZone
        self._mapping['PostalZone'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : Region
        self._mapping['Region'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1) : District
        self._mapping['District'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Zorunlu(1): Country
        self._mapping['Country'] = ('cac', '', 'Zorunlu(1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
