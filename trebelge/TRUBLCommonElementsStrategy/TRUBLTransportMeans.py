from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAirTransport import TRUBLAirTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLMaritimeTransport import TRUBLMaritimeTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLRailTransport import TRUBLRailTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLRoadTransport import TRUBLRoadTransport
from trebelge.TRUBLCommonElementsStrategy.TRUBLStowage import TRUBLStowage


class TRUBLTransportMeans(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportMeans'

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
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['RegistrationNationality'] = ('cbc', 'registrationnationality', 'Seçimli (0...n)')
        registrationnationality_: list = element.findall('./' + cbcnamespace + 'RegistrationNationality')
        if registrationnationality_ is not None:
            registrationnationality: list = []
            for nationality_ in registrationnationality_:
                if nationality_.text is not None:
                    registrationnationality.append(nationality_.text)
            if len(registrationnationality) != 0:
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
            if tagelement_ is not None:
                tmp = element_.get('strategy').process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    frappedoc[element_.get('fieldName')] = tmp.name
        if frappedoc == {}:
            return None
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)')
        measurementdimension_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if measurementdimension_:
            measurementdimension: list = []
            for dimension_ in measurementdimension_:
                tmp = TRUBLDimension().process_element(dimension_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    measurementdimension.append(tmp)
            if len(measurementdimension) != 0:
                document.measurementdimension = measurementdimension
                document.save()

        return self._update_frappedoc(self._frappeDoctype, frappedoc, document)
