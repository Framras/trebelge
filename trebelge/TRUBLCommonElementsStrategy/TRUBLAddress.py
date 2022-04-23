from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCountry import TRUBLCountry


class TRUBLAddress(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Address'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['CitySubdivisionName'] = ('cbc', 'citysubdivisionname', 'Zorunlu(1)')
        citysubdivisionname_: Element = element.find('./' + cbcnamespace + 'CitySubdivisionName')
        if citysubdivisionname_ is not None:
            if citysubdivisionname_.text is not None:
                frappedoc['citysubdivisionname'] = citysubdivisionname_.text.strip()
        # ['CityName'] = ('cbc', 'cityname', 'Zorunlu(1)')
        cityname_: Element = element.find('./' + cbcnamespace + 'CityName')
        if cityname_ is not None:
            if cityname_.text is not None:
                frappedoc['cityname'] = cityname_.text.strip()
        # ['Country'] = ('cac', Country(), 'Zorunlu(1)')
        country_: Element = element.find('./' + cacnamespace + 'Country')
        tmp = TRUBLCountry().process_element(country_, cbcnamespace, cacnamespace)
        if tmp is not None:
            frappedoc['country'] = tmp.name
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
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        buildingnumbers = list()
        buildingnumbers_: list = element.findall('./' + cbcnamespace + 'BuildingNumber')
        if len(buildingnumbers_) == 0:
            return self._get_frappedoc(self._frappeDoctype, frappedoc)
        for buildingnumber in buildingnumbers_:
            if buildingnumber is not None:
                if buildingnumber.text is not None:
                    if buildingnumber.text.strip() != '':
                        buildingnumbers.append(buildingnumber.text.strip())
        if len(buildingnumbers) == 0:
            return self._get_frappedoc(self._frappeDoctype, frappedoc)
        if len(frappe.get_all(self._frappeDoctype, filters=frappedoc)) != 0:
            legacy_: Document = frappe.get_doc(self._frappeDoctype,
                                               frappe.get_all(self._frappeDoctype,
                                                              filters=frappedoc)[0]["name"])
            if legacy_ is not None:
                if len(legacy_.get_value('buildingnumber')) != 0 and len(legacy_.get_value('buildingnumber')) == len(
                        buildingnumbers):
                    for bnumber in legacy_.get_value('buildingnumber'):
                        if buildingnumbers.count(bnumber.buildingnumber) == 0:
                            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
                            doc_append = document.append("buildingnumber", {})
                            for buildingnumber in buildingnumbers:
                                doc_append.buildingnumber = buildingnumber
                                document.save()
                            return document
                return legacy_
        if frappedoc == {}:
            return None
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        doc_append = document.append("buildingnumber", {})
        for buildingnumber_ in buildingnumbers:
            doc_append.buildingnumber = buildingnumber_
            document.save()
        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
