from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLResponse import TRUBLResponse


class TRUBLLineResponse(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR LineResponse'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LineReference'] = ('cac', 'LineReference', 'Zorunlu(1)')
        linereference_: Element = element.find('./' + cacnamespace + 'LineReference')
        tmp = TRUBLLineReference().process_element(linereference_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        # ['Response'] = ('cac', 'Response', 'Zorunlu(1..n)')
        responses = list()
        for response_ in element.findall('./' + cacnamespace + 'Response'):
            tmp = TRUBLResponse().process_element(response_, cbcnamespace, cacnamespace)
            if tmp is not None:
                responses.append(tmp)
        if len(responses) == 0:
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(linereference=tmp.name,
                                                             response=responses))
