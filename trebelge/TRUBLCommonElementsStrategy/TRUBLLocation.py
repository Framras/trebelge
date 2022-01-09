from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLLocation(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Location'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None and id_.text is not None:
            frappedoc['locationid'] = id_.text
        # ['Address'] = ('cac', 'Address()', 'Seçimli (0...1)','address')
        address_: Element = element.find('./' + cacnamespace + 'Address')
        if address_ is not None:
            tmp = TRUBLAddress().process_element(address_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['address'] = tmp.name
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)
