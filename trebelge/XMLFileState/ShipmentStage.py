# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class ShipmentStage(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'ShipmentStage'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TransportModeCode
        self._mapping['TransportModeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TransportMeansTypeCode
        self._mapping['TransportMeansTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): TransitDirectionCode
        self._mapping['TransitDirectionCode'] = ('cbc', '', 'Seçimli (0...n)', False, False, True)
        # Seçimli(0..1): Instructions
        self._mapping['Instructions'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TransitPeriod:Period
        self._mapping['TransitPeriod'] = (
            'cac', 'Period', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): TransportMeans:TransportMeans
        self._mapping['TransportMeans'] = (
            'cac', 'TransportMeans', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..n): DriverPerson:Person
        self._mapping['DriverPerson'] = (
            'cac', 'Person', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
