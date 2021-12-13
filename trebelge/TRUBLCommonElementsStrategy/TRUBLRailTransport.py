from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRailTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR RailTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['TrainID'] = ('cbc', 'TrainID', 'Zorunlu(1)')
        railTransport: dict = {'trainid': element.find(cbcnamespace + 'TrainID').text}

        # ['RailCarID'] = ('cbc', 'RailCarID', 'Seçimli (0...1)')
        railcarid_ = element.find(cbcnamespace + 'RailCarID')
        if railcarid_ is not None:
            railTransport[railcarid_.tag.lower()] = railcarid_.text

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
