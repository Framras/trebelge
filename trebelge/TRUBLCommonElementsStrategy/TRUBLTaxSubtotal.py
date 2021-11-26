from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxCategory import TRUBLTaxCategory


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
        """
        taxamount_ = element.find(cbcnamespace + 'TaxAmount')
        taxSubtotal: dict = {'taxamount': taxamount_.text,
                             'taxamount_currencyid': taxamount_.attrib.get('currencyID')}
        taxcategory = element.find(cacnamespace + 'TaxCategory')
        strategy: TRUBLCommonElement = TRUBLTaxCategory()
        self._strategyContext.set_strategy(strategy)
        taxcategory_ = self._strategyContext.return_element_data(taxcategory, cbcnamespace,
                                                                 cacnamespace)
        mapping: dict = {'name': 'taxcategory_name',
                         'taxexemptionreasoncode': 'taxcategory_taxexemptionreasoncode',
                         'taxexemptionreason': 'taxcategory_taxexemptionreason',
                         'taxscheme_id': 'taxscheme_id',
                         'taxscheme_name': 'taxscheme_name',
                         'taxscheme_taxtypecode': 'taxscheme_taxtypecode'
                         }
        for key in taxcategory_.keys():
            if taxcategory_.get(key) is not None:
                taxSubtotal[mapping.get(key)] = taxcategory_.get(key)

        taxableamount_ = element.find(cbcnamespace + 'TaxableAmount')
        if taxableamount_ is not None:
            taxSubtotal['taxableamount'] = taxableamount_.text
            taxSubtotal['taxableamount_currencyid'] = taxableamount_.attrib.get('currencyID')
        calculationsequencenumeric_ = element.find(cbcnamespace + 'CalculationSequenceNumeric')
        if calculationsequencenumeric_ is not None:
            taxSubtotal['calculationsequencenumeric'] = calculationsequencenumeric_.text
        transactioncurrencytaxamount_ = element.find(cbcnamespace + 'TransactionCurrencyTaxAmount')
        if transactioncurrencytaxamount_ is not None:
            taxSubtotal['transactioncurrencytaxamount'] = transactioncurrencytaxamount_.text
            taxSubtotal['transactioncurrencytaxamount_currencyid'] = transactioncurrencytaxamount_.attrib.get(
                'currencyID')
        percent_ = element.find(cbcnamespace + 'Percent')
        if percent_ is not None:
            taxSubtotal['percent'] = percent_.text
        baseunitmeasure_ = element.find(cbcnamespace + 'BaseUnitMeasure')
        if baseunitmeasure_ is not None:
            taxSubtotal['baseunitmeasure'] = baseunitmeasure_.text
            taxSubtotal['baseunitmeasure_unitcode'] = baseunitmeasure_.attrib.get('unitCode')
        perunitamount_ = element.find(cbcnamespace + 'PerUnitAmount')
        if perunitamount_ is not None:
            taxSubtotal['perunitamount'] = perunitamount_.text
            taxSubtotal['perunitamount_currencyid'] = perunitamount_.attrib.get('currencyID')

        return taxSubtotal