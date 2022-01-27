from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExchangeRate(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ExchangeRate'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['SourceCurrencyCode'] = ('cbc', 'sourcecurrencycode', 'Zorunlu(1)')
        sourcecurrencycode_: Element = element.find('./' + cbcnamespace + 'SourceCurrencyCode')
        if sourcecurrencycode_ is not None:
            if sourcecurrencycode_.text is not None:
                frappedoc['sourcecurrencycode'] = sourcecurrencycode_.text.strip()
        # ['TargetCurrencyCode'] = ('cbc', 'targetcurrencycode', 'Zorunlu(1)')
        targetcurrencycode_: Element = element.find('./' + cbcnamespace + 'TargetCurrencyCode')
        if targetcurrencycode_ is not None:
            if targetcurrencycode_.text is not None:
                frappedoc['targetcurrencycode'] = targetcurrencycode_.text.strip()
        # ['CalculationRate'] = ('cbc', 'calculationrate', 'Zorunlu(1)')
        calculationrate_: Element = element.find('./' + cbcnamespace + 'CalculationRate')
        if calculationrate_ is not None:
            if calculationrate_.text is not None:
                frappedoc['calculationrate_'] = calculationrate_.text.strip()
        # ['Date'] = ('cbc', 'date', 'Seçimli (0...1)')
        date_: Element = element.find('./' + cbcnamespace + 'Date')
        if date_ is not None:
            if date_.text is not None:
                frappedoc['date'] = date_.text.strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
