from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLLocation(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        """
        ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        ['Address'] = ('cac', 'Address()', 'Seçimli (0...1)','address')
        """
        location: dict = {}
        id_: Element = element.find(cbcnamespace + 'ID')
        if not id_:
            location['locationid'] = id_.text
        address_: Element = element.find(cacnamespace + 'Address')
        if not address_:
            strategy: TRUBLCommonElement = TRUBLAddress()
            self._strategyContext.set_strategy(strategy)
            address = self._strategyContext.return_element_data(address_, cbcnamespace,
                                                                cacnamespace)
            for key in address.keys():
                location['address_' + key] = address.get(key)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
