from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommodityClassification(TRUBLCommonElement):

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str):
        """
        ['ItemClassificationCode'] = ('cbc', 'itemclassificationcode', 'Zorunlu(1)')
        ['listAgencyID'] = ('', 'itemclassificationcode_listagencyid', 'Zorunlu(1)')
        ['listID'] = ('', 'itemclassificationcode_listid', 'Zorunlu(1)')
        """
        itemclassificationcode_ = element.find(cbcnamespace + 'ItemClassificationCode')
        commodityclassification: dict = {'itemclassificationcode': itemclassificationcode_.text}
        for key in itemclassificationcode_.attrib.keys():
            commodityclassification[('ItemClassificationCode_' + key).lower()] = itemclassificationcode_.attrib.get(key)

        return commodityclassification
