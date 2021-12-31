from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLItemIdentification(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ItemIdentification'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        id_ = element.find('./' + cbcnamespace + 'ID')
        if id_:
            frappedoc['id'] = id_.text
        else:
            frappe.log_error('id not provided for ' + element.tag, 'TRUBLItemIdentification')
            frappedoc['id'] = str('-')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
