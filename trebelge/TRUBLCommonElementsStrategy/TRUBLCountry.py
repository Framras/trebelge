from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCountry(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str):
        """
        ['IdentificationCode'] = ('cbc', 'identificationcode', 'Seçimli (0...1)')
        ['Name'] = ('cbc', 'name', 'Zorunlu(1)')
        """
        country: dict = {('Country' + 'Name').lower(): element.find(cbcnamespace + 'Name').text}
        identificationcode_ = element.find(cbcnamespace + 'IdentificationCode')
        if identificationcode_ is not None:
            country[identificationcode_.tag.lower()] = identificationcode_.text

        return country
