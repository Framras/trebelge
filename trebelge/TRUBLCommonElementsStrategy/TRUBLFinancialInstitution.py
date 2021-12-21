from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLFinancialInstitution(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR FinancialInstitution'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Name'] = ('cbc', 'name', 'Seçimli(0..1)', 'financialinstitution')
        frappedoc: dict = {}
        name_: Element = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc['financialinstitution'] = name_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
