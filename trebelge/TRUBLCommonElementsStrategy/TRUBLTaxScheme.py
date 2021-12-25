from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLTaxScheme(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxScheme'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['TaxTypeCode'] = ('cbc', 'taxtypecode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'TaxTypeCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['Name'] = ('cbc', 'taxschemename', 'Seçimli (0...1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_:
            frappedoc['taxschemename'] = name_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
