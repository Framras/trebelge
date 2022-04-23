from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLPartyTaxScheme(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR PartyTaxScheme'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['TaxScheme'] = ('cac', 'TaxScheme()', 'Zorunlu (1)', 'taxscheme')
        taxscheme_: Element = element.find('./' + cacnamespace + 'TaxScheme')
        if taxscheme_ is not None:
            tmp = TRUBLTaxScheme().process_element(taxscheme_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['taxscheme'] = tmp.name
        # ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        # ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RegistrationName', 'CompanyID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
