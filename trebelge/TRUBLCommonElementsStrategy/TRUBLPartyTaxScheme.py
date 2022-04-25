from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLPartyTaxScheme(TRUBLCommonElement):

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        pass

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        frappedata: dict = {}
        # ['TaxScheme'] = ('cac', 'TaxScheme()', 'Zorunlu (1)', 'taxscheme')
        taxscheme_: Element = element.find('./' + cacnamespace + 'TaxScheme')
        if taxscheme_ is not None:
            tmp: dict = TRUBLTaxScheme().process_elementasdict(taxscheme_, cbcnamespace, cacnamespace)
            if tmp != {}:
                try:
                    frappedata['taxschemeid'] = tmp['id']
                except KeyError:
                    pass
                try:
                    frappedata['taxschemename'] = tmp['taxschemename']
                except KeyError:
                    pass
                try:
                    frappedata['taxtypecode'] = tmp['taxtypecode']
                except KeyError:
                    pass
        # ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        # ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RegistrationName', 'CompanyID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedata[elementtag_.lower()] = field_.text.strip()

            return frappedata
