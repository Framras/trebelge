from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLBranch import TRUBLBranch
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLFinancialAccount(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR FinancialAccount'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find(cbcnamespace + 'ID')}

        # ['CurrencyCode'] = ('cbc', 'currencycode', 'Seçimli (0...1)')
        # ['PaymentNote'] = ('cbc', 'paymentnote', 'Seçimli (0...1)')
        cbcsecimli01: list = ['CurrencyCode', 'PaymentNote']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['FinancialInstitutionBranch'] = ('cac', 'Branch()', 'Seçimli (0...1)', 'financialinstitutionbranch')
        financialinstitutionbranch_ = element.find(cacnamespace + 'FinancialInstitutionBranch')
        if financialinstitutionbranch_ is not None:
            strategy: TRUBLCommonElement = TRUBLBranch()
            self._strategyContext.set_strategy(strategy)
            frappedoc['financialinstitutionbranch'] = frappe.get_doc(
                'UBL TR Branch',
                self._strategyContext.return_element_data(financialinstitutionbranch_, cbcnamespace,
                                                          cacnamespace)[0]['name'])

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
