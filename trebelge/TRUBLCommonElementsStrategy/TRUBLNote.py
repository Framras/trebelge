from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLNote(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Note'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {'note': element.text}

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
