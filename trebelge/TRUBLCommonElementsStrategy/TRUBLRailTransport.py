from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRailTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR RailTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['TrainID'] = ('cbc', 'TrainID', 'Zorunlu(1)')
        trainid_ = element.find('./' + cbcnamespace + 'TrainID').text
        if trainid_ is None:
            return None
        frappedoc: dict = dict(trainid=trainid_)
        # ['RailCarID'] = ('cbc', 'RailCarID', 'Seçimli (0...1)')
        railcarid_: Element = element.find('./' + cbcnamespace + 'RailCarID')
        if railcarid_ is not None:
            if railcarid_.text is not None:
                frappedoc['railcarid'] = railcarid_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
