from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference


class TRUBLOrderLineReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR OrderLineReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LineID'] = ('cbc', '', 'Zorunlu(1)')
        lineid_ = element.find('./' + cbcnamespace + 'LineID').text
        if lineid_ is None:
            return None
        frappedoc: dict = dict(lineid=lineid_)
        # ['SalesOrderLineID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['UUID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['LineStatusCode'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['SalesOrderLineID', 'UUID', 'LineStatusCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['OrderReference'] = ('cac', 'OrderReference', 'Seçimli (0...1)')
        orderreference_: Element = element.find('./' + cacnamespace + 'OrderReference')
        if orderreference_ is not None:
            tmp = TRUBLOrderReference().process_element(orderreference_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['orderreference'] = tmp.name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
