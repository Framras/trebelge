from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLHazardousGoodsTransit(TRUBLCommonElement):
    _frappeDoctype: str = 'TR UBL Tax Total'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}

        # ['TransportEmergencyCardCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['PackagingCriteriaCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['HazardousRegulationCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['InhalationToxicityZoneCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['TransportAuthorizationCode'] = ('cbc', '', 'Seçimli(0..1)')

        # ['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)')
        # ['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
