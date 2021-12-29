from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineResponse import TRUBLLineResponse
from trebelge.TRUBLCommonElementsStrategy.TRUBLResponse import TRUBLResponse


class TRUBLDocumentResponse(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR DocumentResponse'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Response'] = ('cac', 'Response', 'Zorunlu(1)')
        response_: Element = element.find('./' + cacnamespace + 'Response')
        frappedoc['response'] = TRUBLResponse().process_element(response_,
                                                                cbcnamespace,
                                                                cacnamespace).name
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Zorunlu(1)')
        documentreference_: Element = element.find('./' + cacnamespace + 'DocumentReference')
        frappedoc['documentreference'] = TRUBLDocumentReference().process_element(documentreference_,
                                                                                  cbcnamespace,
                                                                                  cacnamespace).name
        # ['LineResponse'] = ('cac', 'LineResponse', 'Seçimli (0...1)')
        lineresponse_: Element = element.find('./' + cacnamespace + 'LineResponse')
        if lineresponse_:
            frappedoc['lineresponse'] = TRUBLLineResponse().process_element(lineresponse_,
                                                                            cbcnamespace,
                                                                            cacnamespace).name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
