from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLPerson(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str):
        """
        ['FirstName'] = ('cbc', '', 'Zorunlu(1)')
        ['FamilyName'] = ('cbc', '', 'Zorunlu(1)')
        ['Title'] = ('cbc', '', 'Seçimli (0...1)')
        ['MiddleName'] = ('cbc', '', 'Seçimli (0...1)')
        ['NameSuffix'] = ('cbc', '', 'Seçimli (0...1)')
        ['NationalityID'] = ('cbc', '', 'Seçimli (0...1)')
        ['FinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)')
        ['IdentityDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)')
        """
        person: dict = {'FirstName'.lower(): element.find(cbcnamespace + 'FirstName').text,
                        'FamilyName'.lower(): element.find(cbcnamespace + 'FamilyName').text}
        cbcsecimli01: list = ['Title', 'MiddleName', 'NameSuffix', 'NationalityID']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                person[field_.tag.lower()] = field_.text

        taxscheme_ = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        taxscheme = self._strategyContext.return_element_data(taxscheme_, cbcnamespace,
                                                              cacnamespace)
        for key in taxscheme.keys():
            partytaxscheme['taxscheme_' + key] = taxscheme.get(key)

        return person
