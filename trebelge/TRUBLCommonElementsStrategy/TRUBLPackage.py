from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLGoodsItem import TRUBLGoodsItem


class TRUBLPackage(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Package'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ReturnableMaterialIndicator'] = ('cbc', '', 'Seçimli (0...1)')
        # ['PackageLevelCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['PackagingTypeCode'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'ReturnableMaterialIndicator', 'PackageLevelCode', 'PackagingTypeCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['Quantity'] = ('cbc', '', 'Seçimli (0...1)')
        quantity_: Element = element.find('./' + cbcnamespace + 'Quantity')
        if quantity_:
            frappedoc['quantity'] = quantity_.text
            frappedoc['quantityunitcode'] = quantity_.attrib.get('unitCode')
        # ['PackagingMaterial'] = ('cbc', '', 'Seçimli (0...n)')
        packagingmaterials_: list = element.findall('./' + cbcnamespace + 'PackagingMaterial')
        if packagingmaterials_:
            packagingmaterial: list = []
            for packagingmaterial_ in packagingmaterials_:
                packagingmaterial.append(packagingmaterial_.text)
            frappedoc['packagingmaterial'] = packagingmaterial
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['ContainedPackage'] = ('cac', 'Package', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'ContainedPackage')
        if tagelements_:
            tagelements: list = []
            for tagelement in tagelements_:
                tagelements.append(TRUBLPackage().process_element(tagelement,
                                                                  cbcnamespace,
                                                                  cacnamespace))
            document.containedpackage = tagelements
            document.save()
        # ['GoodsItem'] = ('cac', 'GoodsItem', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'GoodsItem')
        if tagelements_:
            tagelements: list = []
            for tagelement in tagelements_:
                tagelements.append(TRUBLGoodsItem().process_element(tagelement,
                                                                    cbcnamespace,
                                                                    cacnamespace))
            document.goodsitem = tagelements
            document.save()
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if tagelements_:
            tagelements: list = []
            for tagelement in tagelements_:
                tagelements.append(TRUBLDimension().process_element(tagelement,
                                                                    cbcnamespace,
                                                                    cacnamespace))
            document.measurementdimension = tagelements
            document.save()

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
