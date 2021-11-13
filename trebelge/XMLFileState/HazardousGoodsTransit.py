# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class HazardousGoodsTransit(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'HazardousGoodsTransit'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): TransportEmergencyCardCode
        self._mapping['TransportEmergencyCardCode'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): PackagingCriteriaCode
        self._mapping['PackagingCriteriaCode'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): HazardousRegulationCode
        self._mapping['HazardousRegulationCode'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): InhalationToxicityZoneCode
        self._mapping['InhalationToxicityZoneCode'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): TransportAuthorizationCode
        self._mapping['TransportAuthorizationCode'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): MaximumTemperature:Temperature
        self._mapping['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..1): MinimumTemperature:Temperature
        self._mapping['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
