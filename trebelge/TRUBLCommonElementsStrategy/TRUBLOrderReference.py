from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference


class TRUBLOrderReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR OrderReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        # ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu(1)')
        issuedate_: Element = element.find('./' + cbcnamespace + 'IssueDate')
        if id_ is None or id_.text is None or \
                issuedate_ is None or issuedate_.text is None:
            return None
        frappedoc: dict = {'id': id_.text,
                           'issuedate': issuedate_.text}
        # ['SalesOrderID'] = ('cbc', 'salesorderid', 'Seçimli (0...1)')
        # ['OrderTypeCode'] = ('cbc', 'ordertypecode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['SalesOrderID', 'OrderTypeCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None and field_.text is not None:
                frappedoc[elementtag_.lower()] = field_.text
        if frappedoc == {}:
            return None
        # ['DocumentReference'] = ('cac', '', 'Seçimli(0..n)', 'documentreference')
        documentreferences_: list = element.findall('./' + cacnamespace + 'DocumentReference')
        documentreferences = list()
        if len(documentreferences_) != 0:
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    documentreferences.append(tmp.name)
        if len(documentreferences) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            doc_append = document.append("documentreference", {})
            for documentreference in documentreferences:
                doc_append.documentreference = documentreference
                document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
