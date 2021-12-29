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
        # ['BuyersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'buyersitemid')
        buyersitemid_: Element = element.find('./' + cacnamespace + 'BuyersItemIdentification')
        if buyersitemid_:
            frappedoc['buyersitemid'] = TRUBLItemIdentification().process_element(buyersitemid_,
                                                                                  cbcnamespace,
                                                                                  cacnamespace).name
        # ['SellersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'sellersitemid')
        sellersitemid_: Element = element.find('./' + cacnamespace + 'SellersItemIdentification')
        if sellersitemid_:
            frappedoc['sellersitemid'] = TRUBLItemIdentification().process_element(sellersitemid_,
                                                                                   cbcnamespace,
                                                                                   cacnamespace).name
        # ['ManufacturersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'manufacturersitemid')
        manufacturersitemid_: Element = element.find('./' + cacnamespace + 'ManufacturersItemIdentification')
        if manufacturersitemid_:
            frappedoc['manufacturersitemid'] = TRUBLItemIdentification().process_element(manufacturersitemid_,
                                                                                         cbcnamespace,
                                                                                         cacnamespace).name
        # ['OriginCountry'] = ('cac', 'Country', 'Seçimli (0...1)', 'origincountry')
        origincountry_: Element = element.find('./' + cacnamespace + 'OriginCountry')
        if origincountry_:
            frappedoc['origincountry'] = TRUBLCountry().process_element(origincountry_,
                                                                        cbcnamespace,
                                                                        cacnamespace).name
        document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['AdditionalItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...n)', 'additionalitemid')
        additionalitemids_: list = element.findall('./' + cacnamespace + 'AdditionalItemIdentification')
        if additionalitemids_:
            additionalitemid: list = []
            for additionalitemid_ in additionalitemids_:
                additionalitemid.append(TRUBLItemIdentification().process_element(additionalitemid_,
                                                                                  cbcnamespace,
                                                                                  cacnamespace))
            document.db_set('additionalitemid', additionalitemid)
            document.save()
        # ['CommodityClassification'] = ('cac', 'CommodityClassification', 'Seçimli (0...n)', 'commodityclassification')
        commodityclassifications_: list = element.findall('./' + cacnamespace + 'CommodityClassification')
        if commodityclassifications_:
            commodityclass: list = []
            for commodityclassification_ in commodityclassifications_:
                commodityclass.append(TRUBLCommodityClassification().process_element(commodityclassification_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace))
            document.db_set('commodityclass', commodityclass)
            document.save()
        # ['ItemInstance'] = ('cac', 'ItemInstance', 'Seçimli (0...n)', 'iteminstance')
        iteminstances_: list = element.findall('./' + cacnamespace + 'ItemInstance')
        if iteminstances_:
            iteminstance: list = []
            for iteminstance_ in iteminstances_:
                iteminstance.append(TRUBLItemInstance().process_element(iteminstance_,
                                                                        cbcnamespace,
                                                                        cacnamespace))
            document.db_set('iteminstance', iteminstance)
            document.save()

        return document
