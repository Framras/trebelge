from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLInvoiceLine import TRUBLInvoiceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLTemperature import TRUBLTemperature


class TRUBLGoodsItem(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR GoodsItem'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli(0..1)')
        # ['HazardousRiskIndicator'] = ('cbc', '', 'Seçimli(0..1)')
        # ['RequiredCustomsID'] = ('cbc', '', 'Seçimli(0..1)')
        # ['CustomsStatusCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['CustomsImportClassifiedIndicator'] = ('cbc', '', 'Seçimli(0..1)')
        # ['TraceID'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['ID', 'HazardousRiskIndicator', 'RequiredCustomsID', 'CustomsStatusCode',
                              'CustomsImportClassifiedIndicator', 'TraceID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[elementtag_.lower()] = field_.text
        # ['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['InsuranceValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        cbcamntsecimli01: list = ['DeclaredCustomsValueAmount', 'DeclaredForCarriageValueAmount',
                                  'DeclaredStatisticsValueAmount', 'FreeOnBoardValueAmount',
                                  'InsuranceValueAmount', 'ValueAmount']
        for elementtag_ in cbcamntsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[elementtag_.lower()] = field_.text
                frappedoc[elementtag_.lower() + 'currencyid'] = field_.attrib.get('currencyID')
        # ['GrossWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['NetWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ChargeableWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['NetVolumeMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['Quantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['CustomsTariffQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ChargeableQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ReturnableQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        cbcamntsecimli01: list = ['GrossWeightMeasure', 'NetWeightMeasure',
                                  'ChargeableWeightMeasure', 'GrossVolumeMeasure',
                                  'NetVolumeMeasure', 'Quantity',
                                  'CustomsTariffQuantity', 'ChargeableQuantity',
                                  'ReturnableQuantity']
        for elementtag_ in cbcamntsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[elementtag_.lower()] = field_.text
                frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Description'] = ('cbc', '', 'Seçimli(0..n)')
        descriptions_: list = element.findall('./' + cbcnamespace + 'Description')
        if descriptions_:
            descriptions: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for description_ in descriptions_:
                descriptions.append(self._strategyContext.return_element_data(description_,
                                                                              cbcnamespace,
                                                                              cacnamespace))
            frappedoc['description'] = descriptions
        # ['OriginAddress'] = ('cac', 'Address', 'Seçimli(0..1)')
        address_: Element = element.find('./' + cacnamespace + 'OriginAddress')
        if address_:
            strategy: TRUBLCommonElement = TRUBLAddress()
            self._strategyContext.set_strategy(strategy)
            frappedoc['originaddress'] = self._strategyContext.return_element_data(address_,
                                                                                   cbcnamespace,
                                                                                   cacnamespace)
        # ['Item'] = ('cac', 'Item', 'Seçimli(0..n)')
        # ['FreightAllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli(0..n)')
        # ['InvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli(0..n)')
        # ['Temperature'] = ('cac', 'Temperature', 'Seçimli(0..n)')
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)')
        cacsecimli0n: list = \
            [{'Tag': 'Item', 'strategy': TRUBLItem(), 'fieldName': 'item'},
             {'Tag': 'FreightAllowanceCharge', 'strategy': TRUBLAllowanceCharge(),
              'fieldName': 'freightallowancecharge'},
             {'Tag': 'InvoiceLine', 'strategy': TRUBLInvoiceLine(), 'fieldName': 'invoiceline'},
             {'Tag': 'Temperature', 'strategy': TRUBLTemperature(), 'fieldName': 'temperature'},
             {'Tag': 'MeasurementDimension', 'strategy': TRUBLDimension(), 'fieldName': 'measurementdimension'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall('./' + cacnamespace + element_.get('Tag'))
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
