from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialAccount import TRUBLFinancialAccount


class TRUBLPerson(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR Person'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['FirstName'] = ('cbc', 'firstname', 'Zorunlu(1)')
        # ['FamilyName'] = ('cbc', 'familyname', 'Zorunlu(1)')
        frappedoc: dict = {'firstname': element.find(cbcnamespace + 'FirstName').text,
                           'familyname': element.find(cbcnamespace + 'FamilyName').text}

        # ['MiddleName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['NameSuffix'] = ('cbc', '', 'Seçimli (0...1)')
        # ['NationalityID'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['MiddleName', 'NameSuffix', 'NationalityID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['Title'] = ('cbc', 'persontitle', 'Seçimli (0...1)')
        field_: Element = element.find(cbcnamespace + 'Title')
        if field_:
            frappedoc['persontitle'] = field_.text

        # ['FinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)', 'financialaccount')
        financialaccount_: Element = element.find(cacnamespace + 'FinancialAccount')
        if financialaccount_:
            strategy: TRUBLCommonElement = TRUBLFinancialAccount()
            self._strategyContext.set_strategy(strategy)
            frappedoc['financialaccount'] = self._strategyContext.return_element_data(financialaccount_,
                                                                                      cbcnamespace,
                                                                                      cacnamespace)
        # ['IdentityDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)', 'documentreference')
        documentreference_: Element = element.find(cacnamespace + 'IdentityDocumentReference')
        if documentreference_:
            strategy: TRUBLCommonElement = TRUBLDocumentReference()
            self._strategyContext.set_strategy(strategy)
            frappedoc['documentreference'] = self._strategyContext.return_element_data(documentreference_,
                                                                                       cbcnamespace,
                                                                                       cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
