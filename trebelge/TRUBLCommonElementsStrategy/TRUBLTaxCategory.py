from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
import trebelge.TRUBLCommonElementsStrategy.TRUBLTaxScheme


class TRUBLTaxCategory(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxCategory'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find(cbcnamespace + 'Name')
        if name_:
            frappedoc['taxcategoryname'] = name_.text
        # ['TaxExemptionReasonCode'] = ('cbc', 'taxexemptionreasoncode', 'Seçimli (0...1)')
        # ['TaxExemptionReason'] = ('cbc', 'taxexemptionreason', 'Seçimli (0...1)')
        cbcsecimli01: list = ['TaxExemptionReasonCode', 'TaxExemptionReason']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['TaxScheme'] = ('cac', 'taxscheme', 'Zorunlu(1)')
        taxscheme_: Element = element.find(cacnamespace + 'TaxScheme')
        strategy: TRUBLCommonElement = trebelge.TRUBLTaxScheme()
        self._strategyContext.set_strategy(strategy)
        frappedoc['taxscheme'] = self._strategyContext.return_element_data(taxscheme_,
                                                                           cbcnamespace,
                                                                           cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
