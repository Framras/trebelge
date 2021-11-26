from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLTaxCategory(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        ['TaxExemptionReasonCode'] = ('cbc', 'taxexemptionreasoncode', 'Seçimli (0...1)')
        ['TaxExemptionReason'] = ('cbc', 'taxexemptionreason', 'Seçimli (0...1)')
        ['TaxScheme'] = ('cac', 'taxscheme', 'Zorunlu(1)')
        """
        taxCategory: dict = {}
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            taxCategory['name'] = name_.text
        taxexemptionreasoncode_ = element.find(cbcnamespace + 'TaxExemptionReasonCode')
        if taxexemptionreasoncode_ is not None:
            taxCategory['taxexemptionreasoncode'] = taxexemptionreasoncode_.text
        taxexemptionreason_ = element.find(cbcnamespace + 'TaxExemptionReason')
        if taxexemptionreason_ is not None:
            taxCategory['taxexemptionreason'] = taxexemptionreason_.text
        taxscheme = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        taxscheme_ = self._strategyContext.return_element_data(taxscheme, cbcnamespace,
                                                               cacnamespace)
        mapping: dict = {'id': 'taxscheme_id',
                         'name': 'taxscheme_name',
                         'taxtypecode': 'taxscheme_taxtypecode'
                         }
        for key in taxscheme_.keys():
            if taxscheme_.get(key) is not None:
                taxCategory[mapping.get(key)] = taxscheme_.get(key)

        return taxCategory
