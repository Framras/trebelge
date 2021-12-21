from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLSignature(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        # ['SignatoryParty'] = ('cac', 'Party', 'Zorunlu(1)')
        # ['DigitalSignatureAttachment'] = ('cac', 'Attachment', 'Zorunlu(1)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
