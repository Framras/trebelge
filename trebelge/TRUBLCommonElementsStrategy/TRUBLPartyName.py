from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyName(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Partyname'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['Name'] = ('cbc', 'partyname', 'Zorunlu (1)')
        partyname: dict = {'partyname': element.find(cbcnamespace + 'Name')}

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
