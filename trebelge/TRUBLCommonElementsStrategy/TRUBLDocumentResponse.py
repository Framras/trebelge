from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineResponse import TRUBLLineResponse
from trebelge.TRUBLCommonElementsStrategy.TRUBLResponse import TRUBLResponse


class TRUBLDocumentResponse(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR DocumentResponse'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Response'] = ('cac', 'Response', 'Zorunlu(1)')
        response_: Element = element.find('./' + cacnamespace + 'Response')
        tmp = TRUBLResponse().process_element(response_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc: dict = dict(response=tmp.name)
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Zorunlu(1)')
        documentreference_: Element = element.find('./' + cacnamespace + 'DocumentReference')
        tmp = TRUBLDocumentReference().process_element(documentreference_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc['documentreference'] = tmp.name
        # ['LineResponse'] = ('cac', 'LineResponse', 'Seçimli (0...1)')
        lineresponse_: Element = element.find('./' + cacnamespace + 'LineResponse')
        if lineresponse_ is not None:
            tmp = TRUBLLineResponse().process_element(lineresponse_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['lineresponse'] = tmp.name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
