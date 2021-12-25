from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAirTransport import TRUBLAirTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLMaritimeTransport import TRUBLMaritimeTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLRailTransport import TRUBLRailTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLRoadTransport import TRUBLRoadTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLStowage import TRUBLStowage


class TRUBLTransportMeans(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportMeans'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['JourneyID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RegistrationNationalityID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['DirectionCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TransportMeansTypeCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TradeServiceCode'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['JourneyID', 'RegistrationNationalityID', 'DirectionCode', 'TransportMeansTypeCode',
                              'TradeServiceCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[elementtag_.lower()] = field_.text
        # ['RegistrationNationality'] = ('cbc', 'registrationnationality', 'Seçimli (0...n)')
        registrationnationality_: list = element.findall('./' + cbcnamespace + 'RegistrationNationality')
        if registrationnationality_:
            registrationnationality: list = []
            for nationality_ in registrationnationality_:
                registrationnationality.append(nationality_.text)
            frappedoc['registrationnationality'] = registrationnationality
        # ['Stowage'] = ('cac', 'Stowage', 'Seçimli(0..1)')
        # ['AirTransport'] = ('cac', 'AirTransport', 'Seçimli(0..1)')
        # ['RoadTransport'] = ('cac', 'RoadTransport', 'Seçimli(0..1)')
        # ['RailTransport'] = ('cac', 'RailTransport', 'Seçimli(0..1)')
        # ['MaritimeTransport'] = ('cac', 'MaritimeTransport', 'Seçimli(0..1)')
        # ['OwnerParty'] = ('cac', 'Party', 'Seçimli(0..1)')
        cacsecimli01: list = \
            [{'Tag': 'Stowage', 'strategy': TRUBLStowage(), 'fieldName': 'stowage'},
             {'Tag': 'AirTransport', 'strategy': TRUBLAirTransport(), 'fieldName': 'airtransport'},
             {'Tag': 'RoadTransport', 'strategy': TRUBLRoadTransport(), 'fieldName': 'roadtransport'},
             {'Tag': 'RailTransport', 'strategy': TRUBLRailTransport(), 'fieldName': 'railtransport'},
             {'Tag': 'MaritimeTransport', 'strategy': TRUBLMaritimeTransport(), 'fieldName': 'maritimetransport'},
             {'Tag': 'OwnerParty', 'strategy': TRUBLParty(), 'fieldName': 'ownerparty'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)')
        measurementdimension_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if measurementdimension_:
            measurementdimension: list = []
            strategy: TRUBLCommonElement = TRUBLDimension()
            self._strategyContext.set_strategy(strategy)
            for dimension_ in measurementdimension_:
                measurementdimension.append(self._strategyContext.return_element_data(dimension_,
                                                                                      cbcnamespace,
                                                                                      cacnamespace))
            frappedoc['measurementdimension'] = measurementdimension

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
