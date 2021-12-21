from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLTransportHandlingUnit(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # ['TransportHandlingUnitTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['HandlingCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['HandlingInstructions'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['HazardousRiskIndicator'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['TotalPackageQuantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['DamageRemarks'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['TraceID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # ['ActualPackage'] = ('cac', 'Package', 'Seçimli (0...n)', True, False, False)
        # ['TransportEquipment'] = ('cac', 'TransportEquipment', 'Seçimli (0...n)', True, False, False)
        # ['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...n)', True, False, False)
        # ['HazardousGoodsTransit'] = ('cac', 'HazardousGoodsTransit', 'Seçimli (0...n)', True, False, False)
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)', True, False, False)
        # ['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)', True, False, False)
        # ['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)', True, False, False)
        # ['FloorSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)', True, False, False)
        # ['PalletSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)', True, False, False)
        # ['ShipmentDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        # ['CustomsDeclaration'] = ('cac', 'CustomsDeclaration', 'Seçimli (0...n)', True, False, False)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
