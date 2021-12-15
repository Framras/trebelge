from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLBuildingNumber import TRUBLBuildingNumber
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCountry import TRUBLCountry


class TRUBLAddress(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Address'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['CitySubdivisionName'] = ('cbc', 'citysubdivisionname', 'Zorunlu(1)')
        # ['CityName'] = ('cbc', 'cityname', 'Zorunlu(1)')
        frappedoc: dict = {'citysubdivisionname': element.find(cbcnamespace + 'CitySubdivisionName').text,
                           'cityname': element.find(cbcnamespace + 'CityName').text}

        # ['Country'] = ('cac', Country(), 'Zorunlu(1)')
        country_ = element.find(cacnamespace + 'Country')
        strategy: TRUBLCommonElement = TRUBLCountry()
        self._strategyContext.set_strategy(strategy)
        country = frappe.get_doc(
            'UBL TR Country',
            self._strategyContext.return_element_data(country_, cbcnamespace,
                                                      cacnamespace)[0]['name'])
        frappedoc['country'] = [country]

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
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        buildingnumbers_ = element.findall(cbcnamespace + 'BuildingNumber')
        if buildingnumbers_ is not None:
            buildingnumbers: list = []
            strategy: TRUBLCommonElement = TRUBLBuildingNumber()
            self._strategyContext.set_strategy(strategy)
            for buildingnumber in buildingnumbers_:
                buildingnumbers.append(frappe.get_doc(
                    'UBL TR BuildingNumber',
                    self._strategyContext.return_element_data(buildingnumber, cbcnamespace,
                                                              cacnamespace)[0]['name']))
            frappedoc['buildingnumber'] = buildingnumbers

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
