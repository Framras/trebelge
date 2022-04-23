from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLInvoiceLine import TRUBLInvoiceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
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
                    frappedoc[elementtag_.lower()] = field_.text.strip()
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
                    frappedoc[elementtag_.lower()] = field_.text.strip()
                    frappedoc[elementtag_.lower() + 'currencyid'] = field_.attrib.get('currencyID').strip()
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
                    frappedoc[elementtag_.lower()] = field_.text.strip()
                    frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode').strip()
        # ['Description'] = ('cbc', '', 'Seçimli(0..n)')
        descriptions = list()
        descriptions_: list = element.findall('./' + cbcnamespace + 'Description')
        if len(descriptions_) != 0:
            for description_ in descriptions_:
                element_ = description_.text
                if element_ is not None and element_.strip() != '':
                    descriptions.append(element_.strip())
        # ['OriginAddress'] = ('cac', 'Address', 'Seçimli(0..1)')
        address_: Element = element.find('./' + cacnamespace + 'OriginAddress')
        if address_ is not None:
            tmp = TRUBLAddress().process_element(address_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['originaddress'] = tmp.name
        if frappedoc == {}:
            return None
        # ['Item'] = ('cac', 'Item', 'Seçimli(0..n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'Item')
        items = list()
        if len(tagelements_) != 0:
            for tagelement in tagelements_:
                tmp = TRUBLItem().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    items.append(tmp.name)
        # ['FreightAllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli(0..n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'FreightAllowanceCharge')
        charges = list()
        if len(tagelements_) != 0:
            for tagelement in tagelements_:
                tmp = TRUBLAllowanceCharge().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    charges.append(tmp.name)
        # ['InvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli(0..n)')
        lines = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'InvoiceLine')
        if len(tagelements_) != 0:
            for tagelement in tagelements_:
                tmp = TRUBLInvoiceLine().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    lines.append(tmp.name)
        # ['Temperature'] = ('cac', 'Temperature', 'Seçimli(0..n)')
        temperatures = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'Temperature')
        if len(tagelements_) != 0:
            for tagelement in tagelements_:
                tmp = TRUBLTemperature().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    temperatures.append(tmp.name)
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)')
        dimensions = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if len(tagelements_) != 0:
            for tagelement in tagelements_:
                tmp = TRUBLDimension().process_element(tagelement, cbcnamespace, cacnamespace)
                if tmp is not None:
                    dimensions.append(tmp.name)
        if len(items) + len(charges) + len(lines) + len(temperatures) + len(dimensions) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(descriptions) != 0:
                for description in descriptions:
                    document.append("description", dict(note=description))
                    document.save()
            if len(items) != 0:
                doc_append = document.append("item", {})
                for item in items:
                    doc_append.item = item
                    document.save()
            if len(charges) != 0:
                doc_append = document.append("freightallowancecharge", {})
                for charge in charges:
                    doc_append.allowancecharge = charge
                    document.save()
            if len(lines) != 0:
                doc_append = document.append("invoiceline", {})
                for line in lines:
                    doc_append.invoiceline = line
                    document.save()
            if len(temperatures) != 0:
                doc_append = document.append("temperature", {})
                for temperature in temperatures:
                    doc_append.temperature = temperature
                    document.save()
            if len(dimensions) != 0:
                doc_append = document.append("measurementdimension", {})
                for dimension in dimensions:
                    doc_append.dimension = dimension
                    document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
