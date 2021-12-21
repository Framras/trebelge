from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRailTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR RailTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['TrainID'] = ('cbc', 'TrainID', 'Zorunlu(1)')
        frappedoc: dict = {'trainid': element.find(cbcnamespace + 'TrainID').text}
        # ['RailCarID'] = ('cbc', 'RailCarID', 'Seçimli (0...1)')
        railcarid_: Element = element.find(cbcnamespace + 'RailCarID')
        if railcarid_:
            frappedoc['railcarid'] = railcarid_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
