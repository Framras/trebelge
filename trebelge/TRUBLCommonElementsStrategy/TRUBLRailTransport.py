from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRailTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR RailTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['TrainID'] = ('cbc', 'TrainID', 'Zorunlu(1)')
        trainid_: Element = element.find('./' + cbcnamespace + 'TrainID')
        if trainid_ is not None:
            if trainid_.text is not None:
                frappedoc['trainid'] = trainid_.text.strip()
        # ['RailCarID'] = ('cbc', 'RailCarID', 'Seçimli (0...1)')
        railcarid_: Element = element.find('./' + cbcnamespace + 'RailCarID')
        if railcarid_ is not None:
            if railcarid_.text is not None:
                frappedoc['railcarid'] = railcarid_.text.strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
