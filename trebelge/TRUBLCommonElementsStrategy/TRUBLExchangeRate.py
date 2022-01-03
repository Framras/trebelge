from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExchangeRate(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ExchangeRate'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['SourceCurrencyCode'] = ('cbc', 'sourcecurrencycode', 'Zorunlu(1)')
        sourcecurrencycode_ = element.find('./' + cbcnamespace + 'SourceCurrencyCode').text
        # ['TargetCurrencyCode'] = ('cbc', 'targetcurrencycode', 'Zorunlu(1)')
        targetcurrencycode_ = element.find('./' + cbcnamespace + 'TargetCurrencyCode').text
        # ['CalculationRate'] = ('cbc', 'calculationrate', 'Zorunlu(1)')
        calculationrate_ = element.find('./' + cbcnamespace + 'CalculationRate').text
        if sourcecurrencycode_ is None or targetcurrencycode_ is None or calculationrate_ is None:
            return None
        frappedoc: dict = dict(sourcecurrencycode=sourcecurrencycode_,
                               targetcurrencycode=targetcurrencycode_,
                               calculationrate=calculationrate_
                               )
        # ['Date'] = ('cbc', 'date', 'Seçimli (0...1)')
        date_: Element = element.find('./' + cbcnamespace + 'Date')
        if date_ is not None:
            if date_.text is not None:
                frappedoc['date'] = date_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
