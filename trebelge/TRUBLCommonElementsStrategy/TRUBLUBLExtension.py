from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLUBLExtension(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportMeans'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ExtensionContent'] = ('cac', 'ExtensionContent', 'Zorunlu(1)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
