from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact


class TRUBLSupplierParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR SupplierParty'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = element.find('./' + cacnamespace + 'Party')
        tmp = TRUBLParty().process_element(party_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc: dict = dict(party=tmp.name)
        # ['DespatchContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'despatchcontact')
        despatchcontact_: Element = element.find('./' + cacnamespace + 'DespatchContact')
        if despatchcontact_ is not None:
            tmp = TRUBLContact().process_element(despatchcontact_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['despatchcontact'] = tmp.name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
