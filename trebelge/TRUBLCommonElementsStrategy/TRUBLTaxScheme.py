from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLTaxScheme(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxScheme'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:

        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['TaxTypeCode'] = ('cbc', 'taxtypecode', 'Seçimli (0...1)')
        frappedoc: dict = {}
        cbcsecimli01: list = ['ID', 'TaxTypeCode']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['Name'] = ('cbc', 'taxschemename', 'Seçimli (0...1)')
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc['taxschemename'] = name_.text

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
