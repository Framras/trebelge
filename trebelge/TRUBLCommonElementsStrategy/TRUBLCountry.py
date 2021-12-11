from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCountry(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Country'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['Name'] = ('cbc', 'name', 'Zorunlu(1)')
        frappedoc: dict = {('Country' + 'Name').lower(): element.find(cbcnamespace + 'Name').text}
        # ['IdentificationCode'] = ('cbc', 'identificationcode', 'Seçimli (0...1)')
        identificationcode_ = element.find(cbcnamespace + 'IdentificationCode')
        if identificationcode_ is not None:
            frappedoc['identificationcode'] = identificationcode_.text

        if not frappe.get_all(self._frappeDoctype, filters=frappedoc):
            pass
        else:
            newfrappedoc = frappedoc
            newfrappedoc['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newfrappedoc)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=frappedoc)
