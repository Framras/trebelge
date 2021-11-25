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
        orderreference_salesorderid = element.find(cbcnamespace + 'SalesOrderID')
        if orderreference_salesorderid is not None:
            orderreference['salesorderid'] = orderreference_salesorderid.text
        orderreference_ordertypecode = element.find(cbcnamespace + 'OrderTypeCode')
        if orderreference_ordertypecode is not None:
            orderreference['ordertypecode'] = orderreference_ordertypecode.text
        orderreference_documentreferences = element.findall(cacnamespace + 'DocumentReference')
        if len(orderreference_documentreferences) != 0:
            # TODO implement this: process via DocumentReference instance
            pass

        return orderreference
