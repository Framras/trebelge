from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommodityClassification(TRUBLCommonElement):

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ItemClassificationCode'] = ('cbc', 'itemclassificationcode', 'Zorunlu(1)')
        # ['listAgencyID'] = ('', 'itemclassificationcode_listagencyid', 'Zorunlu(1)')
        # ['listID'] = ('', 'itemclassificationcode_listid', 'Zorunlu(1)')
        itemclassificationcode_: Element = element.find(cbcnamespace + 'ItemClassificationCode')
        frappedoc: dict = {'itemclassificationcode': itemclassificationcode_.text}
        for key in itemclassificationcode_.attrib.keys():
            frappedoc[('ItemClassificationCode_' + key).lower()] = itemclassificationcode_.attrib.get(key)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
