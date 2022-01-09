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
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['Quantity'] = ('cbc', '', 'Seçimli (0...1)')
        quantity_: Element = element.find('./' + cbcnamespace + 'Quantity')
        if quantity_ is not None:
            if quantity_.text is not None:
                frappedoc['quantity'] = quantity_.text
                frappedoc['quantityunitcode'] = quantity_.attrib.get('unitCode')
        # ['PackagingMaterial'] = ('cbc', '', 'Seçimli (0...n)')
        packagingmaterials_: list = element.findall('./' + cbcnamespace + 'PackagingMaterial')
        if packagingmaterials_:
            packagingmaterial = list()
            for packagingmaterial_ in packagingmaterials_:
                if packagingmaterial_.text is not None:
                    packagingmaterial.append(packagingmaterial_.text)
            if len(packagingmaterial) != 0:
                frappedoc['packagingmaterial'] = packagingmaterial
        if frappedoc == {}:
            return None
        # ['ContainedPackage'] = ('cac', 'Package', 'Seçimli (0...n)')
        containedpackage = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'ContainedPackage')
        if tagelements_:
            for tagelement in tagelements_:
                tmp = TRUBLPackage().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    containedpackage.append(tmp)
        # ['GoodsItem'] = ('cac', 'GoodsItem', 'Seçimli (0...n)')
        goodsitem = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'GoodsItem')
        if tagelements_:
            for tagelement in tagelements_:
                tmp = TRUBLGoodsItem().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    goodsitem.append(tmp)
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)')
        measurementdimension = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if tagelements_:
            for tagelement in tagelements_:
                tmp = TRUBLDimension().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    measurementdimension.append(tmp)

        if len(containedpackage) + len(goodsitem) + len(measurementdimension) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(containedpackage) != 0:
                document.containedpackage = containedpackage
            if len(goodsitem) != 0:
                document.goodsitem = goodsitem
            if len(measurementdimension) != 0:
                document.measurementdimension = measurementdimension
            document.save()

        return document
