from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference


class TRUBLOrderLineReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR OrderLineReference'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LineID'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'lineid': element.find('./' + cbcnamespace + 'LineID').text}
        # ['SalesOrderLineID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['UUID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['LineStatusCode'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['SalesOrderLineID', 'UUID', 'LineStatusCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['OrderReference'] = ('cac', 'OrderReference', 'Seçimli (0...1)')
        orderreference_: Element = element.find('./' + cacnamespace + 'OrderReference')
        if orderreference_:
            strategy: TRUBLCommonElement = TRUBLOrderReference()
            self._strategyContext.set_strategy(strategy)
            frappedoc['orderreference'] = [self._strategyContext.return_element_data(orderreference_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)]

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
