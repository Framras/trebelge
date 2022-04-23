from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference


class TRUBLLineReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR LineReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LineID'] = ('cbc', '', 'Zorunlu (1)')
        lineid_ = element.find('./' + cbcnamespace + 'LineID').text
        if lineid_ is None:
            return None
        frappedoc: dict = dict(lineid=lineid_)
        # ['LineStatusCode'] = ('cbc', '', 'Seçimli (0...1)')
        linestatuscode_: Element = element.find('./' + cbcnamespace + 'LineStatusCode')
        if linestatuscode_ is not None:
            if linestatuscode_.text is not None:
                frappedoc['linestatuscode'] = linestatuscode_.text
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)')
        documentreference_: Element = element.find('./' + cacnamespace + 'DocumentReference')
        if documentreference_ is not None:
            tmp = TRUBLDocumentReference().process_element(documentreference_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['documentreference'] = tmp.name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
