from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialAccount import TRUBLFinancialAccount


class TRUBLPerson(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR Person'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
        frappedoc: dict = {}
        # ['FirstName'] = ('cbc', 'firstname', 'Zorunlu(1)')
        firstname_: Element = element.find('./' + cbcnamespace + 'FirstName')
        # ['FamilyName'] = ('cbc', 'familyname', 'Zorunlu(1)')
        familyname_: Element = element.find('./' + cbcnamespace + 'FamilyName')
        if firstname_ is not None:
            if firstname_.text is not None:
                frappedoc['firstname'] = firstname_.text.strip()
        if familyname_ is not None:
            if familyname_.text is not None:
                frappedoc['firstname'] = familyname_.text.strip()
        # ['MiddleName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['NameSuffix'] = ('cbc', '', 'Seçimli (0...1)')
        # ['NationalityID'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['MiddleName', 'NameSuffix', 'NationalityID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['Title'] = ('cbc', 'persontitle', 'Seçimli (0...1)')
        field_: Element = element.find('./' + cbcnamespace + 'Title')
        if field_ is not None:
            if field_.text is not None:
                frappedoc['persontitle'] = field_.text.strip()
        # ['FinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)', 'financialaccount')
        financialaccount_: Element = element.find('./' + cacnamespace + 'FinancialAccount')
        if financialaccount_ is not None:
            tmp = TRUBLFinancialAccount().process_element(financialaccount_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['financialaccount'] = tmp.name
        # ['IdentityDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)', 'documentreference')
        documentreference_: Element = element.find('./' + cacnamespace + 'IdentityDocumentReference')
        if documentreference_ is not None:
            tmp = TRUBLDocumentReference().process_element(documentreference_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['documentreference'] = tmp.name
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
