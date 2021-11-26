from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExchangeRate(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['SourceCurrencyCode'] = ('cbc', 'sourcecurrencycode', 'Zorunlu(1)')
        ['TargetCurrencyCode'] = ('cbc', 'targetcurrencycode', 'Zorunlu(1)')
        ['CalculationRate'] = ('cbc', 'calculationrate', 'Zorunlu(1)')
        ['Date'] = ('cbc', 'date', 'Seçimli (0...1)')
        """
        sourcecurrencycode_ = element.find(cbcnamespace + 'SourceCurrencyCode')
        targetcurrencycode_ = element.find(cbcnamespace + 'TargetCurrencyCode')
        calculationrate_ = element.find(cbcnamespace + 'CalculationRate')
        exchangerate: dict = {'sourcecurrencycode': sourcecurrencycode_.text,
                              'targetcurrencycode': targetcurrencycode_.text,
                              'calculationrate': calculationrate_.text
                              }
        date_ = element.find(cbcnamespace + 'Date')
        if date_ is not None:
            exchangerate['date'] = date_.text

        return exchangerate