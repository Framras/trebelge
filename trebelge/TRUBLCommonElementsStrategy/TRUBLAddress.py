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
            if country.get(key) is not None:
                address['country_' + key] = country.get(key)
        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            address[id_.tag.lower()] = id_.text
        postbox_ = element.find(cbcnamespace + 'Postbox')
        if postbox_ is not None:
            address[postbox_.tag.lower()] = postbox_.text
        room_ = element.find(cbcnamespace + 'Room')
        if room_ is not None:
            address[room_.tag.lower()] = room_.text
        streetname_ = element.find(cbcnamespace + 'StreetName')
        if streetname_ is not None:
            address[streetname_.tag.lower()] = streetname_.text
        blockname_ = element.find(cbcnamespace + 'BlockName')
        if blockname_ is not None:
            address[blockname_.tag.lower()] = blockname_.text
        buildingname_ = element.find(cbcnamespace + 'BuildingName')
        if buildingname_ is not None:
            address[buildingname_.tag.lower()] = buildingname_.text
        # TODO this is not implemented as Frappe doctype
        buildingnumbers_ = element.findall(cbcnamespace + 'BuildingNumber')
        if buildingnumbers_ is not None:
            buildingnumbers: list = []
            for buildingnumber in buildingnumbers_:
                buildingnumbers.append(buildingnumber.text)
            address['buildingnumbers'] = buildingnumbers
        postalzone_ = element.find(cbcnamespace + 'PostalZone')
        if postalzone_ is not None:
            address[postalzone_.tag.lower()] = postalzone_.text
        region_ = element.find(cbcnamespace + 'Region')
        if region_ is not None:
            address[region_.tag.lower()] = region_.text
        district_ = element.find(cbcnamespace + 'District')
        if district_ is not None:
            address[district_.tag.lower()] = district_.text

        return address
