from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLTaxSubtotal(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['TaxableAmount'] = ('cbc', 'taxableamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'taxableamount_currencyid', 'Zorunlu(1)')
        ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
        ['currencyID'] = ('', 'taxamount_currencyid', 'Zorunlu(1)')
        ['CalculationSequenceNumeric'] = ('cbc', 'calculationsequencenumeric', 'Seçimli (0...1)')
        ['TransactionCurrencyTaxAmount'] = ('cbc', 'transactioncurrencytaxamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'transactioncurrencytaxamount_currencyid', 'Zorunlu(1)')
        ['Percent'] = ('cbc', 'percent', 'Seçimli (0...1)')
        ['BaseUnitMeasure'] = ('cbc', 'baseunitmeasure', 'Seçimli (0...1)')
        ['unitCode'] = ('', 'baseunitmeasure_unitcode', 'Zorunlu(1)')
        ['PerUnitAmount'] = ('cbc', 'perunitamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'perunitamount_currencyid', 'Zorunlu(1)')
        ['TaxCategory'] = ('cac', 'taxcategory', 'Zorunlu(1)')

        ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        ['TaxExemptionReasonCode'] = ('cbc', 'taxexemptionreasonCode', 'Seçimli (0...1)')
        ['TaxExemptionReason'] = ('cbc', 'taxexemptionreason', 'Seçimli (0...1)')
        ['TaxScheme'] = ('cac', 'taxscheme', 'Zorunlu(1)')
        """
        taxSubtotal: dict = {}
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            taxCategory['name'] = name_.text
        taxexemptionreasoncode_ = element.find(cbcnamespace + 'TaxExemptionReasonCode')
        if taxexemptionreasoncode_ is not None:
            taxCategory['taxexemptionreasonCode'] = taxexemptionreasoncode_.text
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
