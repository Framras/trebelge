from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLBuildingNumber import TRUBLBuildingNumber
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCountry import TRUBLCountry


class TRUBLAddress(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Address'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['CitySubdivisionName'] = ('cbc', 'citysubdivisionname', 'Zorunlu(1)')
        citysubdivisionname_ = element.find('./' + cbcnamespace + 'CitySubdivisionName').text
        # ['CityName'] = ('cbc', 'cityname', 'Zorunlu(1)')
        cityname_ = element.find('./' + cbcnamespace + 'CityName').text
        # ['Country'] = ('cac', Country(), 'Zorunlu(1)')
        country_: Element = element.find('./' + cacnamespace + 'Country')
        tmp = TRUBLCountry().process_element(country_, cbcnamespace, cacnamespace)
        if tmp is None and citysubdivisionname_ is None and cityname_ is None:
            return None
        if tmp is not None:
            frappedoc['country'] = tmp.name
        if citysubdivisionname_ is not None:
            frappedoc['citysubdivisionname'] = citysubdivisionname_
        if cityname_ is not None:
            frappedoc['cityname'] = cityname_
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
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        buildingnumbers_: list = element.findall('./' + cbcnamespace + 'BuildingNumber')
        if len(buildingnumbers_) != 0:
            buildingnumbers: list = []
            for buildingnumber in buildingnumbers_:
                tmp = TRUBLBuildingNumber().process_element(buildingnumber, cbcnamespace, cacnamespace)
                if tmp is not None:
                    buildingnumbers.append(tmp)
            if len(buildingnumbers) != 0:
                frappedoc['buildingnumber'] = buildingnumbers
                document.buildingnumber = buildingnumbers
                document.save()

        return self._update_frappedoc(self._frappeDoctype, frappedoc, document)
