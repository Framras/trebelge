# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class GoodsItem(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'GoodsItem'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..n): Description
        self._mapping['Description'] = ('cbc', '', 'Seçimli(0..n)', False, False, True)
        # Seçimli(0..1): HazardousRiskIndicator
        self._mapping['HazardousRiskIndicator'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): DeclaredCustomsValueAmount
        self._mapping['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): DeclaredForCarriageValueAmount
        self._mapping['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): DeclaredStatisticsValueAmount
        self._mapping['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): FreeOnBoardValueAmount
        self._mapping['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): InsuranceValueAmount
        self._mapping['InsuranceValueAmount'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): ValueAmount
        self._mapping['ValueAmount'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False)
        # Seçimli(0..1): GrossWeightMeasure
        self._mapping['GrossWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): NetWeightMeasure
        self._mapping['NetWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): ChargeableWeightMeasure
        self._mapping['ChargeableWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): GrossVolumeMeasure
        self._mapping['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        # Seçimli(0..1): NetVolumeMeasure
        self._mapping['NetVolumeMeasure'] = ('cbc', '', 'Seçimli(0..1)', True, True, True)
        self._mapping['unitCode'] = ('', '', 'Zorunlu(1)', False, False, False)
        # Seçimli(0..1): Quantity
        self._mapping['Quantity'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): RequiredCustomsID
        self._mapping['RequiredCustomsID'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): CustomsStatusCode
        self._mapping['CustomsStatusCode'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): CustomsTariffQuantity
        self._mapping['CustomsTariffQuantity'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): CustomsImportClassifiedIndicator
        self._mapping['CustomsImportClassifiedIndicator'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): ChargeableQuantity
        self._mapping['ChargeableQuantity'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): ReturnableQuantity
        self._mapping['ReturnableQuantity'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..1): TraceID
        self._mapping['TraceID'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..n): Item:Item
        self._mapping['Item'] = ('cac', 'Item', 'Seçimli(0..n)', True, False, False)
        # Seçimli(0..n): FreightAllowanceCharge:AllowanceCharge
        self._mapping['FreightAllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli(0..n)', True, False, False)
        # Seçimli(0..n): InvoiceLine:InvoiceLine
        self._mapping['InvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli(0..n)', True, False, False)
        # Seçimli(0..n): Temperature:Temperature
        self._mapping['Temperature'] = ('cac', 'Temperature', 'Seçimli(0..n)', True, False, False)
        # Seçimli(0..1): OriginAddress:Address
        self._mapping['OriginAddress'] = ('cac', 'Address', 'Seçimli(0..1)', True, False, False)
        # Seçimli(0..n): MeasurementDimension:Dimension
        self._mapping['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
