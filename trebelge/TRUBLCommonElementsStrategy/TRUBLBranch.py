from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialInstitution import TRUBLFinancialInstitution

import frappe


class TRUBLBranch(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['Name'] = ('cbc', 'name', 'Seçimli(0..1)')
        # ['FinancialInstitution'] = ('cac', 'FinancialInstitution()', 'Seçimli(0..1)', 'financialinstitution')
        frappedoc: dict = {}
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc[name_.tag.lower()] = name_.text
        financialinstitution_ = element.find(cacnamespace + 'FinancialInstitution')
        if financialinstitution_ is not None:
            strategy: TRUBLCommonElement = TRUBLFinancialInstitution()
            self._strategyContext.set_strategy(strategy)
            financialinstitution = self._strategyContext.return_element_data(financialinstitution_, cbcnamespace,
                                                                             cacnamespace)
            for key in financialinstitution.keys():
                frappedoc['financialinstitution_' + key] = financialinstitution.get(key)

        if not frappe.get_all(self._frappeDoctype, filters=frappedoc):
            pass
        else:
            newfrappedoc = frappedoc
            newfrappedoc['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newfrappedoc)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=frappedoc)
