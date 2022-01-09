from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyName(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Partyname'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Name'] = ('cbc', 'partyname', 'Zorunlu (1)')
        partyname_: Element = element.find('./' + cbcnamespace + 'Name')
        if partyname_ is None or partyname_.text is None:
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(partyname=partyname_.text))
