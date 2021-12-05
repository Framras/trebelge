from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLItemIdentification(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ID'] = ('cbc', '', 'Zorunlu(1)')
        """
        itemidentification: dict = {'itemidentificationid': element.find(cbcnamespace + 'ID').text}

        return itemidentification
