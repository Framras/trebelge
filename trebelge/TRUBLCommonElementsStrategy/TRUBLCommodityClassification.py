from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommodityClassification(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CommodityClassification'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        itemclassificationcode_: Element = element.find(cbcnamespace + 'ItemClassificationCode')
        # ['ItemClassificationCode'] = ('cbc', 'itemclassificationcode', 'Zorunlu(1)')
        # ['listAgencyID'] = ('', 'itemclassificationcode_listagencyid', 'Zorunlu(1)')
        # ['listID'] = ('', 'itemclassificationcode_listid', 'Zorunlu(1)')
        frappedoc: dict = {'itemclassificationcode': itemclassificationcode_.text,
                           'listagencyid': itemclassificationcode_.attrib.get('listAgencyID'),
                           'listid': itemclassificationcode_.attrib.get('listID')}

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
