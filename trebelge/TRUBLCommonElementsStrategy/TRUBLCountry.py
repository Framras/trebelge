from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCountry(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['IdentificationCode'] = ('cbc', 'identificationcode', 'Seçimli (0...1)')
        ['Name'] = ('cbc', 'name', 'Zorunlu(1)')
        """
        country: dict = {'name': element.find(cbcnamespace + 'Name').text}
        identificationcode_ = element.find(cbcnamespace + 'IdentificationCode')
        if identificationcode_ is not None:
            country['identificationcode'] = identificationcode_.text

        return country
