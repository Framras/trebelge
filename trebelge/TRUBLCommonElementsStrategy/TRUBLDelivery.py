from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDespatch import TRUBLDespatch
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyLegalEntity import TRUBLPartyLegalEntity
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLDelivery(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Party'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Quantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDeliveryDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDeliveryTime'] = ('cbc', '', 'Seçimli(0..1)')
        # ['LatestDeliveryDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['LatestDeliveryTime'] = ('cbc', '', 'Seçimli(0..1)')
        # ['TrackingID'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['ID', 'Quantity', 'ActualDeliveryDate', 'ActualDeliveryTime', 'LatestDeliveryDate',
                              'LatestDeliveryTime', 'TrackingID']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['DeliveryAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        # ['AlternativeDeliveryLocation'] = ('cac', 'Location', 'Seçimli (0...1)')
        # ['EstimatedDeliveryPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        # ['CarrierParty'] = ('cac', 'Party', 'Seçimli (0...1)')
        # ['DeliveryParty'] = ('cac', 'Party', 'Seçimli (0...1)')
        # ['Despatch'] = ('cac', 'Despatch', 'Seçimli (0...1)')
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...1)')
        cacsecimli01: list = \
            [{'Tag': 'DeliveryAddress', 'strategy': TRUBLAddress(), 'fieldName': 'deliveryaddress'},
             {'Tag': 'AlternativeDeliveryLocation', 'strategy': TRUBLLocation(),
              'fieldName': 'alternativedeliverylocation'},
             {'Tag': 'EstimatedDeliveryPeriod', 'strategy': TRUBLPeriod(), 'fieldName': 'estimateddeliveryperiod'},
             {'Tag': 'CarrierParty', 'strategy': TRUBLParty(), 'fieldName': 'carrierparty'},
             {'Tag': 'DeliveryParty', 'strategy': TRUBLParty(), 'fieldName': 'deliveryparty'},
             {'Tag': 'Despatch', 'strategy': TRUBLDespatch(), 'fieldName': 'despatch'},
             {'Tag': 'Shipment', 'strategy': TRUBLShipment(), 'fieldName': 'shipment'}
             ]
        for element_ in cacsecimli01:
            tagelement_ = element.find(cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]

        # ['DeliveryTerms'] = ('cac', 'DeliveryTerms', 'Seçimli (0...n)')
        partylegalentity_ = element.find(cacnamespace + 'PartyLegalEntity')
        if partylegalentity_ is not None:
            strategy: TRUBLCommonElement = TRUBLPartyLegalEntity()
            self._strategyContext.set_strategy(strategy)
            partylegalentities: list = []
            for partylegalentity in partylegalentity_:
                partylegalentities.append(self._strategyContext.return_element_data(partylegalentity,
                                                                                    cbcnamespace,
                                                                                    cacnamespace))
            frappedoc['partylegalentity'] = partylegalentities

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
