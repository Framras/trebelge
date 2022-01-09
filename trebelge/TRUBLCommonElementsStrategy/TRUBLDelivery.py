from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDeliveryTerms import TRUBLDeliveryTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLDespatch import TRUBLDespatch
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLDelivery(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Delivery'

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
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['Quantity'] = ('cbc', '', 'Seçimli (0...1)')
        quantity_: Element = element.find('./' + cbcnamespace + 'Quantity')
        if quantity_ is not None:
            if quantity_.text is not None:
                frappedoc['quantity'] = quantity_.text
                frappedoc['quantityunitcode'] = quantity_.attrib.get('unitCode')
        # ['DeliveryAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'DeliveryAddress')
        if tagelement_ is not None:
            tmp = TRUBLAddress().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['deliveryaddress'] = tmp.name
        # ['AlternativeDeliveryLocation'] = ('cac', 'Location', 'Seçimli (0...1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'AlternativeDeliveryLocation')
        if tagelement_ is not None:
            tmp = TRUBLLocation().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['alternativedeliverylocation'] = tmp.name
        # ['EstimatedDeliveryPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'EstimatedDeliveryPeriod')
        if tagelement_ is not None:
            tmp = TRUBLPeriod().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['estimateddeliveryperiod'] = tmp.name
        # ['CarrierParty'] = ('cac', 'Party', 'Seçimli (0...1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'CarrierParty')
        if tagelement_ is not None:
            tmp = TRUBLParty().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['carrierparty'] = tmp.name
        # ['DeliveryParty'] = ('cac', 'Party', 'Seçimli (0...1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'DeliveryParty')
        if tagelement_ is not None:
            tmp = TRUBLParty().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['deliveryparty'] = tmp.name
        # ['Despatch'] = ('cac', 'Despatch', 'Seçimli (0...1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'Despatch')
        if tagelement_ is not None:
            tmp = TRUBLDespatch().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['despatch'] = tmp.name
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...1)')
        tagelement_: Element = element.find('./' + cacnamespace + 'Shipment')
        if tagelement_ is not None:
            tmp = TRUBLShipment().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['shipment'] = tmp.name
        if frappedoc == {}:
            return None
        # ['DeliveryTerms'] = ('cac', 'DeliveryTerms', 'Seçimli (0...n)')
        deliveryterms = list()
        deliveryterms_: Element = element.find('./' + cacnamespace + 'DeliveryTerms')
        if deliveryterms_ is not None:
            for deliveryterm_ in deliveryterms_:
                tmp = TRUBLDeliveryTerms().process_element(deliveryterm_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    deliveryterms.append(tmp)
        if len(deliveryterms) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            document.deliveryterms = deliveryterms
            document.save()

        return document
