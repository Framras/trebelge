from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLPartyTaxScheme(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str):
        """
        ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        ['TaxScheme'] = ('cac', 'TaxScheme()', 'Zorunlu (1)', 'taxscheme')
        """
        partytaxscheme: dict = {}
        cbcsecimli01: list = ['RegistrationName', 'CompanyID']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                partytaxscheme[field_.tag.lower()] = field_.text

        taxscheme_ = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        taxscheme = self._strategyContext.return_element_data(taxscheme_, cbcnamespace,
                                                              cacnamespace)
        for key in taxscheme.keys():
            partytaxscheme['taxscheme_' + key] = taxscheme.get(key)

        return partytaxscheme
