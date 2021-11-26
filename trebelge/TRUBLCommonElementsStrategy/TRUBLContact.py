from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialInstitution import TRUBLFinancialInstitution


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
        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            contact[id_.tag.lower()] = id_.text
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            contact[name_.tag.lower()] = name_.text
        telephone_ = element.find(cbcnamespace + 'Telephone')
        if telephone_ is not None:
            contact[telephone_.tag.lower()] = telephone_.text
        telefax_ = element.find(cbcnamespace + 'Telefax')
        if telefax_ is not None:
            contact[telefax_.tag.lower()] = telefax_.text
        electronicmail_ = element.find(cbcnamespace + 'ElectronicMail')
        if electronicmail_ is not None:
            contact[electronicmail_.tag.lower()] = electronicmail_.text
        note_ = element.find(cbcnamespace + 'Note')
        if note_ is not None:
            contact[note_.tag.lower()] = note_.text
        othercommunication_ = element.findall(cacnamespace + 'OtherCommunication')
        if othercommunication_ is not None:
            strategy: TRUBLCommonElement = TRUBLFinancialInstitution()
            self._strategyContext.set_strategy(strategy)
            financialinstitution = self._strategyContext.return_element_data(othercommunication_, cbcnamespace,
                                                                             cacnamespace)
            if financialinstitution is not None:
                branch['financialinstitution_name'] = financialinstitution.get('name')

        return branch
