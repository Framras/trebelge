from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLTaxCategory(TRUBLCommonElement):

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        pass

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        frappedata: dict = {}
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is not None:
            if name_.text is not None:
                frappedata['taxcategoryname'] = name_.text.strip()
        # ['TaxExemptionReasonCode'] = ('cbc', 'taxexemptionreasoncode', 'Seçimli (0...1)')
        # ['TaxExemptionReason'] = ('cbc', 'taxexemptionreason', 'Seçimli (0...1)')
        cbcsecimli01: list = ['TaxExemptionReasonCode', 'TaxExemptionReason']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedata[elementtag_.lower()] = field_.text.strip()
        # ['TaxScheme'] = ('cac', 'taxscheme', 'Zorunlu(1)')
        taxscheme_: Element = element.find('./' + cacnamespace + 'TaxScheme')
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

        return frappedata
