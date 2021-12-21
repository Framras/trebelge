from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCustomsDeclaration(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CustomsDeclaration'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find(cbcnamespace + 'ID').text}
        # ['IssuerParty'] = ('cac', 'Party', 'Seçimli(0..1)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
