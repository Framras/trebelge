from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAirTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AirTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['AircraftID'] = ('cbc', '', 'Zorunlu (1)')
        airTransport: dict = {'aircraftid': element.find(cbcnamespace + 'AircraftID').text}

        if not frappe.get_all(self._frappeDoctype, filters=airTransport):
            pass
        else:
            newairtransport = airTransport
            newairtransport['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newairtransport)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=airTransport)
