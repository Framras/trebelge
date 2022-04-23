from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAirTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AirTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['AircraftID'] = ('cbc', '', 'Zorunlu (1)')
        aircraftid_: Element = element.find('./' + cbcnamespace + 'AircraftID')
        if aircraftid_ is not None:
            if aircraftid_.text is not None:
                return self._get_frappedoc(self._frappeDoctype, dict(aircraftid=aircraftid_.text.strip()))

        return None

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
