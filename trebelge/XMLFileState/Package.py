# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Package(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Package'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): ID
        self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Quantity
        self._mapping['Quantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ReturnableMaterialIndicator
        self._mapping['ReturnableMaterialIndicator'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): PackageLevelCode
        self._mapping['PackageLevelCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): PackagingTypeCode
        self._mapping['PackagingTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): PackagingMaterial
        self._mapping['PackagingMaterial'] = ('cbc', '', 'Seçimli (0...n)', False, False, True)
        # Seçimli(0..n): ContainedPackage:Package
        self._mapping['ContainedPackage'] = (
            'cac', 'Package', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): GoodsItem:GoodsItem
        self._mapping['GoodsItem'] = (
            'cac', 'GoodsItem', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): MeasurementDimension:Dimension
        self._mapping['MeasurementDimension'] = (
            'cac', 'Dimension', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
