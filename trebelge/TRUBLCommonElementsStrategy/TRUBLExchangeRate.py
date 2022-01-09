from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExchangeRate(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ExchangeRate'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['SourceCurrencyCode'] = ('cbc', 'sourcecurrencycode', 'Zorunlu(1)')
        sourcecurrencycode_: Element = element.find('./' + cbcnamespace + 'SourceCurrencyCode')
        # ['TargetCurrencyCode'] = ('cbc', 'targetcurrencycode', 'Zorunlu(1)')
        targetcurrencycode_: Element = element.find('./' + cbcnamespace + 'TargetCurrencyCode')
        # ['CalculationRate'] = ('cbc', 'calculationrate', 'Zorunlu(1)')
        calculationrate_: Element = element.find('./' + cbcnamespace + 'CalculationRate')
        if sourcecurrencycode_ is None or sourcecurrencycode_.text is None or \
                targetcurrencycode_ is None or targetcurrencycode_.text is None or \
                calculationrate_ is None or calculationrate_.text is None:
            return None
        frappedoc: dict = dict(sourcecurrencycode=sourcecurrencycode_.text,
                               targetcurrencycode=targetcurrencycode_.text,
                               calculationrate=calculationrate_.text
                               )
        # ['Date'] = ('cbc', 'date', 'Seçimli (0...1)')
        date_: Element = element.find('./' + cbcnamespace + 'Date')
        if date_ is not None and date_.text is not None:
            frappedoc['date'] = date_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
