from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLTaxCategory(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['TaxExemptionReasonCode'] = ('cbc', 'taxexemptionreasoncode', 'Seçimli (0...1)')
        # ['TaxExemptionReason'] = ('cbc', 'taxexemptionreason', 'Seçimli (0...1)')
        cbcsecimli01: list = ['TaxExemptionReasonCode', 'TaxExemptionReason']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc['taxcategoryname'] = name_.text

        # ['TaxScheme'] = ('cac', 'taxscheme', 'Zorunlu(1)')
        taxscheme_: Element = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        taxscheme = self._strategyContext.return_element_data(taxscheme_, cbcnamespace,
                                                              cacnamespace)
        for key in taxscheme.keys():
            if taxscheme.get(key) is not None:
                frappedoc['taxscheme_' + key] = taxscheme.get(key)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
