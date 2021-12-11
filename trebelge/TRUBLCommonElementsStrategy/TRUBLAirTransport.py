from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAirTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AirTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['AircraftID'] = ('cbc', '', 'Zorunlu (1)')
        frappedoc: dict = {'aircraftid': element.find(cbcnamespace + 'AircraftID').text}

        if not frappe.get_all(self._frappeDoctype, filters=frappedoc):
            pass
        else:
            newfrappedoc = frappedoc
            newfrappedoc['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newfrappedoc)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=frappedoc)
