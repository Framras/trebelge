from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineResponse import TRUBLLineResponse
from trebelge.TRUBLCommonElementsStrategy.TRUBLResponse import TRUBLResponse


class TRUBLDocumentResponse(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR DocumentResponse'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Response'] = ('cac', 'Response', 'Zorunlu(1)')
        response_: Element = element.find(cacnamespace + 'Response')
        strategy: TRUBLCommonElement = TRUBLResponse()
        self._strategyContext.set_strategy(strategy)
        frappedoc['response'] = self._strategyContext.return_element_data(response_,
                                                                          cbcnamespace,
                                                                          cacnamespace)
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Zorunlu(1)')
        documentreference_: Element = element.find(cacnamespace + 'DocumentReference')
        strategy: TRUBLCommonElement = TRUBLDocumentReference()
        self._strategyContext.set_strategy(strategy)
        frappedoc['documentreference'] = self._strategyContext.return_element_data(documentreference_,
                                                                                   cbcnamespace,
                                                                                   cacnamespace)
        # ['LineResponse'] = ('cac', 'LineResponse', 'Seçimli (0...1)')
        lineresponse_: Element = element.find(cacnamespace + 'LineResponse')
        if lineresponse_:
            strategy: TRUBLCommonElement = TRUBLLineResponse()
            self._strategyContext.set_strategy(strategy)
            frappedoc['lineresponse'] = self._strategyContext.return_element_data(lineresponse_,
                                                                                  cbcnamespace,
                                                                                  cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
