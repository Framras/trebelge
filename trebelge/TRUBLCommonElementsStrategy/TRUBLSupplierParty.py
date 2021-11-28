from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLSupplierParty(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'customerparty')
        ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
        """
        orderreference: dict = {'id': element.find(cbcnamespace + 'ID').text,
                                'issuedate': element.find(cbcnamespace + 'IssueDate').text}

        cbcsecimli01: list = ['SalesOrderID', 'OrderTypeCode']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                orderreference[field_.tag.lower()] = field_.text

        documentreferences_ = element.findall(cacnamespace + 'DocumentReference')
        if documentreferences_ is not None:
            # TODO implement this: process via DocumentReference instance
            pass

        return orderreference
