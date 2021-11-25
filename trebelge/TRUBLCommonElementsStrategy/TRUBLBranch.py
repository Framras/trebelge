from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialInstitution import TRUBLFinancialInstitution


class TRUBLBranch(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['Name'] = ('cbc', 'name', 'Seçimli(0..1)')
        ['FinancialInstitution'] = ('cac', 'financialinstitution_name', 'Seçimli(0..1)')
        """
        branch: dict = {}
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            branch['name'] = name_.text
        financialinstitution_ = element.find(cacnamespace + 'FinancialInstitution')
        if financialinstitution_ is not None:
            strategy: TRUBLCommonElement = TRUBLFinancialInstitution()
            self._strategyContext.set_strategy(strategy)
            financialinstitution = self._strategyContext.return_element_data(financialinstitution_, cbcnamespace,
                                                                             cacnamespace)
            if financialinstitution is not None:
                branch['financialinstitution_name'] = financialinstitution.get('name')

        return branch
