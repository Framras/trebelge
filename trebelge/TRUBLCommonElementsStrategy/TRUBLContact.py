from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommunication import TRUBLCommunication


class TRUBLContact(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        ['Telephone'] = ('cbc', 'telephone', 'Seçimli (0...1)')
        ['Telefax'] = ('cbc', 'telefax', 'Seçimli (0...1)')
        ['ElectronicMail'] = ('cbc', 'electronicmail', 'Seçimli (0...1)')
        ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        ['OtherCommunication'] = ('cac', 'Communication', 'Seçimli(0..n)')
        """
        contact: dict = {}
        cbcsecimli01: list = ['Telephone', 'Telefax', 'ElectronicMail', 'Note']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                contact[field_.tag.lower()] = field_.text

        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            contact[('Contact' + 'ID').lower()] = id_.text
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            contact[('Contact' + 'Name').lower()] = name_.text
        othercommunications_ = element.findall(cacnamespace + 'OtherCommunication')
        if othercommunications_ is not None:
            strategy: TRUBLCommonElement = TRUBLCommunication()
            self._strategyContext.set_strategy(strategy)
            communications: list = []
            for othercommunication in othercommunications_:
                communication_ = self._strategyContext.return_element_data(othercommunication, cbcnamespace,
                                                                           cacnamespace)
                communications.append(communication_)
            contact['othercommunications'] = communications

        return contact
