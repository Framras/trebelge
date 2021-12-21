from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLLineResponse(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR LineResponse'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LineReference'] = ('cac', 'LineReference', 'Zorunlu(1)')
        frappedoc: dict = {}
        # ['Response'] = ('cac', 'Response', 'Zorunlu(1..n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
