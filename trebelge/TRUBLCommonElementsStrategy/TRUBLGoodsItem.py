from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLGoodsItem(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR GoodsItem'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli(0..1)')
        # ['Description'] = ('cbc', '', 'Seçimli(0..n)')
        # ['HazardousRiskIndicator'] = ('cbc', '', 'Seçimli(0..1)')
        # ['DeclaredCustomsValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['DeclaredForCarriageValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['DeclaredStatisticsValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['FreeOnBoardValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['InsuranceValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ValueAmount'] = ('cbc', '', 'Seçimli(0..1)')
        # ['currencyID'] = ('', '', 'Zorunlu(1)')
        # ['GrossWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['NetWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ChargeableWeightMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['GrossVolumeMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['NetVolumeMeasure'] = ('cbc', '', 'Seçimli(0..1)')
        # ['unitCode'] = ('', '', 'Zorunlu(1)')
        # ['Quantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['RequiredCustomsID'] = ('cbc', '', 'Seçimli(0..1)')
        # ['CustomsStatusCode'] = ('cbc', '', 'Seçimli(0..1)')
        # ['CustomsTariffQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['CustomsImportClassifiedIndicator'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ChargeableQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['ReturnableQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['TraceID'] = ('cbc', '', 'Seçimli(0..1)')
        # ['Item'] = ('cac', 'Item', 'Seçimli(0..n)')
        # ['FreightAllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli(0..n)')
        # ['InvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli(0..n)')
        # ['Temperature'] = ('cac', 'Temperature', 'Seçimli(0..n)')
        # ['OriginAddress'] = ('cac', 'Address', 'Seçimli(0..1)')
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli(0..n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
