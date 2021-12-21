from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLDespatchLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DespatchLine'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find(cbcnamespace + 'ID').text}

        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Zorunlu(1)')
        # ['Item'] = ('cac', 'Item', 'Zorunlu(1)')

        # ['Note'] = ('cbc', '', 'Seçimli(0..n)')
        # ['OutstandingReason'] = ('cbc', '', 'Seçimli(0..n)')

        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli(0..n)')
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli(0..n)')

        # ['DeliveredQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OutstandingQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['DeliveredQuantity', 'OutstandingQuantity', 'OversupplyQuantity']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
