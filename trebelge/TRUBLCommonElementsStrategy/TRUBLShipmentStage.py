from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLShipmentStage(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Price'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TransportModeCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TransportMeansTypeCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Instructions'] = ('cbc', '', 'Seçimli (0...1)')

        # ['TransitDirectionCode'] = ('cbc', '', 'Seçimli (0...n)')

        # ['TransitPeriod'] = ('cac', 'Period', 'Seçimli (0...1)')
        # ['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...1)')
        # ['DriverPerson'] = ('cac', 'Person', 'Seçimli (0...n)')

        cbcsecimli01: list = ['HandlingCode', 'HandlingInstructions']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if not field_:
                frappedoc[field_.tag.lower()] = field_.text

        # ['GrossWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossweightmeasure_: Element = element.find(cbcnamespace + 'GrossWeightMeasure')
        if not grossweightmeasure_:
            frappedoc['grossweightmeasure'] = grossweightmeasure_.text
            frappedoc['grossweightmeasureunitcode'] = grossweightmeasure_.attrib.get('unitCode')
        # ['NetWeightMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netweightmeasure_: Element = element.find(cbcnamespace + 'NetWeightMeasure')
        if not netweightmeasure_:
            frappedoc['netweightmeasure'] = netweightmeasure_.text
            frappedoc['netweightmeasureunitcode'] = netweightmeasure_.attrib.get('unitCode')
        # ['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grossvolumemeasure_: Element = element.find(cbcnamespace + 'GrossVolumeMeasure')
        if not grossvolumemeasure_:
            frappedoc['grossvolumemeasure'] = grossvolumemeasure_.text
            frappedoc['grossvolumemeasureunitcode'] = grossvolumemeasure_.attrib.get('unitCode')
        # ['NetVolumeMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        netvolumemeasure_: Element = element.find(cbcnamespace + 'NetVolumeMeasure')
        if not netvolumemeasure_:
            frappedoc['netvolumemeasure'] = netvolumemeasure_.text
            frappedoc['netvolumemeasureunitcode'] = netvolumemeasure_.attrib.get('unitCode')
        # ['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totalgoodsitemquantity_: Element = element.find(cbcnamespace + 'TotalGoodsItemQuantity')
        if not totalgoodsitemquantity_:
            frappedoc['totalgoodsitemquantity'] = totalgoodsitemquantity_.text
            frappedoc['totalgoodsitemquantityunitcode'] = totalgoodsitemquantity_.attrib.get('unitCode')
        # ['TotalTransportHandlingUnitQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        totaltransporthandlingunitquantity_: Element = element.find(cbcnamespace + 'TotalTransportHandlingUnitQuantity')
        if not totaltransporthandlingunitquantity_:
            frappedoc['totaltransporthandlingunitquantity'] = totaltransporthandlingunitquantity_.text
            frappedoc['totaltransporthandlingunitquantityunitcode'] = totaltransporthandlingunitquantity_.attrib.get(
                'unitCode')
        # ['InsuranceValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        insurancevalueamount_: Element = element.find(cbcnamespace + 'InsuranceValueAmount')
        if not insurancevalueamount_:
            frappedoc['insurancevalueamount'] = insurancevalueamount_.text
            frappedoc['insurancevalueamountcurrencyid'] = insurancevalueamount_.attrib.get('currencyID')
        # ['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredcustomsvalueamount_: Element = element.find(cbcnamespace + 'DeclaredCustomsValueAmount')
        if not declaredcustomsvalueamount_:
            frappedoc['declaredcustomsvalueamount'] = declaredcustomsvalueamount_.text
            frappedoc['declaredcustomsvalueamountcurrencyid'] = declaredcustomsvalueamount_.attrib.get('currencyID')
        # ['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredforcarriagevalueamount_: Element = element.find(cbcnamespace + 'DeclaredCustomsValueAmount')
        if not declaredforcarriagevalueamount_:
            frappedoc['declaredforcarriagevalueamount'] = declaredforcarriagevalueamount_.text
            frappedoc['declaredforcarriagevalueamountcurrencyid'] = declaredforcarriagevalueamount_.attrib.get(
                'currencyID')
        # ['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        declaredstatisticsvalueamount_: Element = element.find(cbcnamespace + 'DeclaredStatisticsValueAmount')
        if not declaredstatisticsvalueamount_ is not None:
            frappedoc['declaredstatisticsvalueamount'] = declaredstatisticsvalueamount_.text
            frappedoc['declaredstatisticsvalueamountcurrencyid'] = declaredstatisticsvalueamount_.attrib.get(
                'currencyID')
        # ['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli (0...1)')
        freeonboardvalueamount_: Element = element.find(cbcnamespace + 'FreeOnBoardValueAmount')
        if not freeonboardvalueamount_ is not None:
            frappedoc['freeonboardvalueamount'] = freeonboardvalueamount_.text
            frappedoc['freeonboardvalueamountcurrencyid'] = freeonboardvalueamount_.attrib.get('currencyID')

        # ['SpecialInstructions'] = ('cbc', '', 'Seçimli (0...n)')

        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...1)')
        # ['ReturnAddress'] = ('cac', 'Address', 'Seçimli (0...1)')
        # ['FirstArrivalPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')
        # ['LastExitPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')

        # ['GoodsItem'] = ('cac', 'GoodsItem', 'Seçimli (0...n)')
        # ['ShipmentStage'] = ('cac', 'ShipmentStage', 'Seçimli (0...n)')
        # ['TransportHandlingUnit'] = ('cac', 'TransportHandlingUnit', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
