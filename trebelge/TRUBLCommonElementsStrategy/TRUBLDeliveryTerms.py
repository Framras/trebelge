from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLDeliveryTerms(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['SpecialTerms'] = ('cbc', 'specialterms', 'Seçimli (0...1)')
        # ['Amount'] = ('cbc', 'amount', 'Seçimli (0...1)')
        # ['currencyID'] = ('', 'amountcurrencyid', 'Zorunlu(1)')
        frappedoc: dict = {}
        id_: Element = element.find(cbcnamespace + 'ID')
        if not id_:
            frappedoc['id'] = id_.text
        specialterms_: Element = element.find(cbcnamespace + 'SpecialTerms')
        if not specialterms_:
            frappedoc['specialterms'] = specialterms_.text
        amount_: Element = element.find(cbcnamespace + 'Amount')
        if not amount_:
            frappedoc['amount'] = amount_.text
            frappedoc['amountcurrencyid'] = amount_.attrib.get('currencyID')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
