from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLCustomsDeclaration(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CustomsDeclaration'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text}
        # ['IssuerParty'] = ('cac', 'Party', 'Seçimli(0..1)', 'issuerparty')
        issuerparty_: Element = element.find('./' + cacnamespace + 'IssuerParty')
        if issuerparty_:
            frappedoc['issuerparty'] = TRUBLParty().process_element(issuerparty_,
                                                                    cbcnamespace,
                                                                    cacnamespace).name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
