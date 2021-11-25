from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLOrderReference(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        ['SalesOrderID'] = ('cbc', 'salesorderid', 'Seçimli (0...1)')
        ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu(1)')
        ['OrderTypeCode'] = ('cbc', 'ordertypecode', 'Seçimli (0...1)')
        ['DocumentReference'] = ('cac', 'documentreferences', 'Seçimli(0..n)', 'documentreference')
        """
        orderreference: dict = {'id': element.find(cbcnamespace + 'ID').text,
                                'issuedate': element.find(cbcnamespace + 'IssueDate').text}
        salesorderid_ = element.find(cbcnamespace + 'SalesOrderID')
        if salesorderid_ is not None:
            orderreference['salesorderid'] = salesorderid_.text
        ordertypecode_ = element.find(cbcnamespace + 'OrderTypeCode')
        if ordertypecode_ is not None:
            orderreference['ordertypecode'] = ordertypecode_.text
        documentreferences_ = element.findall(cacnamespace + 'DocumentReference')
        if documentreferences_ is not None:
            # TODO implement this: process via DocumentReference instance
            pass

        return orderreference
