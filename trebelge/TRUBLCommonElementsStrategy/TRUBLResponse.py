from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote


class TRUBLResponse(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR Response'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ReferenceID'] = ('cbc', '', 'Zorunlu (1)')
        frappedoc: dict = {'referenceid': element.find('./' + cbcnamespace + 'ReferenceID').text}
        # ['ResponseCode'] = ('cbc', '', 'Seçimli (0...1)')
        responsecode_: Element = element.find('./' + cbcnamespace + 'ResponseCode')
        if responsecode_:
            frappedoc['responsecode'] = responsecode_.text
        # ['Description'] = ('cbc', '', 'Seçimli (0...n)')
        descriptions_: list = element.findall('./' + cacnamespace + 'Description')
        if descriptions_:
            descriptions: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for description_ in descriptions_:
                descriptions.append(self._strategyContext.return_element_data(description_,
                                                                              cbcnamespace,
                                                                              cacnamespace))
            frappedoc['description'] = descriptions

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
