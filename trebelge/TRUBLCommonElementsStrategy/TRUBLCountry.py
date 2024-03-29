from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCountry(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Country'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['IdentificationCode'] = ('cbc', 'identificationcode', 'Seçimli (0...1)')
        identificationcode_: Element = element.find('./' + cbcnamespace + 'IdentificationCode')
        if identificationcode_ is not None:
            if identificationcode_.text is not None:
                frappedoc['identificationcode'] = identificationcode_.text.strip()
                if len(frappe.get_all(self._frappeDoctype, filters=frappedoc)) == 0:
                    # ['Name'] = ('cbc', 'countryname', 'Zorunlu(1)')
                    countryname = element.find('./' + cbcnamespace + 'Name')
                    if countryname is not None:
                        if countryname.text is not None:
                            frappedoc['countryname'] = countryname.text.strip()
                    # TODO connection to ERPNext Country is pending
                    # TODO this is weird nonconforming xml files without Name filled
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
