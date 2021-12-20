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
        lineextensionamount = element.find(cbcnamespace + 'LineExtensionAmount')
        taxexclusiveamount = element.find(cbcnamespace + 'TaxExclusiveAmount')
        taxinclusiveamount = element.find(cbcnamespace + 'TaxInclusiveAmount')
        payableamount = element.find(cbcnamespace + 'PayableAmount')
        frappedoc: dict = {'lineextensionamount': lineextensionamount.text,
                           'lineextensionamountcurrencyid': lineextensionamount.attrib.get('currencyID'),
                           'taxexclusiveamount': taxexclusiveamount.text,
                           'taxexclusiveamountcurrencyid': taxexclusiveamount.attrib.get('currencyID'),
                           'taxinclusiveamount': taxinclusiveamount.text,
                           'taxinclusiveamountcurrencyid': taxinclusiveamount.attrib.get('currencyID'),
                           'payableamount': payableamount.text,
                           'payableamountcurrencyid': payableamount.attrib.get('currencyID')
                           }
        # ['AllowanceTotalAmount'] = ('cbc', 'allowancetotalamount', 'Seçimli (0...1)')
        allowancetotalamount_ = element.find(cbcnamespace + 'AllowanceTotalAmount')
        if allowancetotalamount_ is not None:
            frappedoc['allowancetotalamount'] = allowancetotalamount_.text
            frappedoc['allowancetotalamount_currencyid'] = allowancetotalamount_.attrib.get(
                'currencyID')
        # ['ChargeTotalAmount'] = ('cbc', 'chargetotalamount', 'Seçimli (0...1)')
        chargetotalamount_ = element.find(cbcnamespace + 'ChargeTotalAmount')
        if chargetotalamount_ is not None:
            frappedoc['chargetotalamount'] = chargetotalamount_.text
            frappedoc['chargetotalamount_currencyid'] = chargetotalamount_.attrib.get(
                'currencyID')
        # ['PayableRoundingAmount'] = ('cbc', 'payableroundingamount', 'Seçimli (0...1)')
        payableroundingamount_ = element.find(cbcnamespace + 'PayableRoundingAmount')
        if payableroundingamount_ is not None:
            frappedoc['payableroundingamount'] = payableroundingamount_.text
            frappedoc['payableroundingamount_currencyid'] = payableroundingamount_.attrib.get(
                'currencyID')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
