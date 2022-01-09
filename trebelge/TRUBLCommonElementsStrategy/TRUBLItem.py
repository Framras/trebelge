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
        itemname_ = element.find('./' + cbcnamespace + 'Name').text
        if itemname_ is None:
            return None
        frappedoc: dict = dict(itemname=itemname_)
        # ['Description'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Keyword'] = ('cbc', '', 'Seçimli (0...1)')
        # ['BrandName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ModelName'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['Description', 'Keyword', 'BrandName', 'ModelName']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['BuyersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'buyersitemid')
        buyersitemid_: Element = element.find('./' + cacnamespace + 'BuyersItemIdentification')
        if buyersitemid_ is not None:
            tmp = TRUBLItemIdentification().process_element(buyersitemid_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['buyersitemid'] = tmp.name
        # ['SellersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'sellersitemid')
        sellersitemid_: Element = element.find('./' + cacnamespace + 'SellersItemIdentification')
        if sellersitemid_ is not None:
            tmp = TRUBLItemIdentification().process_element(sellersitemid_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['sellersitemid'] = tmp.name
        # ['ManufacturersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'manufacturersitemid')
        manufacturersitemid_: Element = element.find('./' + cacnamespace + 'ManufacturersItemIdentification')
        if manufacturersitemid_ is not None:
            tmp = TRUBLItemIdentification().process_element(manufacturersitemid_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['manufacturersitemid'] = tmp.name
        # ['OriginCountry'] = ('cac', 'Country', 'Seçimli (0...1)', 'origincountry')
        origincountry_: Element = element.find('./' + cacnamespace + 'OriginCountry')
        if origincountry_ is not None:
            tmp = TRUBLCountry().process_element(origincountry_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['origincountry'] = tmp.name
        # ['AdditionalItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...n)', 'additionalitemid')
        additionalitemid: list = []
        additionalitemids_: list = element.findall('./' + cacnamespace + 'AdditionalItemIdentification')
        if len(additionalitemids_) != 0:
            for additionalitemid_ in additionalitemids_:
                tmp = TRUBLItemIdentification().process_element(additionalitemid_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    additionalitemid.append(tmp)
        # ['CommodityClassification'] = ('cac', 'CommodityClassification', 'Seçimli (0...n)', 'commodityclassification')
        commodityclass: list = []
        commodityclassifications_: list = element.findall('./' + cacnamespace + 'CommodityClassification')
        if len(commodityclassifications_) != 0:
            for commodityclassification_ in commodityclassifications_:
                tmp = TRUBLCommodityClassification().process_element(commodityclassification_,
                                                                     cbcnamespace,
                                                                     cacnamespace)
                if tmp is not None:
                    commodityclass.append(tmp)
        # ['ItemInstance'] = ('cac', 'ItemInstance', 'Seçimli (0...n)', 'iteminstance')
        iteminstance: list = []
        iteminstances_: list = element.findall('./' + cacnamespace + 'ItemInstance')
        if len(iteminstances_) != 0:
            for iteminstance_ in iteminstances_:
                tmp = TRUBLItemInstance().process_element(iteminstance_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    iteminstance.append(tmp)

        if len(additionalitemid) + len(commodityclass) + len(iteminstance) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(additionalitemid) != 0:
                document.additionalitemid = additionalitemid
            if len(commodityclass) != 0:
                document.commodityclass = commodityclass
            if len(iteminstance) != 0:
                document.iteminstance = iteminstance
            document.save()

        return document
