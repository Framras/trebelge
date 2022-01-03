from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTemperature import TRUBLTemperature


class TRUBLHazardousGoodsTransit(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR HazardousGoodsTransit'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['TransportEmergencyCardCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['PackagingCriteriaCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['HazardousRegulationCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['InhalationToxicityZoneCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['TransportAuthorizationCode'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['TransportEmergencyCardCode', 'PackagingCriteriaCode', 'HazardousRegulationCode',
                              'InhalationToxicityZoneCode', 'TransportAuthorizationCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'MaximumTemperature')
        if tagelement_ is not None:
            tmp = TRUBLTemperature().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['maximumtemperature'] = tmp.name
        # ['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'MinimumTemperature')
        if tagelement_ is not None:
            tmp = TRUBLTemperature().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['minimumtemperature'] = tmp.name
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)
