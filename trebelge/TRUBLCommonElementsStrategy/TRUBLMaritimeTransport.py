from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLMaritimeTransport(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['VesselID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['VesselName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RadioCallSignID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ShipsRequirements'] = ('cbc', '', 'Seçimli (0...n)')
        # ['GrossTonnageMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        # ['NetTonnageMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RegistryCertificateDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)')
        # ['RegistryPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
