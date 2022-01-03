from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLCustomsDeclaration(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CustomsDeclaration'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        id_ = element.find('./' + cbcnamespace + 'ID').text
        if id_ is None:
            return None
        frappedoc: dict = {'id': id_}
        # ['IssuerParty'] = ('cac', 'Party', 'Seçimli(0..1)', 'issuerparty')
        issuerparty_: Element = element.find('./' + cacnamespace + 'IssuerParty')
        if issuerparty_ is not None:
            tmp = TRUBLParty().process_element(issuerparty_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['issuerparty'] = tmp.name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
