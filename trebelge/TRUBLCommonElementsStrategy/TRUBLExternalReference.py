from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExternalReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ExternalReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['URI'] = ('cbc', '', 'Zorunlu(1)')
        uri_ = element.find('./' + cbcnamespace + 'URI').text
        if uri_ is None:
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(uri=uri_))
