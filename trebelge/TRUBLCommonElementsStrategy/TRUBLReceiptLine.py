from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLReceiptLine(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Zorunlu (1)')
        # ['Note'] = ('cbc', '', 'Seçimli (0...n)')
        # ['ReceivedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ShortQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RejectedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RejectReasonCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RejectReason'] = ('cbc', '', 'Seçimli (0...n)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ReceivedDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaintCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaint'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...1)')
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...1)')
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)')
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
