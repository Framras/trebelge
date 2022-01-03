from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommodityClassification(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CommodityClassification'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        itemclassificationcode_: Element = element.find('./' + cbcnamespace + 'ItemClassificationCode')
        # ['ItemClassificationCode'] = ('cbc', 'itemclassificationcode', 'Zorunlu(1)')
        if itemclassificationcode_.text is None:
            return None
        frappedoc: dict = dict(itemclassificationcode=itemclassificationcode_.text)
        for key in itemclassificationcode_.attrib.keys():
            meta = frappe.get_meta(self._frappeDoctype)
            if meta.has_field(key.lower()):
                frappedoc[key.lower()] = itemclassificationcode_.attrib.get(key)
            else:
                frappe.log_error(key + ' not found as field in ' + self._frappeDoctype)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
