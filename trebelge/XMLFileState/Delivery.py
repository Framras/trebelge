# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Delivery(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Delivery'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Quantity
        self._mapping['Quantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ActualDeliveryDate
        self._mapping['ActualDeliveryDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ActualDeliveryTime
        self._mapping['ActualDeliveryTime'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): LatestDeliveryDate
        self._mapping['LatestDeliveryDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): LatestDeliveryTime
        self._mapping['LatestDeliveryTime'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): TrackingID
        self._mapping['TrackingID'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): DeliveryAddress:Address
        self._mapping['DeliveryAddress'] = ('cac', 'Address', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): AlternativeDeliveryLocation:Location
        self._mapping['AlternativeDeliveryLocation'] = ('cac', 'Location', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): EstimatedDeliveryPeriod:Period
        self._mapping['EstimatedDeliveryPeriod'] = ('cac', 'Period', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): CarrierParty:Party
        self._mapping['CarrierParty'] = ('cac', 'Party', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): DeliveryParty:Party
        self._mapping['DeliveryParty'] = ('cac', 'Party', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): Despatch:Despatch
        self._mapping['Despatch'] = ('cac', 'Despatch', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..n): DeliveryTerms:DeliveryTerms
        self._mapping['DeliveryTerms'] = ('cac', 'DeliveryTerms', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..1): Shipment:Shipment
        self._mapping['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
