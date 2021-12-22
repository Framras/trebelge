from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLGoodsItem import TRUBLGoodsItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipmentStage import TRUBLShipmentStage
from trebelge.TRUBLCommonElementsStrategy.TRUBLTransportHandlingUnit import TRUBLTransportHandlingUnit

from apps.trebelge.trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote


class TRUBLShipment(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Shipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find(cbcnamespace + 'ID').text}
        # ['HandlingCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['HandlingInstructions'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['HandlingCode', 'HandlingInstructions']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['GrossWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossweightmeasure_: Element = element.find(cbcnamespace + 'GrossWeightMeasure')
        if grossweightmeasure_:
            frappedoc['grossweightmeasure'] = grossweightmeasure_.text
            frappedoc['grossweightmeasureunitcode'] = grossweightmeasure_.attrib.get('unitCode')
        # ['NetWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netweightmeasure_: Element = element.find(cbcnamespace + 'NetWeightMeasure')
        if netweightmeasure_:
            frappedoc['netweightmeasure'] = netweightmeasure_.text
            frappedoc['netweightmeasureunitcode'] = netweightmeasure_.attrib.get('unitCode')
        # ['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossvolumemeasure_: Element = element.find(cbcnamespace + 'GrossVolumeMeasure')
        if grossvolumemeasure_:
            frappedoc['grossvolumemeasure'] = grossvolumemeasure_.text
            frappedoc['grossvolumemeasureunitcode'] = grossvolumemeasure_.attrib.get('unitCode')
        # ['NetVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netvolumemeasure_: Element = element.find(cbcnamespace + 'NetVolumeMeasure')
        if netvolumemeasure_:
            frappedoc['netvolumemeasure'] = netvolumemeasure_.text
            frappedoc['netvolumemeasureunitcode'] = netvolumemeasure_.attrib.get('unitCode')
        # ['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totalgoodsitemquantity_: Element = element.find(cbcnamespace + 'TotalGoodsItemQuantity')
        if totalgoodsitemquantity_:
            frappedoc['totalgoodsitemquantity'] = totalgoodsitemquantity_.text
            frappedoc['totalgoodsitemquantityunitcode'] = totalgoodsitemquantity_.attrib.get('unitCode')
        # ['TotalTransportHandlingUnitQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totaltransporthandlingunitquantity_: Element = element.find(cbcnamespace + 'TotalTransportHandlingUnitQuantity')
        if totaltransporthandlingunitquantity_:
            frappedoc['totaltransporthandlingunitquantity'] = totaltransporthandlingunitquantity_.text
            frappedoc['totaltransporthandlingunitquantityunitcode'] = totaltransporthandlingunitquantity_.attrib.get(
                'unitCode')
        # ['InsuranceValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        insurancevalueamount_: Element = element.find(cbcnamespace + 'InsuranceValueAmount')
        if insurancevalueamount_:
            frappedoc['insurancevalueamount'] = insurancevalueamount_.text
            frappedoc['insurancevalueamountcurrencyid'] = insurancevalueamount_.attrib.get('currencyID')
        # ['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredcustomsvalueamount_: Element = element.find(cbcnamespace + 'DeclaredCustomsValueAmount')
        if declaredcustomsvalueamount_:
            frappedoc['declaredcustomsvalueamount'] = declaredcustomsvalueamount_.text
            frappedoc['declaredcustomsvalueamountcurrencyid'] = declaredcustomsvalueamount_.attrib.get('currencyID')
        # ['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredforcarriagevalueamount_: Element = element.find(cbcnamespace + 'DeclaredCustomsValueAmount')
        if declaredforcarriagevalueamount_:
            frappedoc['declaredforcarriagevalueamount'] = declaredforcarriagevalueamount_.text
            frappedoc['declaredforcarriagevalueamountcurrencyid'] = declaredforcarriagevalueamount_.attrib.get(
                'currencyID')
        # ['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredstatisticsvalueamount_: Element = element.find(cbcnamespace + 'DeclaredStatisticsValueAmount')
        if declaredstatisticsvalueamount_:
            frappedoc['declaredstatisticsvalueamount'] = declaredstatisticsvalueamount_.text
            frappedoc['declaredstatisticsvalueamountcurrencyid'] = declaredstatisticsvalueamount_.attrib.get(
                'currencyID')
        # ['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        freeonboardvalueamount_: Element = element.find(cbcnamespace + 'FreeOnBoardValueAmount')
        if freeonboardvalueamount_:
            frappedoc['freeonboardvalueamount'] = freeonboardvalueamount_.text
            frappedoc['freeonboardvalueamountcurrencyid'] = freeonboardvalueamount_.attrib.get('currencyID')
        # ['SpecialInstructions'] = ('cbc', '', 'Seçimli (0...n)')
        descriptions_: list = element.findall(cbcnamespace + 'SpecialInstructions')
        if descriptions_:
            descriptions: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for description_ in descriptions_:
                descriptions.append(self._strategyContext.return_element_data(description_,
                                                                              cbcnamespace,
                                                                              cacnamespace))
            frappedoc['specialinstructions'] = descriptions
        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...1)')
        # ['ReturnAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        # ['FirstArrivalPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')
        # ['LastExitPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')
        cacsecimli01: list = \
            [{'Tag': 'Delivery', 'strategy': TRUBLDelivery(), 'fieldName': 'delivery'},
             {'Tag': 'ReturnAddress', 'strategy': TRUBLAddress(), 'fieldName': 'returnaddress'},
             {'Tag': 'FirstArrivalPortLocation', 'strategy': TRUBLLocation(), 'fieldName': 'firstarrivalportlocation'},
             {'Tag': 'LastExitPortLocation', 'strategy': TRUBLLocation(), 'fieldName': 'lastexitportlocation'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find(cacnamespace + element_.get('Tag'))
            if tagelement_:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]
        # ['GoodsItem'] = ('cac', 'GoodsItem', 'Seçimli (0...n)')
        # ['ShipmentStage'] = ('cac', 'ShipmentStage', 'Seçimli (0...n)')
        # ['TransportHandlingUnit'] = ('cac', 'TransportHandlingUnit', 'Seçimli (0...n)')
        cacsecimli0n: list = \
            [{'Tag': 'GoodsItem', 'strategy': TRUBLGoodsItem(), 'fieldName': 'goodsitem'},
             {'Tag': 'ShipmentStage', 'strategy': TRUBLShipmentStage(), 'fieldName': 'shipmentstage'},
             {'Tag': 'TransportHandlingUnit', 'strategy': TRUBLTransportHandlingUnit(),
              'fieldName': 'transporthandlingunit'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall(cacnamespace + element_.get('Tag'))
            if tagelements_:
                tagelements: list = []
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                for tagelement in tagelements_:
                    tagelements.append(self._strategyContext.return_element_data(tagelement,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
