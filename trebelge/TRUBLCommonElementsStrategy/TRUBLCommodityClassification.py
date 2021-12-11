from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommodityClassification(TRUBLCommonElement):

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['ItemClassificationCode'] = ('cbc', 'itemclassificationcode', 'Zorunlu(1)')
        # ['listAgencyID'] = ('', 'itemclassificationcode_listagencyid', 'Zorunlu(1)')
        # ['listID'] = ('', 'itemclassificationcode_listid', 'Zorunlu(1)')
        itemclassificationcode_ = element.find(cbcnamespace + 'ItemClassificationCode')
        frappedoc: dict = {'itemclassificationcode': itemclassificationcode_.text}
        for key in itemclassificationcode_.attrib.keys():
            frappedoc[('ItemClassificationCode_' + key).lower()] = itemclassificationcode_.attrib.get(key)

        if not frappe.get_all(self._frappeDoctype, filters=frappedoc):
            pass
        else:
            newfrappedoc = frappedoc
            newfrappedoc['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newfrappedoc)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=frappedoc)
