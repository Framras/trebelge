from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommunication import TRUBLCommunication


class TRUBLContact(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Contact'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['Telephone'] = ('cbc', 'telephone', 'Seçimli (0...1)')
        # ['Telefax'] = ('cbc', 'telefax', 'Seçimli (0...1)')
        # ['ElectronicMail'] = ('cbc', 'electronicmail', 'Seçimli (0...1)')
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'Telephone', 'Telefax', 'ElectronicMail', 'Note']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc['contactname'] = name_.text

        # ['OtherCommunication'] = ('cac', 'Communication', 'Seçimli(0..n)')
        othercommunications_: list = element.findall(cacnamespace + 'OtherCommunication')
        if othercommunications_ is not None:
            communications: list = []
            strategy: TRUBLCommonElement = TRUBLCommunication()
            self._strategyContext.set_strategy(strategy)
            for othercommunication in othercommunications_:
                communications.append(self._strategyContext.return_element_data(othercommunication,
                                                                                cbcnamespace,
                                                                                cacnamespace))
            frappedoc['othercommunication'] = communications

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
