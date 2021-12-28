from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommodityClassification import TRUBLCommodityClassification
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCountry import TRUBLCountry
from trebelge.TRUBLCommonElementsStrategy.TRUBLItemIdentification import TRUBLItemIdentification
from trebelge.TRUBLCommonElementsStrategy.TRUBLItemInstance import TRUBLItemInstance


class TRUBLItem(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Item'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Name'] = ('cbc', 'itemname', 'Zorunlu (1)')
        frappedoc: dict = {'itemname': element.find('./' + cbcnamespace + 'Name').text}
        # ['Description'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Keyword'] = ('cbc', '', 'Seçimli (0...1)')
        # ['BrandName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ModelName'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['Description', 'Keyword', 'BrandName', 'ModelName']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['BuyersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)')
        # ['SellersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)')
        # ['ManufacturersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)')
        # ['OriginCountry'] = ('cac', 'Country', 'Seçimli (0...1)')
        cacsecimli01: list = \
            [{'Tag': 'BuyersItemIdentification', 'strategy': TRUBLItemIdentification(),
              'fieldName': 'buyersitemidentification'},
             {'Tag': 'SellersItemIdentification', 'strategy': TRUBLItemIdentification(),
              'fieldName': 'sellersitemidentification'},
             {'Tag': 'ManufacturersItemIdentification', 'strategy': TRUBLItemIdentification(),
              'fieldName': 'manufacturersitemidentification'},
             {'Tag': 'OriginCountry', 'strategy': TRUBLCountry(), 'fieldName': 'origincountry'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_:
                frappedoc[element_.get('fieldName')] = [element_.get('strategy').process_element(tagelement_,
                                                                                                 cbcnamespace,
                                                                                                 cacnamespace)]
        # ['AdditionalItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...n)')
        # ['CommodityClassification'] = ('cac', 'CommodityClassification', 'Seçimli (0...n)')
        # ['ItemInstance'] = ('cac', 'ItemInstance', 'Seçimli (0...n)')
        cacsecimli0n: list = \
            [{'Tag': 'AdditionalItemIdentification', 'strategy': TRUBLItemIdentification(),
              'fieldName': 'additionalitemidentification'},
             {'Tag': 'CommodityClassification', 'strategy': TRUBLCommodityClassification(),
              'fieldName': 'commodityclassification'},
             {'Tag': 'ItemInstance', 'strategy': TRUBLItemInstance(), 'fieldName': 'iteminstance'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall('./' + cacnamespace + element_.get('Tag'))
            if tagelements_:
                tagelements: list = []
                for tagelement in tagelements_:
                    tagelements.append(element_.get('strategy').process_element(tagelement,
                                                                                cbcnamespace,
                                                                                cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
