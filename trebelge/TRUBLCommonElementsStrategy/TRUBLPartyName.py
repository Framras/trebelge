from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyName(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Partyname'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Name'] = ('cbc', 'partyname', 'Zorunlu (1)')
        partyname_ = element.find('./' + cbcnamespace + 'Name').text
        if partyname_ is None:
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(partyname=partyname_))
