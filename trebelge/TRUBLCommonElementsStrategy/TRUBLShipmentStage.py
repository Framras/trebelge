from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLPerson import TRUBLPerson
from trebelge.TRUBLCommonElementsStrategy.TRUBLTransportMeans import TRUBLTransportMeans


class TRUBLShipmentStage(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ShipmentStage'

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
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['TransitDirectionCode'] = ('cbc', '', 'Seçimli (0...n)')
        transitdirectioncodes_: list = element.findall('./' + cbcnamespace + 'TransitDirectionCode')
        if len(transitdirectioncodes_) != 0:
            transitdirectioncode: list = []
            for transitdirectioncode_ in transitdirectioncodes_:
                if transitdirectioncode_.text is not None:
                    transitdirectioncode.append(transitdirectioncode_.text)
            if len(transitdirectioncode) != 0:
                frappedoc['transitdirectioncode'] = transitdirectioncode
        # ['TransitPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        transitperiod_: Element = element.find('./' + cbcnamespace + 'TransitPeriod')
        if transitperiod_ is not None:
            tmp = TRUBLPeriod.process_element(transitperiod_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['transitperiod'] = tmp.name
        # ['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...1)')
        transportmeans_: Element = element.find('./' + cbcnamespace + 'TransportMeans')
        if transportmeans_ is not None:
            tmp = TRUBLTransportMeans().process_element(transportmeans_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['transportmeans'] = tmp.name
        if frappedoc == {}:
            return None
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['DriverPerson'] = ('cac', 'Person', 'Seçimli (0...n)')
        driverpeople_: list = element.findall('./' + cacnamespace + 'DriverPerson')
        if len(driverpeople_) != 0:
            driverpeople: list = []
            for driverperson_ in driverpeople_:
                tmp = TRUBLPerson().process_element(driverperson_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    driverpeople.append(tmp)
            if len(driverpeople) != 0:
                document.driverperson = driverpeople
                document.save()

        return self._update_frappedoc(self._frappeDoctype, frappedoc, document)
