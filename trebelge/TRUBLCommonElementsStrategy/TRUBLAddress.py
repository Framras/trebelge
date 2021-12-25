from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLBuildingNumber import TRUBLBuildingNumber
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCountry import TRUBLCountry


class TRUBLAddress(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Address'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['CitySubdivisionName'] = ('cbc', 'citysubdivisionname', 'Zorunlu(1)')
        # ['CityName'] = ('cbc', 'cityname', 'Zorunlu(1)')
        frappedoc: dict = {'citysubdivisionname': element.find('./' + cbcnamespace + 'CitySubdivisionName').text,
                           'cityname': element.find('./' + cbcnamespace + 'CityName').text}
        # ['Country'] = ('cac', Country(), 'Zorunlu(1)')
        country_: Element = element.find('./' + cacnamespace + 'Country')
        strategy: TRUBLCommonElement = TRUBLCountry()
        self._strategyContext.set_strategy(strategy)
        frappedoc['country'] = [self._strategyContext.return_element_data(country_,
                                                                          cbcnamespace,
                                                                          cacnamespace)]
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['Postbox'] = ('cbc', 'postbox', 'Seçimli (0...1)')
        # ['Room'] = ('cbc', 'room', 'Seçimli (0...1)')
        # ['StreetName'] = ('cbc', 'streetname', 'Seçimli (0...1)')
        # ['BlockName'] = ('cbc', 'blockname', 'Seçimli (0...1)')
        # ['BuildingName'] = ('cbc', 'buildingname', 'Seçimli (0...1)')
        # ['PostalZone'] = ('cbc', 'postalzone', 'Seçimli (0...1)')
        # ['Region'] = ('cbc', 'region', 'Seçimli (0...1)')
        # ['District'] = ('cbc', 'district', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'Postbox', 'Room', 'StreetName', 'BlockName', 'BuildingName', 'PostalZone',
                              'Region', 'District']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[elementtag_.lower()] = field_.text
        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        buildingnumbers_: list = element.findall('./' + cbcnamespace + 'BuildingNumber')
        if buildingnumbers_:
            buildingnumbers: list = []
            strategy: TRUBLCommonElement = TRUBLBuildingNumber()
            self._strategyContext.set_strategy(strategy)
            for buildingnumber in buildingnumbers_:
                buildingnumbers.append(self._strategyContext.return_element_data(buildingnumber,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
            frappedoc['buildingnumber'] = buildingnumbers

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
