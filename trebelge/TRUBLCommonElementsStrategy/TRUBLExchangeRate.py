from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExchangeRate(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        """
        ['SourceCurrencyCode'] = ('cbc', 'sourcecurrencycode', 'Zorunlu(1)')
        ['TargetCurrencyCode'] = ('cbc', 'targetcurrencycode', 'Zorunlu(1)')
        ['CalculationRate'] = ('cbc', 'calculationrate', 'Zorunlu(1)')
        ['Date'] = ('cbc', 'date', 'Seçimli (0...1)')
        """
        exchangerate: dict = {'sourcecurrencycode': element.find(cbcnamespace + 'SourceCurrencyCode').text,
                              'targetcurrencycode': element.find(cbcnamespace + 'TargetCurrencyCode').text,
                              'calculationrate': element.find(cbcnamespace + 'CalculationRate').text
                              }
        date_ = element.find(cbcnamespace + 'Date')
        if date_ is not None:
            exchangerate['exchangeratedate'] = date_.text

        return exchangerate
