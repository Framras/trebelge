from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLGoodsItem import TRUBLGoodsItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipmentStage import TRUBLShipmentStage
from trebelge.TRUBLCommonElementsStrategy.TRUBLTransportHandlingUnit import TRUBLTransportHandlingUnit


class TRUBLShipment(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Shipment'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        id_ = element.find('./' + cbcnamespace + 'ID').text
        if id_ is not None:
            frappedoc: dict = {'id': id_}
        else:
            return None
        # ['HandlingCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['HandlingInstructions'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['HandlingCode', 'HandlingInstructions']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['GrossWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossweightmeasure_: Element = element.find('./' + cbcnamespace + 'GrossWeightMeasure')
        if grossweightmeasure_ is not None:
            if grossweightmeasure_.text is not None:
                frappedoc['grossweightmeasure'] = grossweightmeasure_.text
                frappedoc['grossweightmeasureunitcode'] = grossweightmeasure_.attrib.get('unitCode')
        # ['NetWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netweightmeasure_: Element = element.find('./' + cbcnamespace + 'NetWeightMeasure')
        if netweightmeasure_ is not None:
            if netweightmeasure_.text is not None:
                frappedoc['netweightmeasure'] = netweightmeasure_.text
                frappedoc['netweightmeasureunitcode'] = netweightmeasure_.attrib.get('unitCode')
        # ['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossvolumemeasure_: Element = element.find('./' + cbcnamespace + 'GrossVolumeMeasure')
        if grossvolumemeasure_ is not None:
            if grossvolumemeasure_.text is not None:
                frappedoc['grossvolumemeasure'] = grossvolumemeasure_.text
                frappedoc['grossvolumemeasureunitcode'] = grossvolumemeasure_.attrib.get('unitCode')
        # ['NetVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netvolumemeasure_: Element = element.find('./' + cbcnamespace + 'NetVolumeMeasure')
        if netvolumemeasure_ is not None:
            if netvolumemeasure_.text is not None:
                frappedoc['netvolumemeasure'] = netvolumemeasure_.text
                frappedoc['netvolumemeasureunitcode'] = netvolumemeasure_.attrib.get('unitCode')
        # ['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totalgoodsitemquantity_: Element = element.find('./' + cbcnamespace + 'TotalGoodsItemQuantity')
        if totalgoodsitemquantity_ is not None:
            if totalgoodsitemquantity_.text is not None:
                frappedoc['totalgoodsitemquantity'] = totalgoodsitemquantity_.text
                frappedoc['totalgoodsitemquantityunitcode'] = totalgoodsitemquantity_.attrib.get('unitCode')
        # ['TotalTransportHandlingUnitQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totaltransporthandlingunitquantity_: Element = element.find(
            './' + cbcnamespace + 'TotalTransportHandlingUnitQuantity')
        if totaltransporthandlingunitquantity_ is not None:
            if totaltransporthandlingunitquantity_.text is not None:
                frappedoc['totaltransporthandlingunitquantity'] = totaltransporthandlingunitquantity_.text
                frappedoc[
                    'totaltransporthandlingunitquantityunitcode'] = totaltransporthandlingunitquantity_.attrib.get(
                    'unitCode')
        # ['InsuranceValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        insurancevalueamount_: Element = element.find('./' + cbcnamespace + 'InsuranceValueAmount')
        if insurancevalueamount_ is not None:
            if insurancevalueamount_.text is not None:
                frappedoc['insurancevalueamount'] = insurancevalueamount_.text
                frappedoc['insurancevalueamountcurrencyid'] = insurancevalueamount_.attrib.get('currencyID')
        # ['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredcustomsvalueamount_: Element = element.find('./' + cbcnamespace + 'DeclaredCustomsValueAmount')
        if declaredcustomsvalueamount_ is not None:
            if declaredcustomsvalueamount_.text is not None:
                frappedoc['declaredcustomsvalueamount'] = declaredcustomsvalueamount_.text
                frappedoc['declaredcustomsvalueamountcurrencyid'] = declaredcustomsvalueamount_.attrib.get('currencyID')
        # ['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredforcarriagevalueamount_: Element = element.find('./' + cbcnamespace + 'DeclaredCustomsValueAmount')
        if declaredforcarriagevalueamount_ is not None:
            if declaredforcarriagevalueamount_.text is not None:
                frappedoc['declaredforcarriagevalueamount'] = declaredforcarriagevalueamount_.text
                frappedoc['declaredforcarriagevalueamountcurrencyid'] = declaredforcarriagevalueamount_.attrib.get(
                    'currencyID')
        # ['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredstatisticsvalueamount_: Element = element.find('./' + cbcnamespace + 'DeclaredStatisticsValueAmount')
        if declaredstatisticsvalueamount_ is not None:
            if declaredstatisticsvalueamount_.text is not None:
                frappedoc['declaredstatisticsvalueamount'] = declaredstatisticsvalueamount_.text
                frappedoc['declaredstatisticsvalueamountcurrencyid'] = declaredstatisticsvalueamount_.attrib.get(
                    'currencyID')
        # ['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        freeonboardvalueamount_: Element = element.find('./' + cbcnamespace + 'FreeOnBoardValueAmount')
        if freeonboardvalueamount_ is not None:
            if freeonboardvalueamount_.text is not None:
                frappedoc['freeonboardvalueamount'] = freeonboardvalueamount_.text
                frappedoc['freeonboardvalueamountcurrencyid'] = freeonboardvalueamount_.attrib.get('currencyID')
        # ['SpecialInstructions'] = ('cbc', '', 'Seçimli (0...n)')
        descriptions_: list = element.findall('./' + cbcnamespace + 'SpecialInstructions')
        if len(descriptions_) != 0:
            descriptions: list = []
            for description_ in descriptions_:
                tmp = TRUBLNote().process_element(description_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    descriptions.append(tmp)
            if len(descriptions) != 0:
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
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                tmp = element_.get('strategy').process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    frappedoc[element_.get('fieldName')] = tmp.name
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['GoodsItem'] = ('cac', 'GoodsItem', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'GoodsItem')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLGoodsItem().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.goodsitem = tagelements
                document.save()
        # ['ShipmentStage'] = ('cac', 'ShipmentStage', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'ShipmentStage')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLShipmentStage().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.shipmentstage = tagelements
                document.save()
        # ['TransportHandlingUnit'] = ('cac', 'TransportHandlingUnit', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'TransportHandlingUnit')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLTransportHandlingUnit().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.transporthandlingunit = tagelements
                document.save()
        return document
