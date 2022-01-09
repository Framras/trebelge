from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLNote(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Note'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        element_ = element.text
        if element_ is None:
            return None
        if str.strip(element_) == '':
            return None

        return self._get_frappedoc(self._frappeDoctype, dict(note=element_))
