from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLBuildingNumber(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR BuildingNumber'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        if element.text is None:
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(buildingnumber=element.text))
