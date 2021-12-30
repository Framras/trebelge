from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCountry(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Country'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Name'] = ('cbc', 'countryname', 'Zorunlu(1)')
        frappedoc: dict = {}
        countryname = element.find('./' + cbcnamespace + 'Name')
        if countryname:
            frappedoc['countryname'] = countryname.text
        else:
            frappe.log_error('countryname not provided for ' + element.tag, 'TRUBLCountry')
            frappedoc['countryname'] = str(' ')

        # ['IdentificationCode'] = ('cbc', 'identificationcode', 'Seçimli (0...1)')
        identificationcode_: Element = element.find('./' + cbcnamespace + 'IdentificationCode')
        if identificationcode_ is not None:
            frappedoc['identificationcode'] = identificationcode_.text
        # TODO connection to ERPNext Country is pending

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
