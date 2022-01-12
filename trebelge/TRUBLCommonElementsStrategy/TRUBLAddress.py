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
        # ['CityName'] = ('cbc', 'cityname', 'Zorunlu(1)')
        cityname_: Element = element.find('./' + cbcnamespace + 'CityName')
        # ['Country'] = ('cac', Country(), 'Zorunlu(1)')
        country_: Element = element.find('./' + cacnamespace + 'Country')
        tmp = TRUBLCountry().process_element(country_, cbcnamespace, cacnamespace)
        if citysubdivisionname_.text is None and cityname_.text is None and tmp is None:
            return None
        if tmp is not None:
            frappedoc['country'] = tmp.name
        if citysubdivisionname_ is not None:
            frappedoc['citysubdivisionname'] = citysubdivisionname_.text
        if cityname_ is not None:
            frappedoc['cityname'] = cityname_.text
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
            if field_ is not None and field_.text is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['BuildingNumber'] = ('cbc', 'buildingnumber', 'Seçimli(0..n)')
        buildingnumbers = list()
        buildingnumbers_: list = element.findall('./' + cbcnamespace + 'BuildingNumber')
        if len(buildingnumbers_) == 0:
            return self._get_frappedoc(self._frappeDoctype, frappedoc)
        for buildingnumber in buildingnumbers_:
            if buildingnumber.text is not None and buildingnumber.text.strip() != '':
                buildingnumbers.append(buildingnumber.text)
        if len(buildingnumbers) == 0:
            return self._get_frappedoc(self._frappeDoctype, frappedoc)
        if len(frappe.get_all(self._frappeDoctype, filters=frappedoc)) != 0:
            legacy_: Document = frappe.get_doc(self._frappeDoctype,
                                               frappe.get_all(self._frappeDoctype,
                                                              filters=frappedoc)[0]["name"])
            if legacy_ is not None:
                if len(legacy_.buildingnumber) != 0 and len(legacy_.buildingnumber) == len(buildingnumbers):
                    for bnumber in legacy_.buildingnumber:
                        if buildingnumbers.count(bnumber.buildingnumber) == 0:
                            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
                            document.buildingnumber = buildingnumbers
                            document.save()
                            return document
                return legacy_
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        for buildingnumber_ in buildingnumbers:
            doc_append = document.append("buildingnumber", {})
            doc_append.buildingnumber = buildingnumber_
            document.save()
        return document
