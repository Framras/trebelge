from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLItemIdentification(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ItemIdentification'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None:
            element_ = id_.text
            if element_ is not None and element_.strip() != '':
                return self._get_frappedoc(self._frappeDoctype, {'id': element_.strip()})

        return None
