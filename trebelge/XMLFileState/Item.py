# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Item(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Item'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): Description
        self._mapping['Description'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Zorunlu(1): Name
        self._mapping['Name'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Seçimli(0..1): Keyword
        self._mapping['Keyword'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): BrandName
        self._mapping['BrandName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): ModelName
        self._mapping['ModelName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): BuyersItemIdentification:ItemIdentification
        self._mapping['BuyersItemIdentification'] = (
            'cac', 'ItemIdentification', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): SellersItemIdentification:ItemIdentification
        self._mapping['SellersItemIdentification'] = (
            'cac', 'ItemIdentification', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): ManufacturersItemIdentification:ItemIdentification
        self._mapping['ManufacturersItemIdentification'] = (
            'cac', 'ItemIdentification', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..n): AdditionalItemIdentification:ItemIdentification
        self._mapping['AdditionalItemIdentification'] = (
            'cac', 'ItemIdentification', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..1): OriginCountry:Country
        self._mapping['OriginCountry'] = ('cac', 'Country', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..n): CommodityClassification:CommodityClassification
        self._mapping['CommodityClassification'] = (
            'cac', 'CommodityClassification', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): ItemInstance:ItemInstance
        self._mapping['ItemInstance'] = (
            'cac', 'ItemInstance', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
