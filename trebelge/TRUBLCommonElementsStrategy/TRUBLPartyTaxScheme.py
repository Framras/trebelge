from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLPartyTaxScheme(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['TaxScheme'] = ('cac', 'TaxScheme()', 'Zorunlu (1)', 'taxscheme')
        taxscheme_: Element = element.find('./' + cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        frappedoc['taxscheme'] = self._strategyContext.return_element_data(taxscheme_,
                                                                           cbcnamespace,
                                                                           cacnamespace)
        # ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        # ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RegistrationName', 'CompanyID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
