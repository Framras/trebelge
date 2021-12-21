from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLDespatch(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Despatch'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDespatchDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDespatchTime'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Instructions'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['ID', 'ActualDespatchDate', 'ActualDespatchTime', 'Instructions']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text
        # ['DespatchAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        # ['DespatchParty'] = ('cac', 'Party', 'Seçimli (0...1)')
        # ['Contact'] = ('cac', 'Contact', 'Seçimli (0...1)')
        # ['EstimatedDespatchPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        cacsecimli01: list = \
            [{'Tag': 'DespatchAddress', 'strategy': TRUBLAddress(), 'docType': 'UBL TR Address',
              'fieldName': 'despatchaddress'},
             {'Tag': 'DespatchParty', 'strategy': TRUBLParty(), 'docType': 'UBL TR Party',
              'fieldName': 'despatchparty'},
             {'Tag': 'Contact', 'strategy': TRUBLContact(), 'docType': 'UBL TR Contact', 'fieldName': 'contact'},
             {'Tag': 'EstimatedDespatchPeriod', 'strategy': TRUBLPeriod(), 'docType': 'UBL TR Period',
              'fieldName': 'estimateddespatchperiod'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find(cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
