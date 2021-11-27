from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyIdentification(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        ['schemeID'] = ('', 'schemeid', 'Zorunlu (1)')
        """
        partyidentification_ = element.find(cbcnamespace + 'ID')
        partyidentification: dict = {'id': partyidentification_.text,
                                     'schemeid': partyidentification_.attrib.get('schemeID')
                                     }

        return partyidentification
