from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxCategory import TRUBLTaxCategory


class TRUBLTaxSubtotal(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxSubtotal'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
        taxamount_: Element = element.find('./' + cbcnamespace + 'TaxAmount')
        if taxamount_ is not None:
            if taxamount_.text is not None:
                frappedoc['taxamount'] = taxamount_.text.strip()
                frappedoc['taxamountcurrencyid'] = taxamount_.attrib.get('currencyID').strip()
        # ['TaxCategory'] = ('cac', 'taxcategory', 'Zorunlu(1)')
        taxcategory_: Element = element.find('./' + cacnamespace + 'TaxCategory')
        if taxcategory_ is not None:
            tmp = TRUBLTaxCategory().process_element(taxcategory_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['taxcategory'] = tmp.name
        # ['CalculationSequenceNumeric'] = ('cbc', 'calculationsequencenumeric', 'Seçimli (0...1)')
        # ['Percent'] = ('cbc', 'percent', 'Seçimli (0...1)')
        cbcsecimli01: list = ['CalculationSequenceNumeric', 'Percent']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['TaxableAmount'] = ('cbc', 'taxableamount', 'Seçimli (0...1)')
        taxableamount_: Element = element.find('./' + cbcnamespace + 'TaxableAmount')
        if taxableamount_ is not None:
            if taxableamount_.text is not None:
                frappedoc['taxableamount'] = taxableamount_.text.strip()
                frappedoc['taxableamountcurrencyid'] = taxableamount_.attrib.get('currencyID').strip()
        # ['TransactionCurrencyTaxAmount'] = ('cbc', 'transactioncurrencytaxamount', 'Seçimli (0...1)')
        transactioncurrencytaxamount_: Element = element.find('./' + cbcnamespace + 'TransactionCurrencyTaxAmount')
        if transactioncurrencytaxamount_ is not None:
            if transactioncurrencytaxamount_.text is not None:
                frappedoc['transactioncurrencytaxamount'] = transactioncurrencytaxamount_.text.strip()
                frappedoc['transactioncurrencytaxamountcurrencyid'] = transactioncurrencytaxamount_.attrib.get(
                    'currencyID').strip()
        # ['BaseUnitMeasure'] = ('cbc', 'baseunitmeasure', 'Seçimli (0...1)')
        baseunitmeasure_: Element = element.find('./' + cbcnamespace + 'BaseUnitMeasure')
        if baseunitmeasure_ is not None:
            if baseunitmeasure_.text is not None:
                frappedoc['baseunitmeasure'] = baseunitmeasure_.text.strip()
                frappedoc['baseunitmeasureunitcode'] = baseunitmeasure_.attrib.get('unitCode').strip()
        # ['PerUnitAmount'] = ('cbc', 'perunitamount', 'Seçimli (0...1)')
        perunitamount_: Element = element.find('./' + cbcnamespace + 'PerUnitAmount')
        if perunitamount_ is not None:
            if perunitamount_.text is not None:
                frappedoc['perunitamount'] = perunitamount_.text.strip()
                frappedoc['perunitamountcurrencyid'] = perunitamount_.attrib.get('currencyID').strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc, False)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
