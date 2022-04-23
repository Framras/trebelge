from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLItemInstance(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR ItemInstance'

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
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['AdditionalItemProperty'] = ('cac', 'AdditionalItemProperty', 'Seçimli (0...1)')
        # ['LotIdentification'] = ('cac', 'LotIdentification', 'Seçimli (0...1)')
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
