from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLTemperature(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Temperature'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str) -> Document:
        # ['AttributeID'] = ('cbc', '', 'Zorunlu (1)')
        # ['Measure'] = ('cbc', '', 'Zorunlu (1)')
        # ['unitCode'] = ('', '', 'Zorunlu(1)')
        measure_: Element = element.find(cbcnamespace + 'Measure')
        frappedoc: dict = {'attributeid': element.find(cbcnamespace + 'AttributeID'),
                           'measure': measure_.text,
                           'measureunitcode': measure_.attrib.get('unitCode')
                           }

        # ['Description'] = ('cbc', '', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
