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
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['DespatchAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        despatchaddress_: Element = element.find('./' + cacnamespace + 'DespatchAddress')
        if despatchaddress_ is not None:
            tmp: Document = TRUBLAddress().process_element(despatchaddress_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['despatchaddress'] = tmp.name
        # ['DespatchParty'] = ('cac', 'Party', 'Seçimli (0...1)')
        despatchparty_: Element = element.find('./' + cacnamespace + 'DespatchParty')
        if despatchparty_ is not None:
            tmp: Document = TRUBLParty().process_element(despatchparty_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['despatchparty'] = tmp.name
        # ['Contact'] = ('cac', 'Contact', 'Seçimli (0...1)')
        contact_: Element = element.find('./' + cacnamespace + 'Contact')
        if contact_ is not None:
            tmp: Document = TRUBLContact().process_element(contact_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['contact'] = tmp.name
        # ['EstimatedDespatchPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        estimateddespatchperiod_: Element = element.find('./' + cacnamespace + 'EstimatedDespatchPeriod')
        if estimateddespatchperiod_ is not None:
            tmp: dict = TRUBLPeriod().process_elementasdict(estimateddespatchperiod_, cbcnamespace, cacnamespace)
            if tmp != {}:
                for key in ['startdate', 'starttime', 'enddate', 'endtime', 'durationmeasure',
                            'durationmeasure_unitcode', 'description']:
                    try:
                        frappedoc[key] = tmp[key]
                    except KeyError:
                        pass
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
