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
        # Mal/hizmet adı serbest metin olarak girilir.
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
        # Alıcının mal/hizmete verdiği
        # tanımlama bilgisi girilir.
        buyersitemid_: Element = element.find('./' + cacnamespace + 'BuyersItemIdentification')
        if buyersitemid_ is not None:
            tmp = TRUBLItemIdentification().process_element(buyersitemid_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['buyersitemid'] = tmp.name
        # ['SellersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'sellersitemid')
        # Satıcının mal/hizmete verdiği
        # tanımlama bilgisi girilir.
        sellersitemid_: Element = element.find('./' + cacnamespace + 'SellersItemIdentification')
        if sellersitemid_ is not None:
            tmp = TRUBLItemIdentification().process_element(sellersitemid_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['sellersitemid'] = tmp.name
        # ['ManufacturersItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...1)', 'manufacturersitemid')
        # Üreticinin mal/hizmete
        # verdiği tanımlama bilgisi girilir.
        manufacturersitemid_: Element = element.find('./' + cacnamespace + 'ManufacturersItemIdentification')
        if manufacturersitemid_ is not None:
            tmp = TRUBLItemIdentification().process_element(manufacturersitemid_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['manufacturersitemid'] = tmp.name
        # ['OriginCountry'] = ('cac', 'Country', 'Seçimli (0...1)', 'origincountry')
        # Menşei bilgisi girilebilir.
        origincountry_: Element = element.find('./' + cacnamespace + 'OriginCountry')
        if origincountry_ is not None:
            tmp = TRUBLCountry().process_element(origincountry_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['origincountry'] = tmp.name
        # ['AdditionalItemIdentification'] = ('cac', 'ItemIdentification', 'Seçimli (0...n)', 'additionalitemid')
        # Mal/hizmet için diğer
        # kullanılabilecek sınıflandırma bilgileri girilebilir.
        additionalitemids = list()
        additionalitemids_: list = element.findall('./' + cacnamespace + 'AdditionalItemIdentification')
        if len(additionalitemids_) != 0:
            for additionalitemid_ in additionalitemids_:
                tmp = TRUBLItemIdentification().process_element(additionalitemid_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    additionalitemids.append(tmp)
        # ['CommodityClassification'] = ('cac', 'CommodityClassification', 'Seçimli (0...n)', 'commodityclassification')
        # Emtia sınıflandırma bilgisi girilir.
        commodityclassifications = list()
        commodityclassifications_: list = element.findall('./' + cacnamespace + 'CommodityClassification')
        if len(commodityclassifications_) != 0:
            for commodityclassification_ in commodityclassifications_:
                tmp = TRUBLCommodityClassification().process_element(commodityclassification_,
                                                                     cbcnamespace,
                                                                     cacnamespace)
                if tmp is not None:
                    commodityclassifications.append(tmp)
        # ['ItemInstance'] = ('cac', 'ItemInstance', 'Seçimli (0...n)', 'iteminstance')
        # Parti lot bilgisi, ürün takip numarası, üretim
        # zamanı, seri numarası ve kayıt numarası gibi bilgiler
        # girilebilir.
        iteminstances = list()
        iteminstances_: list = element.findall('./' + cacnamespace + 'ItemInstance')
        if len(iteminstances_) != 0:
            for iteminstance_ in iteminstances_:
                tmp = TRUBLItemInstance().process_element(iteminstance_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    iteminstances.append(tmp)

        if len(additionalitemids) + len(commodityclassifications) + len(iteminstances) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(additionalitemids) != 0:
                document.additionalitemid = additionalitemids
            if len(commodityclassifications) != 0:
                document.commodityclass = commodityclassifications
            if len(iteminstances) != 0:
                document.iteminstance = iteminstances
            document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
