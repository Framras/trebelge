from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme import TRUBLTaxScheme


class TRUBLTaxCategory(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxCategory'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is not None:
            if name_.text is not None:
                frappedoc['taxcategoryname'] = name_.text.strip()
        # ['TaxExemptionReasonCode'] = ('cbc', 'taxexemptionreasoncode', 'Seçimli (0...1)')
        # ['TaxExemptionReason'] = ('cbc', 'taxexemptionreason', 'Seçimli (0...1)')
        cbcsecimli01: list = ['TaxExemptionReasonCode', 'TaxExemptionReason']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['TaxScheme'] = ('cac', 'taxscheme', 'Zorunlu(1)')
        taxscheme_: Element = element.find('./' + cacnamespace + 'TaxScheme')
        tmp = TRUBLTaxScheme().process_element(taxscheme_, cbcnamespace, cacnamespace)
        if tmp is not None:
            frappedoc['taxscheme'] = tmp.name
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
