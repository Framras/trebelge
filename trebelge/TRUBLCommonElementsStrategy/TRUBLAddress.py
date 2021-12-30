from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLBuildingNumber import TRUBLBuildingNumber
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCountry import TRUBLCountry


class TRUBLAddress(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Address'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['CitySubdivisionName'] = ('cbc', 'citysubdivisionname', 'Zorunlu(1)')
        # ['CityName'] = ('cbc', 'cityname', 'Zorunlu(1)')
        citysubdivisionname = element.find('./' + cbcnamespace + 'CitySubdivisionName')
        if citysubdivisionname:
            frappedoc['citysubdivisionname'] = citysubdivisionname.text
        else:
            frappe.log_error('citysubdivisionname not provided for ' + element.tag, 'TRUBLAddress')
            frappedoc['citysubdivisionname'] = str(' ')
        cityname = element.find('./' + cbcnamespace + 'CityName')
        if cityname:
            frappedoc['cityname'] = cityname.text
        else:
            frappe.log_error('cityname not provided for ' + element.tag, 'TRUBLAddress')
            frappedoc['cityname'] = str(' ')
        # ['Country'] = ('cac', Country(), 'Zorunlu(1)')
        country_: Element = element.find('./' + cacnamespace + 'Country')
        frappedoc['country'] = TRUBLCountry().process_element(country_,
                                                              cbcnamespace,
                                                              cacnamespace).name
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
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        buildingnumbers_: list = element.findall('./' + cbcnamespace + 'BuildingNumber')
        if len(buildingnumbers_) != 0:
            buildingnumbers: list = []
            for buildingnumber in buildingnumbers_:
                buildingnumbers.append(TRUBLBuildingNumber().process_element(buildingnumber,
                                                                             cbcnamespace,
                                                                             cacnamespace))
            document.buildingnumber = buildingnumbers
        document.save()

        return document
