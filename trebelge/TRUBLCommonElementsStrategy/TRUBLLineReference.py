from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference


class TRUBLLineReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR LineReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LineID'] = ('cbc', '', 'Zorunlu (1)')
        frappedoc: dict = {'lineid': element.find('./' + cbcnamespace + 'LineID').text}
        # ['LineStatusCode'] = ('cbc', '', 'Seçimli (0...1)')
        linestatuscode_: Element = element.find('./' + cbcnamespace + 'LineStatusCode')
        if linestatuscode_:
            frappedoc['linestatuscode'] = linestatuscode_.text
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)')
        documentreference_: Element = element.find('./' + cacnamespace + 'DocumentReference')
        if documentreference_:
            frappedoc['documentreference'] = [TRUBLDocumentReference.process_element(documentreference_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)]

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
