from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote


class TRUBLTemperature(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Temperature'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['AttributeID'] = ('cbc', '', 'Zorunlu (1)')
        # ['Measure'] = ('cbc', '', 'Zorunlu (1)')
        # ['unitCode'] = ('', '', 'Zorunlu(1)')
        measure_: Element = element.find(cbcnamespace + 'Measure')
        frappedoc: dict = {'attributeid': element.find(cbcnamespace + 'AttributeID').text,
                           'measure': measure_.text,
                           'measureunitcode': measure_.attrib.get('unitCode')
                           }
        # ['Description'] = ('cbc', '', 'Seçimli (0...n)')
        descriptions_: list = element.findall(cbcnamespace + 'Description')
        if descriptions_ is not None:
            descriptions: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for description_ in descriptions_:
                descriptions.append(self._strategyContext.return_element_data(description_,
                                                                              cbcnamespace,
                                                                              cacnamespace))
            frappedoc['description'] = descriptions

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
