from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLPerson(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['FirstName'] = ('cbc', 'firstname', 'Zorunlu(1)')
        # ['FamilyName'] = ('cbc', 'familyname', 'Zorunlu(1)')
        frappedoc: dict = {'firstname': element.find(cbcnamespace + 'FirstName').text,
                           'familyname': element.find(cbcnamespace + 'FamilyName').text}
        # ['Title'] = ('cbc', '', 'Seçimli (0...1)')
        # ['MiddleName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['NameSuffix'] = ('cbc', '', 'Seçimli (0...1)')
        # ['NationalityID'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['Title', 'MiddleName', 'NameSuffix', 'NationalityID']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['FinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)')
        # ['IdentityDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)')
        taxscheme_ = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        taxscheme = self._strategyContext.return_element_data(taxscheme_, cbcnamespace,
                                                              cacnamespace)
        for key in taxscheme.keys():
            partytaxscheme['taxscheme_' + key] = taxscheme.get(key)

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
