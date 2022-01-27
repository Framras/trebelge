from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLDeliveryTerms(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DeliveryTerms'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None:
            if id_.text:
                frappedoc['id'] = id_.text.strip()
        # ['SpecialTerms'] = ('cbc', 'specialterms', 'Seçimli (0...1)')
        specialterms_: Element = element.find('./' + cbcnamespace + 'SpecialTerms')
        if specialterms_ is not None:
            if specialterms_.text is not None:
                frappedoc['specialterms'] = specialterms_.text.strip()
        # ['Amount'] = ('cbc', 'amount', 'Seçimli (0...1)')
        amount_: Element = element.find('./' + cbcnamespace + 'Amount')
        if amount_ is not None:
            if amount_.text is not None:
                frappedoc['amount'] = amount_.text.strip()
                frappedoc['amountcurrencyid'] = amount_.attrib.get('currencyID').strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
