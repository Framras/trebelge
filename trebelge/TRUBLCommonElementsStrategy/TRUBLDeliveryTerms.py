from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLDeliveryTerms(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DeliveryTerms'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is None or id_.text.strip() == '':
            return None
        frappedoc['id'] = id_.text
        # ['SpecialTerms'] = ('cbc', 'specialterms', 'Seçimli (0...1)')
        specialterms_: Element = element.find('./' + cbcnamespace + 'SpecialTerms')
        if specialterms_ is not None and specialterms_.text.strip() != '':
            frappedoc['specialterms'] = specialterms_.text
        # ['Amount'] = ('cbc', 'amount', 'Seçimli (0...1)')
        amount_: Element = element.find('./' + cbcnamespace + 'Amount')
        if amount_ is not None and amount_.text.strip() != '':
            frappedoc['amount'] = amount_.text
            frappedoc['amountcurrencyid'] = amount_.attrib.get('currencyID')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
