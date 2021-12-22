from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxCategory import TRUBLTaxCategory


class TRUBLTaxSubtotal(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxSubtotal'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
        taxamount_: Element = element.find(cbcnamespace + 'TaxAmount')
        frappedoc: dict = {'taxamount': taxamount_.text,
                           'taxamountcurrencyid': taxamount_.attrib.get('currencyID')}
        # ['TaxCategory'] = ('cac', 'taxcategory', 'Zorunlu(1)')
        taxcategory_: Element = element.find(cacnamespace + 'TaxCategory')
        strategy: TRUBLCommonElement = TRUBLTaxCategory()
        self._strategyContext.set_strategy(strategy)
        frappedoc['taxcategory'] = self._strategyContext.return_element_data(taxcategory_,
                                                                             cbcnamespace,
                                                                             cacnamespace)
        # ['CalculationSequenceNumeric'] = ('cbc', 'calculationsequencenumeric', 'Seçimli (0...1)')
        # ['Percent'] = ('cbc', 'percent', 'Seçimli (0...1)')
        cbcsecimli01: list = ['CalculationSequenceNumeric', 'Percent']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['TaxableAmount'] = ('cbc', 'taxableamount', 'Seçimli (0...1)')
        taxableamount_: Element = element.find(cbcnamespace + 'TaxableAmount')
        if taxableamount_:
            frappedoc['taxableamount'] = taxableamount_.text
            frappedoc['taxableamountcurrencyid'] = taxableamount_.attrib.get('currencyID')
        # ['TransactionCurrencyTaxAmount'] = ('cbc', 'transactioncurrencytaxamount', 'Seçimli (0...1)')
        transactioncurrencytaxamount_: Element = element.find(cbcnamespace + 'TransactionCurrencyTaxAmount')
        if transactioncurrencytaxamount_:
            frappedoc['transactioncurrencytaxamount'] = transactioncurrencytaxamount_.text
            frappedoc['transactioncurrencytaxamountcurrencyid'] = transactioncurrencytaxamount_.attrib.get(
                'currencyID')
        # ['BaseUnitMeasure'] = ('cbc', 'baseunitmeasure', 'Seçimli (0...1)')
        baseunitmeasure_: Element = element.find(cbcnamespace + 'BaseUnitMeasure')
        if baseunitmeasure_:
            frappedoc['baseunitmeasure'] = baseunitmeasure_.text
            frappedoc['baseunitmeasureunitcode'] = baseunitmeasure_.attrib.get('unitCode')
        # ['PerUnitAmount'] = ('cbc', 'perunitamount', 'Seçimli (0...1)')
        perunitamount_: Element = element.find(cbcnamespace + 'PerUnitAmount')
        if perunitamount_:
            frappedoc['perunitamount'] = perunitamount_.text
            frappedoc['perunitamountcurrencyid'] = perunitamount_.attrib.get('currencyID')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
