from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyName(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['Name'] = ('cbc', 'partyname', 'Zorunlu (1)')
        """
        partyname: dict = {'partyname': element.find(cbcnamespace + 'Name')}

        return partyname
