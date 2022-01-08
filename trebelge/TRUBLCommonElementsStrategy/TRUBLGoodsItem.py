from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLInvoiceLine import TRUBLInvoiceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLTemperature import TRUBLTemperature


class TRUBLGoodsItem(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR GoodsItem'

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
            if field_ is not None:
                if field_.text is not None:
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
            if field_ is not None:
                if field_.text is not None:
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
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
                    frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Description'] = ('cbc', '', 'Seçimli(0..n)')
        descriptions_: list = element.findall('./' + cbcnamespace + 'Description')
        if descriptions_ is not None:
            descriptions: list = []
            for description_ in descriptions_:
                tmp = TRUBLNote().process_element(description_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    descriptions.append(tmp)
            if len(descriptions) != 0:
                frappedoc['description'] = descriptions
        # ['OriginAddress'] = ('cac', 'Address', 'Seçimli(0..1)')
        address_: Element = element.find('./' + cacnamespace + 'OriginAddress')
        if address_ is not None:
            tmp = TRUBLAddress().process_element(address_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['originaddress'] = tmp.name
        if frappedoc == {}:
            return None
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['Item'] = ('cac', 'Item', 'Seçimli(0..n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'Item')
        if tagelements_ is not None:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLItem().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.item = tagelements
                document.save()
        # ['FreightAllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli(0..n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'FreightAllowanceCharge')
        if tagelements_ is not None:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLAllowanceCharge().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.freightallowancecharge = tagelements
                document.save()
        # ['InvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli(0..n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'InvoiceLine')
        if tagelements_ is not None:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLInvoiceLine().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.invoiceline = tagelements
                document.save()
        # ['Temperature'] = ('cac', 'Temperature', 'Seçimli(0..n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'Temperature')
        if tagelements_ is not None:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLTemperature().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.temperature = tagelements
                document.save()
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if tagelements_ is not None:
            tagelements: list = []
            for tagelement in tagelements_:
                tmp = TRUBLDimension().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.measurementdimension = tagelements
                document.save()

        return self._update_frappedoc(self._frappeDoctype, frappedoc, document)
