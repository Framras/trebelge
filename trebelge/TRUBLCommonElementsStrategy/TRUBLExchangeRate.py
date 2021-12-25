from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExchangeRate(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ExchangeRate'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['SourceCurrencyCode'] = ('cbc', 'sourcecurrencycode', 'Zorunlu(1)')
        # ['TargetCurrencyCode'] = ('cbc', 'targetcurrencycode', 'Zorunlu(1)')
        # ['CalculationRate'] = ('cbc', 'calculationrate', 'Zorunlu(1)')
        frappedoc: dict = {'sourcecurrencycode': element.find('./' + cbcnamespace + 'SourceCurrencyCode').text,
                           'targetcurrencycode': element.find('./' + cbcnamespace + 'TargetCurrencyCode').text,
                           'calculationrate': element.find('./' + cbcnamespace + 'CalculationRate').text
                           }
        # ['Date'] = ('cbc', 'date', 'Seçimli (0...1)')
        date_: Element = element.find('./' + cbcnamespace + 'Date')
        if date_:
            frappedoc['exchangeratedate'] = date_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
