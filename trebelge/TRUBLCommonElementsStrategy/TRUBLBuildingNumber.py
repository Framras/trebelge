from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLBuildingNumber(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR BuildingNumber'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        buildingnumber = element.text
        if buildingnumber:
            frappedoc['buildingnumber'] = buildingnumber
        else:
            frappe.log_error('buildingnumber not provided for ' + element.tag, 'TRUBLBuildingNumber')
            frappedoc['buildingnumber'] = str('-')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
