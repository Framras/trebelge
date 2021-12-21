from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLBuildingNumber import TRUBLBuildingNumber
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLItem(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Item'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Name'] = ('cbc', 'itemname', 'Zorunlu (1)')
        frappedoc: dict = {'itemname': element.find(cbcnamespace + 'Name').text}

        # ['Description'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Keyword'] = ('cbc', '', 'Seçimli (0...1)')
        # ['BrandName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ModelName'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['Description', 'Keyword', 'BrandName', 'ModelName']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['BuyersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)')
        # ['SellersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)')
        # ['ManufacturersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)')
        # ['OriginCountry'] = ('cac', 'Country', 'Seçimli (0...1)')

        # ['AdditionalItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...n)')
        # ['CommodityClassification'] = ('cac', 'CommodityClassification', 'Seçimli (0...n)')
        # ['ItemInstance'] = ('cac', 'ItemInstance', 'Seçimli (0...n)')
        buildingnumbers_: list = element.findall(cbcnamespace + 'BuildingNumber')
        if buildingnumbers_ is not None:
            buildingnumbers: list = []
            strategy: TRUBLCommonElement = TRUBLBuildingNumber()
            self._strategyContext.set_strategy(strategy)
            for buildingnumber in buildingnumbers_:
                buildingnumbers.append(self._strategyContext.return_element_data(buildingnumber,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
            frappedoc['buildingnumber'] = buildingnumbers

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
