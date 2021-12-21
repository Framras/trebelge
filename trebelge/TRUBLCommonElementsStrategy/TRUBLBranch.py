from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialInstitution import TRUBLFinancialInstitution


class TRUBLBranch(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR Branch'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Name'] = ('cbc', 'branchname', 'Seçimli(0..1)')
        name_: Element = element.find(cbcnamespace + 'Name')
        if not name_:
            frappedoc['branchname'] = name_.text
        # ['FinancialInstitution'] = ('cac', 'FinancialInstitution()', 'Seçimli(0..1)', 'financialinstitution')
        financialinstitution_: Element = element.find(cacnamespace + 'FinancialInstitution')
        if not financialinstitution_:
            strategy: TRUBLCommonElement = TRUBLFinancialInstitution()
            self._strategyContext.set_strategy(strategy)
            frappedoc['financialinstitution'] = [self._strategyContext.return_element_data(financialinstitution_,
                                                                                           cbcnamespace,
                                                                                           cacnamespace)]

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
