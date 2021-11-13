# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Shipment(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Shipment'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): HandlingCode
        self._mapping['HandlingCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): HandlingInstructions
        self._mapping['HandlingInstructions'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): GrossWeightMeasure
        self._mapping['GrossWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): NetWeightMeasure
        self._mapping['NetWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): GrossVolumeMeasure
        self._mapping['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): NetVolumeMeasure
        self._mapping['NetVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TotalGoodsItemQuantity
        self._mapping['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TotalTransportHandlingUnitQuantity
        self._mapping['TotalTransportHandlingUnitQuantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): InsuranceValueAmount
        self._mapping['InsuranceValueAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): DeclaredCustomsValueAmount
        self._mapping['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): DeclaredForCarriageValueAmount
        self._mapping['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): DeclaredStatisticsValueAmount
        self._mapping['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): FreeOnBoardValueAmount
        self._mapping['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..n): SpecialInstructions
        self._mapping['SpecialInstructions'] = ('cbc', '', 'Seçimli (0...n)', False, False, True)
        # Seçimli(0..n): GoodsItem:GoodsItem
        self._mapping['GoodsItem'] = (
            'cac', 'GoodsItem', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): ShipmentStage:ShipmentStage
        self._mapping['ShipmentStage'] = (
            'cac', 'ShipmentStage', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..1): Delivery:Delivery
        self._mapping['Delivery'] = (
            'cac', 'Delivery', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..n): TransportHandlingUnit:TransportHandlingUnit
        self._mapping['TransportHandlingUnit'] = (
            'cac', 'TransportHandlingUnit', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..1): ReturnAddress:Address
        self._mapping['ReturnAddress'] = (
            'cac', 'Address', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): FirstArrivalPortLocation:Location
        self._mapping['FirstArrivalPortLocation'] = (
            'cac', 'Location', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): LastExitPortLocation:Location
        self._mapping['LastExitPortLocation'] = (
            'cac', 'Location', 'Seçimli (0...1)', True, False, False)
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False)
        self._mapping['unitCode'] = ('', '', 'Zorunlu(1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
