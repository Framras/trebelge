from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLReceiptLine(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu (1)')
        frappedoc: dict = {'id': element.find(cbcnamespace + 'ID').text}
        # ['RejectReasonCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ReceivedDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaintCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaint'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RejectReasonCode', 'ReceivedDate', 'TimingComplaintCode', 'TimingComplaint']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['ReceivedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ShortQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RejectedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        cbcqtysecimli01: list = ['ReceivedQuantity', 'ShortQuantity', 'RejectedQuantity', 'OversupplyQuantity']
        for elementtag_ in cbcqtysecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
                frappedoc[field_.tag.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Note'] = ('cbc', '', 'Seçimli (0...n)')

        # ['RejectReason'] = ('cbc', '', 'Seçimli (0...n)')

        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')

        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...1)')
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...1)')

        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)')
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
