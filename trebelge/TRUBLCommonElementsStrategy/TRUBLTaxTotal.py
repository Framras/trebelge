from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxSubtotal import TRUBLTaxSubtotal


class TRUBLTaxTotal(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxTotal'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
        taxamount_: Element = element.find('./' + cbcnamespace + 'TaxAmount')
        if taxamount_.text is None:
            return None
        frappedoc: dict = dict(taxamount=taxamount_.text,
                               taxamountcurrencyid=taxamount_.attrib.get('currencyID')
                               )
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['TaxSubtotal'] = ('cac', 'taxsubtotals', 'Zorunlu(1..n)', 'taxsubtotal')
        taxsubtotals: list = []
        for taxsubtotal_ in element.findall('./' + cacnamespace + 'TaxSubtotal'):
            tmp = TRUBLTaxSubtotal().process_element(taxsubtotal_, cbcnamespace, cacnamespace)
            if tmp is not None:
                taxsubtotals.append(tmp)
        if len(taxsubtotals) != 0:
            document.taxsubtotal = taxsubtotals
            document.save()

        return self._update_frappedoc(self._frappeDoctype, frappedoc, document)
