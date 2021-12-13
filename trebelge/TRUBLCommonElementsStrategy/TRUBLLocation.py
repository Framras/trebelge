from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLLocation(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        """
        ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        ['Address'] = ('cac', 'Address()', 'Seçimli (0...1)','address')
        """
        location: dict = {}
        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            location['locationid'] = id_.text
        address_ = element.find(cacnamespace + 'Address')
        if address_ is not None:
            strategy: TRUBLCommonElement = TRUBLAddress()
            self._strategyContext.set_strategy(strategy)
            address = self._strategyContext.return_element_data(address_, cbcnamespace,
                                                                cacnamespace)
            for key in address.keys():
                location['address_' + key] = address.get(key)

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
