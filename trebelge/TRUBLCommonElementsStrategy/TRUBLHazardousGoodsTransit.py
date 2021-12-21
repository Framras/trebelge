from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTemperature import TRUBLTemperature


class TRUBLHazardousGoodsTransit(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR HazardousGoodsTransit'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

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
            field_: Element = element.find(cbcnamespace + elementtag_)
            if not field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text
        # ['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)')
        # ['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli(0..1)')
        cacsecimli01: list = \
            [{'Tag': 'MaximumTemperature', 'strategy': TRUBLTemperature(), 'fieldName': 'maximumtemperature'},
             {'Tag': 'MinimumTemperature', 'strategy': TRUBLTemperature(), 'fieldName': 'minimumtemperature'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find(cacnamespace + element_.get('Tag'))
            if not tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
