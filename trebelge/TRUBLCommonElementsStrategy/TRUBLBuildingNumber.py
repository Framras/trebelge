from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLBuildingNumber(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR BuildingNumber'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        frappedoc: dict = {'buildingnumber': element.find(cbcnamespace + 'BuildingNumber').text}

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
