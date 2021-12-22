from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyIdentification(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR PartyIdentification'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        # ['schemeID'] = ('', 'schemeid', 'Zorunlu (1)')
        partyidentification_ = element.find(cbcnamespace + 'ID')
        frappedoc: dict = {'id': partyidentification_.text,
                           'schemeid': partyidentification_.attrib.get('schemeID')}

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
