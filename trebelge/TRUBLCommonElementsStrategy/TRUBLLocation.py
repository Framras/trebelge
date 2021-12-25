from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLLocation(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Location'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None:
            frappedoc['locationid'] = id_.text
        # ['Address'] = ('cac', 'Address()', 'Seçimli (0...1)','address')
        address_: Element = element.find('./' + cacnamespace + 'Address')
        if address_ is not None:
            strategy: TRUBLCommonElement = TRUBLAddress()
            self._strategyContext.set_strategy(strategy)
            frappedoc['address'] = self._strategyContext.return_element_data(address_,
                                                                             cbcnamespace,
                                                                             cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
