from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLPartyTaxScheme(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        ['TaxScheme'] = ('cac', 'TaxScheme()', 'Zorunlu (1)', 'taxscheme')
        """
        partytaxscheme: dict = {}
        registrationname_ = element.find(cbcnamespace + 'RegistrationName')
        if registrationname_ is not None:
            partytaxscheme[registrationname_.tag.lower()] = registrationname_.text
        companyid_ = element.find(cbcnamespace + 'CompanyID')
        if companyid_ is not None:
            partytaxscheme[companyid_.tag.lower()] = companyid_.text
        taxscheme_ = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        taxscheme = self._strategyContext.return_element_data(taxscheme_, cbcnamespace,
                                                              cacnamespace)
        for key in taxscheme.keys():
            partytaxscheme['taxscheme_' + key] = taxscheme.get(key)

        return partytaxscheme
