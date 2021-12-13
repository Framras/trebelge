from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLTaxCategory(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        """
        ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        ['TaxExemptionReasonCode'] = ('cbc', 'taxexemptionreasoncode', 'Seçimli (0...1)')
        ['TaxExemptionReason'] = ('cbc', 'taxexemptionreason', 'Seçimli (0...1)')
        ['TaxScheme'] = ('cac', 'taxscheme', 'Zorunlu(1)')
        """
        taxCategory: dict = {}
        cbcsecimli01: list = ['TaxExemptionReasonCode', 'TaxExemptionReason']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                taxCategory[field_.tag.lower()] = field_.text

        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            taxCategory['taxcategoryname'] = name_.text

        taxscheme = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        taxscheme_ = self._strategyContext.return_element_data(taxscheme, cbcnamespace,
                                                               cacnamespace)
        for key in taxscheme_.keys():
            if taxscheme_.get(key) is not None:
                taxCategory['taxscheme_' + key] = taxscheme_.get(key)

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
