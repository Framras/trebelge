from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialInstitution import TRUBLFinancialInstitution


class TRUBLBranch(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR Branch'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        frappedoc: dict = {}
        # ['Name'] = ('cbc', 'branchname', 'Seçimli(0..1)')
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc['branchname'] = name_.text
        # ['FinancialInstitution'] = ('cac', 'FinancialInstitution()', 'Seçimli(0..1)', 'financialinstitution')
        financialinstitution_ = element.find(cacnamespace + 'FinancialInstitution')
        if financialinstitution_ is not None:
            strategy: TRUBLCommonElement = TRUBLFinancialInstitution()
            self._strategyContext.set_strategy(strategy)
            frappedoc['financialinstitution'] = frappe.get_doc(
                'UBL TR FinancialInstitution',
                self._strategyContext.return_element_data(financialinstitution_,
                                                          cbcnamespace,
                                                          cacnamespace)[0]['name'])

            return self.get_frappedoc(self._frappeDoctype, frappedoc)
