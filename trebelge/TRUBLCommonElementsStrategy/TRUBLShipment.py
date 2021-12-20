from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLShipment(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Price'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find(cbcnamespace + 'ID').text}

        # ['HandlingCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['HandlingInstructions'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['HandlingCode', 'HandlingInstructions']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['GrossWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossweightmeasure = element.find(cbcnamespace + 'GrossWeightMeasure')
        if grossweightmeasure is not None:
            frappedoc['grossweightmeasure'] = grossweightmeasure.text
            frappedoc['grossweightmeasureunitcode'] = grossweightmeasure.attrib.get('unitCode')
        # ['NetWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netweightmeasure = element.find(cbcnamespace + 'NetWeightMeasure')
        if netweightmeasure is not None:
            frappedoc['netweightmeasure'] = netweightmeasure.text
            frappedoc['netweightmeasureunitcode'] = netweightmeasure.attrib.get('unitCode')
        # ['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossvolumemeasure = element.find(cbcnamespace + 'GrossVolumeMeasure')
        if grossvolumemeasure is not None:
            frappedoc['grossvolumemeasure'] = grossvolumemeasure.text
            frappedoc['grossvolumemeasureunitcode'] = grossvolumemeasure.attrib.get('unitCode')
        # ['NetVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netvolumemeasure = element.find(cbcnamespace + 'NetVolumeMeasure')
        if netvolumemeasure is not None:
            frappedoc['netvolumemeasure'] = netvolumemeasure.text
            frappedoc['netvolumemeasureunitcode'] = netvolumemeasure.attrib.get('unitCode')
        # ['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totalgoodsitemquantity = element.find(cbcnamespace + 'TotalGoodsItemQuantity')
        if totalgoodsitemquantity is not None:
            frappedoc['totalgoodsitemquantity'] = totalgoodsitemquantity.text
            frappedoc['totalgoodsitemquantityunitcode'] = totalgoodsitemquantity.attrib.get('unitCode')
        # ['TotalTransportHandlingUnitQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totaltransporthandlingunitquantity = element.find(cbcnamespace + 'TotalTransportHandlingUnitQuantity')
        if totaltransporthandlingunitquantity is not None:
            frappedoc['totaltransporthandlingunitquantity'] = totaltransporthandlingunitquantity.text
            frappedoc['totaltransporthandlingunitquantityunitcode'] = totaltransporthandlingunitquantity.attrib.get(
                'unitCode')
        # ['InsuranceValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        insurancevalueamount = element.find(cbcnamespace + 'InsuranceValueAmount')
        if insurancevalueamount is not None:
            frappedoc['insurancevalueamount'] = insurancevalueamount.text
            frappedoc['insurancevalueamountcurrencyid'] = insurancevalueamount.attrib.get('currencyID')
        # ['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredcustomsvalueamount = element.find(cbcnamespace + 'DeclaredCustomsValueAmount')
        if declaredcustomsvalueamount is not None:
            frappedoc['declaredcustomsvalueamount'] = declaredcustomsvalueamount.text
            frappedoc['declaredcustomsvalueamountcurrencyid'] = declaredcustomsvalueamount.attrib.get('currencyID')
        # ['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredforcarriagevalueamount = element.find(cbcnamespace + 'DeclaredCustomsValueAmount')
        if declaredforcarriagevalueamount is not None:
            frappedoc['declaredforcarriagevalueamount'] = declaredforcarriagevalueamount.text
            frappedoc['declaredforcarriagevalueamountcurrencyid'] = declaredforcarriagevalueamount.attrib.get(
                'currencyID')
        # ['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredstatisticsvalueamount = element.find(cbcnamespace + 'DeclaredStatisticsValueAmount')
        if declaredstatisticsvalueamount is not None:
            frappedoc['declaredstatisticsvalueamount'] = declaredstatisticsvalueamount.text
            frappedoc['declaredstatisticsvalueamountcurrencyid'] = declaredstatisticsvalueamount.attrib.get(
                'currencyID')
        # ['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        freeonboardvalueamount = element.find(cbcnamespace + 'FreeOnBoardValueAmount')
        if freeonboardvalueamount is not None:
            frappedoc['freeonboardvalueamount'] = freeonboardvalueamount.text
            frappedoc['freeonboardvalueamountcurrencyid'] = freeonboardvalueamount.attrib.get('currencyID')

        # ['SpecialInstructions'] = ('cbc', '', 'Seçimli (0...n)')

        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...1)')
        # ['ReturnAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        # ['FirstArrivalPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')
        # ['LastExitPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')

        # ['GoodsItem'] = ('cac', 'GoodsItem', 'Seçimli (0...n)')
        # ['ShipmentStage'] = ('cac', 'ShipmentStage', 'Seçimli (0...n)')
        # ['TransportHandlingUnit'] = ('cac', 'TransportHandlingUnit', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
