from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLPerson import TRUBLPerson
from trebelge.TRUBLCommonElementsStrategy.TRUBLTransportMeans import TRUBLTransportMeans


class TRUBLShipmentStage(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ShipmentStage'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TransportModeCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TransportMeansTypeCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Instructions'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'TransportModeCode', 'TransportMeansTypeCode', 'Instructions']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['TransitDirectionCode'] = ('cbc', '', 'Seçimli (0...n)')
        transitdirectioncodes_: list = element.findall('./' + cbcnamespace + 'TransitDirectionCode')
        if transitdirectioncodes_:
            transitdirectioncode: list = []
            for transitdirectioncode_ in transitdirectioncodes_:
                transitdirectioncode.append(transitdirectioncode_.text)
            frappedoc['transitdirectioncode'] = transitdirectioncode
        # ['TransitPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        transitperiod_: Element = element.find('./' + cbcnamespace + 'TransitPeriod')
        if transitperiod_:
            strategy: TRUBLCommonElement = TRUBLPeriod()
            self._strategyContext.set_strategy(strategy)
            frappedoc['transitperiod'] = [self._strategyContext.return_element_data(transitperiod_,
                                                                                    cbcnamespace,
                                                                                    cacnamespace)]
        # ['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...1)')
        transportmeans_: Element = element.find('./' + cbcnamespace + 'TransportMeans')
        if transportmeans_:
            strategy: TRUBLCommonElement = TRUBLTransportMeans()
            self._strategyContext.set_strategy(strategy)
            frappedoc['transportmeans'] = [self._strategyContext.return_element_data(transportmeans_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)]
        # ['DriverPerson'] = ('cac', 'Person', 'Seçimli (0...n)')
        driverpeople_: list = element.findall('./' + cacnamespace + 'DriverPerson')
        if driverpeople_:
            driverpeople: list = []
            strategy: TRUBLCommonElement = TRUBLPerson()
            self._strategyContext.set_strategy(strategy)
            for driverperson_ in driverpeople_:
                driverpeople.append(self._strategyContext.return_element_data(driverperson_,
                                                                              cbcnamespace,
                                                                              cacnamespace))
            frappedoc['driverperson'] = driverpeople

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
