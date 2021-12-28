from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxSubtotal import TRUBLTaxSubtotal


class TRUBLTaxTotal(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxTotal'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
        taxamount_: Element = element.find('./' + cbcnamespace + 'TaxAmount')
        frappedoc: dict = {'taxamount': taxamount_.text,
                           'taxamountcurrencyid': taxamount_.attrib.get('currencyID')
                           }
        # ['TaxSubtotal'] = ('cac', 'taxsubtotals', 'Zorunlu(1..n)', 'taxsubtotal')
        taxsubtotals: list = []
        for taxsubtotal_ in element.findall('./' + cacnamespace + 'TaxSubtotal'):
            taxsubtotals.append(TRUBLTaxSubtotal.process_element(taxsubtotal_,
                                                                 cbcnamespace,
                                                                 cacnamespace))
        frappedoc['taxsubtotal'] = taxsubtotals

        return self._get_frappedoc(self._frappeDoctype, frappedoc, False)
