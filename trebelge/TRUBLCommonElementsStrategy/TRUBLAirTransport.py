from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAirTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AirTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['AircraftID'] = ('cbc', '', 'Zorunlu (1)')
        frappedoc: dict = {'aircraftid': element.find('./' + cbcnamespace + 'AircraftID').text}

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
