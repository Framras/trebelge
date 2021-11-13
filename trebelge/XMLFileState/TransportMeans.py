# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class TransportMeans(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'TransportMeans'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): JourneyID
        self._mapping['JourneyID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): RegistrationNationalityID
        self._mapping['RegistrationNationalityID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): RegistrationNationality
        self._mapping['RegistrationNationality'] = ('cbc', '', 'Seçimli (0...n)', False, False, True)
        # Seçimli(0..1): DirectionCode
        self._mapping['DirectionCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TransportMeansTypeCode
        self._mapping['TransportMeansTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TradeServiceCode
        self._mapping['TradeServiceCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Stowage:Stowage
        self._mapping['Stowage'] = ('cac', 'Stowage', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..1): AirTransport:AirTransport
        self._mapping['AirTransport'] = ('cac', 'AirTransport', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..1): RoadTransport:RoadTransport
        self._mapping['RoadTransport'] = ('cac', 'RoadTransport', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..1): RailTransport:RailTransport
        self._mapping['RailTransport'] = ('cac', 'RailTransport', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..1): MaritimeTransport:MaritimeTransport
        self._mapping['MaritimeTransport'] = ('cac', 'MaritimeTransport', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..1): OwnerParty:Party
        self._mapping['OwnerParty'] = ('cac', 'Party', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..n): MeasurementDimension:Dimension
        self._mapping['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
