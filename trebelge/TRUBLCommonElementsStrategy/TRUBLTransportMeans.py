from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialAccount import TRUBLFinancialAccount


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
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['RegistrationNationality'] = ('cbc', '', 'Seçimli (0...n)')

        # ['Stowage'] = ('cac', 'Stowage', 'Seçimli(0..1)')
        # ['AirTransport'] = ('cac', 'AirTransport', 'Seçimli(0..1)')
        # ['RoadTransport'] = ('cac', 'RoadTransport', 'Seçimli(0..1)')
        # ['RailTransport'] = ('cac', 'RailTransport', 'Seçimli(0..1)')
        # ['MaritimeTransport'] = ('cac', 'MaritimeTransport', 'Seçimli(0..1)')
        # ['OwnerParty'] = ('cac', 'Party', 'Seçimli(0..1)')

        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)')

        # ['FinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)', 'financialaccount')
        financialaccount_ = element.find(cacnamespace + 'FinancialAccount')
        if financialaccount_ is not None:
            strategy: TRUBLCommonElement = TRUBLFinancialAccount()
            self._strategyContext.set_strategy(strategy)
            frappedoc['financialaccount'] = self._strategyContext.return_element_data(financialaccount_,
                                                                                      cbcnamespace,
                                                                                      cacnamespace)
        # ['IdentityDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)', 'documentreference')
        documentreference_ = element.find(cacnamespace + 'IdentityDocumentReference')
        if documentreference_ is not None:
            strategy: TRUBLCommonElement = TRUBLDocumentReference()
            self._strategyContext.set_strategy(strategy)
            frappedoc['documentreference'] = self._strategyContext.return_element_data(documentreference_,
                                                                                       cbcnamespace,
                                                                                       cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
