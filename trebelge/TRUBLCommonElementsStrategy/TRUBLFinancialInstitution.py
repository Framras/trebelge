from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLFinancialInstitution(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        _frappeDoctype: str = 'UBL TR FinancialInstitution'

        # ['Name'] = ('cbc', 'name', 'Seçimli(0..1)', 'financialinstitution')
        frappedoc: dict = {}
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc['financialinstitution'] = name_.text

        if not frappe.get_all(self._frappeDoctype, filters=frappedoc):
            pass
        else:
            newfrappedoc = frappedoc
            newfrappedoc['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newfrappedoc)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=frappedoc)
