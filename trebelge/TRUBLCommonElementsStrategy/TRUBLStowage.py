from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLStowage(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Stowage'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}

        # ['LocationID'] = ('cbc', '', 'Seçimli (0...1)')

        # ['Location'] = ('cac', 'Location', 'Seçimli (0...n)')
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
