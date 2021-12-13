from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLBranch import TRUBLBranch
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLFinancialAccount(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        """
        ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        ['CurrencyCode'] = ('cbc', 'currencycode', 'Seçimli (0...1)')
        ['PaymentNote'] = ('cbc', 'paymentnote', 'Seçimli (0...1)')
        ['FinancialInstitutionBranch'] = ('cac', 'Branch()', 'Seçimli (0...1)', 'financialinstitutionbranch')
        """
        financialaccount: dict = {'financialaccountid': element.find(cbcnamespace + 'ID')}
        cbcsecimli01: list = ['CurrencyCode', 'PaymentNote']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                financialaccount[field_.tag.lower()] = field_.text

        financialinstitutionbranch_ = element.find(cacnamespace + 'FinancialInstitutionBranch')
        if financialinstitutionbranch_ is not None:
            strategy: TRUBLCommonElement = TRUBLBranch()
            self._strategyContext.set_strategy(strategy)
            financialinstitutionbranch = self._strategyContext.return_element_data(financialinstitutionbranch_,
                                                                                   cbcnamespace, cacnamespace)
            for key in financialinstitutionbranch.keys():
                financialaccount['financialinstitutionbranch_' + key] = financialinstitutionbranch.get(key)

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
