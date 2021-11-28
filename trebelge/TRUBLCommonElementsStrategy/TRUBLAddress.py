from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCountry import TRUBLCountry


class TRUBLAddress(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        ['Postbox'] = ('cbc', 'postbox', 'Seçimli (0...1)')
        ['Room'] = ('cbc', 'room', 'Seçimli (0...1)')
        ['StreetName'] = ('cbc', 'streetname', 'Seçimli (0...1)')
        ['BlockName'] = ('cbc', 'blockname', 'Seçimli (0...1)')
        ['BuildingName'] = ('cbc', 'buildingname', 'Seçimli (0...1)')
        ['BuildingNumber'] = ('cbc', 'buildingnumbers', 'Seçimli(0..n)')
        ['CitySubdivisionName'] = ('cbc', 'citysubdivisionname', 'Zorunlu(1)')
        ['CityName'] = ('cbc', 'cityname', 'Zorunlu(1)')
        ['PostalZone'] = ('cbc', 'postalzone', 'Seçimli (0...1)')
        ['Region'] = ('cbc', 'region', 'Seçimli (0...1)')
        ['District'] = ('cbc', 'district', 'Seçimli (0...1)')
        ['Country'] = ('cac', Country(), 'Zorunlu(1)')
        """
        address: dict = {'citysubdivisionname': element.find(cbcnamespace + 'CitySubdivisionName').text,
                         'cityname': element.find(cbcnamespace + 'Name').text}
        country_ = element.find(cacnamespace + 'Country')
        strategy: TRUBLCommonElement = TRUBLCountry()
        self._strategyContext.set_strategy(strategy)
        country = self._strategyContext.return_element_data(country_, cbcnamespace,
                                                            cacnamespace)
        for key in country.keys():
            address['country_' + key] = country.get(key)
        cbcsecimli01: list = ['Postbox', 'Room', 'StreetName', 'BlockName', 'BuildingName', 'PostalZone', 'Region',
                              'District']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                address[field_.tag.lower()] = field_.text
        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            address['address' + id_.tag.lower()] = id_.text
        # TODO this is not implemented as Frappe doctype
        buildingnumbers_ = element.findall(cbcnamespace + 'BuildingNumber')
        if buildingnumbers_ is not None:
            buildingnumbers: list = []
            for buildingnumber in buildingnumbers_:
                buildingnumbers.append(buildingnumber.text)
            address['buildingnumbers'] = buildingnumbers

        return address
