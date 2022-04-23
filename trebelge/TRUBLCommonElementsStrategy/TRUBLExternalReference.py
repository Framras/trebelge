from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExternalReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ExternalReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['URI'] = ('cbc', '', 'Zorunlu(1)')
        uri_: Element = element.find('./' + cbcnamespace + 'URI')
        if uri_ is None or uri_.text.strip() == '':
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(uri=uri_.text))

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
