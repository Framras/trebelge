from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAirTransport(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['AircraftID'] = ('cbc', '', 'Zorunlu (1)')
        """
        airTransport: dict = {'aircraftid': element.find(cbcnamespace + 'AircraftID').text}

        return airTransport
