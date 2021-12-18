from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLBuildingNumber(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR BuildingNumber'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        frappedoc: dict = {'buildingnumber': element.find(cbcnamespace + 'BuildingNumber').text}

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
