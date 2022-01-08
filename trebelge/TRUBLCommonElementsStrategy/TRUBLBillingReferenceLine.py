from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLBillingReferenceLine(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR BillingReferenceLine'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        id_ = element.find('./' + cbcnamespace + 'ID').text
        if id_ is None:
            return None
        frappedoc: dict = {'id': id_}
        # ['Amount'] = ('cbc', '', 'Seçimli (0..1)')
        amount_: Element = element.find('./' + cbcnamespace + 'Amount')
        if amount_ is not None:
            if amount_.text is not None:
                frappedoc['amount'] = amount_.text
                frappedoc['amountcurrencyid'] = amount_.attrib.get('currencyID')
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge.', 'Seçimli (0...n)', 'allowancecharge')
        allowancecharges_: list = element.findall('./' + cacnamespace + 'AllowanceCharge')
        if len(allowancecharges_) != 0:
            allowancecharge: list = []
            for allowancecharge_ in allowancecharges_:
                tmp = TRUBLAllowanceCharge().process_element(allowancecharge_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    allowancecharge.append(tmp)
            if len(allowancecharge) != 0:
                document.allowancecharge = allowancecharge
                document.save()

        return document
