from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference


class TRUBLOrderReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR OrderReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        # ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text,
                           'issuedate': element.find('./' + cbcnamespace + 'IssueDate').text}
        # ['SalesOrderID'] = ('cbc', 'salesorderid', 'Seçimli (0...1)')
        # ['OrderTypeCode'] = ('cbc', 'ordertypecode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['SalesOrderID', 'OrderTypeCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['DocumentReference'] = ('cac', '', 'Seçimli(0..n)', 'documentreference')
        documentreferences_: list = element.findall('./' + cacnamespace + 'DocumentReference')
        if len(documentreferences_) != 0:
            documentreferences: list = []
            for documentreference_ in documentreferences_:
                documentreferences.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                   cbcnamespace,
                                                                                   cacnamespace))
            frappedoc['documentreference'] = documentreferences

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
