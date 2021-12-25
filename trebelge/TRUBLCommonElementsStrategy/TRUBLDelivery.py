from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDeliveryTerms import TRUBLDeliveryTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLDespatch import TRUBLDespatch
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLDelivery(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Delivery'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDeliveryDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ActualDeliveryTime'] = ('cbc', '', 'Seçimli(0..1)')
        # ['LatestDeliveryDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['LatestDeliveryTime'] = ('cbc', '', 'Seçimli(0..1)')
        # ['TrackingID'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['ID', 'ActualDeliveryDate', 'ActualDeliveryTime', 'LatestDeliveryDate',
                              'LatestDeliveryTime', 'TrackingID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['Quantity'] = ('cbc', '', 'Seçimli (0...1)')
        # unitCode
        quantity_: Element = element.find('./' + cbcnamespace + 'Quantity')
        if quantity_ is not None:
            frappedoc['quantity'] = quantity_.text
            frappedoc['quantityunitcode'] = quantity_.attrib.get('unitCode')

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
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]
        # ['DeliveryTerms'] = ('cac', 'DeliveryTerms', 'Seçimli (0...n)')
        deliveryterms_: Element = element.find('./' + cacnamespace + 'DeliveryTerms')
        if deliveryterms_ is not None:
            deliveryterms: list = []
            strategy: TRUBLCommonElement = TRUBLDeliveryTerms()
            self._strategyContext.set_strategy(strategy)
            for deliveryterm_ in deliveryterms_:
                deliveryterms.append(self._strategyContext.return_element_data(deliveryterm_,
                                                                               cbcnamespace,
                                                                               cacnamespace))
            frappedoc['deliveryterms'] = deliveryterms

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
