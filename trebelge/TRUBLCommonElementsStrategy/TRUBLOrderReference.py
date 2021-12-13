from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLOrderReference(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        # ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu(1)')
        orderreference: dict = {'id': element.find(cbcnamespace + 'ID').text,
                                'issuedate': element.find(cbcnamespace + 'IssueDate').text}

        # ['SalesOrderID'] = ('cbc', 'salesorderid', 'Seçimli (0...1)')
        # ['OrderTypeCode'] = ('cbc', 'ordertypecode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['SalesOrderID', 'OrderTypeCode']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                orderreference[field_.tag.lower()] = field_.text

        # ['DocumentReference'] = ('cac', 'documentreferences', 'Seçimli(0..n)', 'documentreference')
        documentreferences_ = element.findall(cacnamespace + 'DocumentReference')
        if documentreferences_ is not None:
            # TODO implement this: process via DocumentReference instance
            pass

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
