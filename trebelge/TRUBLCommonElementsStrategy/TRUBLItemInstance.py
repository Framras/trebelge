from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLItemInstance(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ItemInstance'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ProductTraceID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ManufacturedDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ManufacturedTime'] = ('cbc', '', 'Seçimli (0...1)')
        # ['BestBeforeDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RegistrationID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['SerialID'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ProductTraceID', 'ManufacturedDate', 'ManufacturedTime', 'BestBeforeDate',
                              'RegistrationID', 'SerialID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text

        # ['AdditionalItemProperty'] = ('cac', 'AdditionalItemProperty', 'Seçimli (0...1)')
        # ['LotIdentification'] = ('cac', 'LotIdentification', 'Seçimli (0...1)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
