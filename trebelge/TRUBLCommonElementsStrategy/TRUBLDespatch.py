from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLDespatch(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Despatch'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDespatchDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDespatchTime'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Instructions'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['ID', 'ActualDespatchDate', 'ActualDespatchTime', 'Instructions']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['DespatchAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        # ['DespatchParty'] = ('cac', 'Party', 'Seçimli (0...1)')
        # ['Contact'] = ('cac', 'Contact', 'Seçimli (0...1)')
        # ['EstimatedDespatchPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        cacsecimli01: list = \
            [{'Tag': 'DespatchAddress', 'strategy': TRUBLAddress(), 'fieldName': 'despatchaddress'},
             {'Tag': 'DespatchParty', 'strategy': TRUBLParty(), 'fieldName': 'despatchparty'},
             {'Tag': 'Contact', 'strategy': TRUBLContact(), 'fieldName': 'contact'},
             {'Tag': 'EstimatedDespatchPeriod', 'strategy': TRUBLPeriod(), 'fieldName': 'estimateddespatchperiod'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_:
                frappedoc[element_.get('fieldName')] = element_.get('strategy').process_element(tagelement_,
                                                                                                cbcnamespace,
                                                                                                cacnamespace).name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
