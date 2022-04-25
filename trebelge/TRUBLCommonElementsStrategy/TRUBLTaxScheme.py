from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLTaxScheme(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxScheme'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        pass

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        frappedata: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['TaxTypeCode'] = ('cbc', 'taxtypecode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'TaxTypeCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedata[elementtag_.lower()] = field_.text.strip()
        # ['Name'] = ('cbc', 'taxschemename', 'Seçimli (0...1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is not None:
            if name_.text is not None:
                frappedata['taxschemename'] = name_.text.strip()

        return frappedata
