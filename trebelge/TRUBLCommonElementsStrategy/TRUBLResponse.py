from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLDocumentResponse(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ReferenceID'] = ('cbc', '', 'Zorunlu (1)')
        # ['ResponseCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Description'] = ('cbc', '', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
