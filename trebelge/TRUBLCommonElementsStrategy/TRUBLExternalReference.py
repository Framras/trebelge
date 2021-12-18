from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLExternalReference(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        """
        ['URI'] = ('cbc', '', 'Zorunlu(1)')
        """
        externalreference: dict = {'uri': element.find(cbcnamespace + 'URI').text}

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
