from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLBuildingNumber(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR BuildingNumber'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        if element.text is not None:
            frappedoc['buildingnumber'] = element.text
        else:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
