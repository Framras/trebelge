from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLBillingReferenceLine(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR BillingReferenceLine'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

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
            strategy: TRUBLCommonElement = TRUBLAllowanceCharge()
            self._strategyContext.set_strategy(strategy)
            for allowancecharge_ in allowancecharges_:
                allowancecharge.append(self._strategyContext.return_element_data(allowancecharge_,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
            frappedoc['allowancecharge'] = allowancecharge

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
