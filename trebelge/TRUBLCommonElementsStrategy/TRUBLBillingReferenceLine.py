from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLBillingReferenceLine(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR BillingReferenceLine'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text}
        # ['Amount'] = ('cbc', '', 'Seçimli (0..1)')
        amount_: Element = element.find('./' + cbcnamespace + 'Amount')
        if amount_:
            frappedoc['amount'] = amount_.text
            frappedoc['amountcurrencyid'] = amount_.attrib.get('currencyID')
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge.', 'Seçimli (0...n)', 'allowancecharge')
        allowancecharges_: list = element.findall('./' + cacnamespace + 'AllowanceCharge')
        if allowancecharges_:
            allowancecharge: list = []
            for allowancecharge_ in allowancecharges_:
                allowancecharge.append(TRUBLAllowanceCharge.process_element(allowancecharge_,
                                                                            cbcnamespace,
                                                                            cacnamespace))
            frappedoc['allowancecharge'] = allowancecharge

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
