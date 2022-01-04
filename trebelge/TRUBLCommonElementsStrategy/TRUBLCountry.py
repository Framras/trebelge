from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCountry(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Country'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Name'] = ('cbc', 'countryname', 'Zorunlu(1)')
        countryname = element.find('./' + cbcnamespace + 'Name')
        if countryname is None:
            return None
        if countryname.text is not None:
            frappedoc['countryname'] = countryname.text
        # ['IdentificationCode'] = ('cbc', 'identificationcode', 'Seçimli (0...1)')
        identificationcode_: Element = element.find('./' + cbcnamespace + 'IdentificationCode')
        if identificationcode_ is not None:
            if identificationcode_.text is not None:
                frappedoc['identificationcode'] = identificationcode_.text
        # TODO connection to ERPNext Country is pending
        # TODO this is weird nonconforming xml files without Name filled
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)
