from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLTaxScheme(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        """
        ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        ['TaxTypeCode'] = ('cbc', 'taxtypecode', 'Seçimli (0...1)')
        """
        taxScheme: dict = {}
        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            taxScheme['taxschemeid'] = id_.text
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            taxScheme['taxschemename'] = name_.text
        taxtypecode_ = element.find(cbcnamespace + 'TaxTypeCode')
        if taxtypecode_ is not None:
            taxScheme[taxtypecode_.tag.lower()] = taxtypecode_.text

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
