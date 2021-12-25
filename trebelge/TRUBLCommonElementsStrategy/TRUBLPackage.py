from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLGoodsItem import TRUBLGoodsItem


class TRUBLPackage(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Package'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ReturnableMaterialIndicator'] = ('cbc', '', 'Seçimli (0...1)')
        # ['PackageLevelCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['PackagingTypeCode'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'ReturnableMaterialIndicator', 'PackageLevelCode', 'PackagingTypeCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
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
        # ['ContainedPackage'] = ('cac', 'Package', 'Seçimli (0...n)')
        # ['GoodsItem'] = ('cac', 'GoodsItem', 'Seçimli (0...n)')
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)')
        cacsecimli0n: list = \
            [{'Tag': 'ContainedPackage', 'strategy': TRUBLPackage(), 'fieldName': 'containedpackage'},
             {'Tag': 'GoodsItem', 'strategy': TRUBLGoodsItem(), 'fieldName': 'goodsitem'},
             {'Tag': 'MeasurementDimension', 'strategy': TRUBLDimension(), 'fieldName': 'measurementdimension'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall('./' + cacnamespace + element_.get('Tag'))
            if tagelements_:
                tagelements: list = []
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                for tagelement in tagelements_:
                    tagelements.append(self._strategyContext.return_element_data(tagelement,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
