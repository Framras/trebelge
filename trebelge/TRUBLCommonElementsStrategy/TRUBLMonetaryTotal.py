from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLMonetaryTotal(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR MonetaryTotal'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LineExtensionAmount'] = ('cbc', 'lineextensionamount', 'Zorunlu(1)')
        # ['TaxExclusiveAmount'] = ('cbc', 'taxexclusiveamount', 'Zorunlu(1)')
        # ['TaxInclusiveAmount'] = ('cbc', 'taxinclusiveamount', 'Zorunlu(1)')
        # ['PayableAmount'] = ('cbc', 'payableamount', 'Zorunlu(1)')
        lineextensionamount_: Element = element.find(cbcnamespace + 'LineExtensionAmount')
        taxexclusiveamount_: Element = element.find(cbcnamespace + 'TaxExclusiveAmount')
        taxinclusiveamount_: Element = element.find(cbcnamespace + 'TaxInclusiveAmount')
        payableamount_: Element = element.find(cbcnamespace + 'PayableAmount')
        frappedoc: dict = {'lineextensionamount': lineextensionamount_.text,
                           'lineextensionamountcurrencyid': lineextensionamount_.attrib.get('currencyID'),
                           'taxexclusiveamount': taxexclusiveamount_.text,
                           'taxexclusiveamountcurrencyid': taxexclusiveamount_.attrib.get('currencyID'),
                           'taxinclusiveamount': taxinclusiveamount_.text,
                           'taxinclusiveamountcurrencyid': taxinclusiveamount_.attrib.get('currencyID'),
                           'payableamount': payableamount_.text,
                           'payableamountcurrencyid': payableamount_.attrib.get('currencyID')
                           }
        # ['AllowanceTotalAmount'] = ('cbc', 'allowancetotalamount', 'Seçimli (0...1)')
        allowancetotalamount_: Element = element.find(cbcnamespace + 'AllowanceTotalAmount')
        if not allowancetotalamount_:
            frappedoc['allowancetotalamount'] = allowancetotalamount_.text
            frappedoc['allowancetotalamount_currencyid'] = allowancetotalamount_.attrib.get(
                'currencyID')
        # ['ChargeTotalAmount'] = ('cbc', 'chargetotalamount', 'Seçimli (0...1)')
        chargetotalamount_: Element = element.find(cbcnamespace + 'ChargeTotalAmount')
        if not chargetotalamount_:
            frappedoc['chargetotalamount'] = chargetotalamount_.text
            frappedoc['chargetotalamount_currencyid'] = chargetotalamount_.attrib.get(
                'currencyID')
        # ['PayableRoundingAmount'] = ('cbc', 'payableroundingamount', 'Seçimli (0...1)')
        payableroundingamount_: Element = element.find(cbcnamespace + 'PayableRoundingAmount')
        if not payableroundingamount_:
            frappedoc['payableroundingamount'] = payableroundingamount_.text
            frappedoc['payableroundingamount_currencyid'] = payableroundingamount_.attrib.get(
                'currencyID')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
