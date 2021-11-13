# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class TransportHandlingUnit(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'TransportHandlingUnit'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): TransportHandlingUnitTypeCode
        self._mapping['TransportHandlingUnitTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): HandlingCode
        self._mapping['HandlingCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): HandlingInstructions
        self._mapping['HandlingInstructions'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): HazardousRiskIndicator
        self._mapping['HazardousRiskIndicator'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TotalGoodsItemQuantity
        self._mapping['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TotalPackageQuantity
        self._mapping['TotalPackageQuantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): DamageRemarks
        self._mapping['DamageRemarks'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TraceID
        self._mapping['TraceID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): ActualPackage:Package
        self._mapping['ActualPackage'] = ('cac', 'Package', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): TransportEquipment:TransportEquipment
        self._mapping['TransportEquipment'] = ('cac', 'TransportEquipment', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): TransportMeans:TransportMeans
        self._mapping['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): HazardousGoodsTransit:HazardousGoodsTransit
        self._mapping['HazardousGoodsTransit'] = ('cac', 'HazardousGoodsTransit', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): MeasurementDimension:Dimension
        self._mapping['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..1): MinimumTemperature:Temperature
        self._mapping['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): MaximumTemperature:Temperature
        self._mapping['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): FloorSpaceMeasurementDimension:Dimension
        self._mapping['FloorSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): PalletSpaceMeasurementDimension:Dimension
        self._mapping['PalletSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..n): ShipmentDocumentReference:DocumentReference
        self._mapping['ShipmentDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): CustomsDeclaration:CustomsDeclaration
        self._mapping['CustomsDeclaration'] = ('cac', 'CustomsDeclaration', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
