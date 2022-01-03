from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAirTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AirTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['AircraftID'] = ('cbc', '', 'Zorunlu (1)')
        aircraftid_ = element.find('./' + cbcnamespace + 'AircraftID').text
        if aircraftid_ is None:
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(aircraftid=aircraftid_))
