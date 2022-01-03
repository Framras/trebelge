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
        lineextensionamount_: Element = element.find('./' + cbcnamespace + 'LineExtensionAmount')
        taxexclusiveamount_: Element = element.find('./' + cbcnamespace + 'TaxExclusiveAmount')
        taxinclusiveamount_: Element = element.find('./' + cbcnamespace + 'TaxInclusiveAmount')
        payableamount_: Element = element.find('./' + cbcnamespace + 'PayableAmount')
        if lineextensionamount_ is None or lineextensionamount_.text is None or \
                taxexclusiveamount_ is None or taxexclusiveamount_.text is None or \
                taxinclusiveamount_ is None or taxinclusiveamount_.text is None or \
                payableamount_ is None or payableamount_.text is None:
            return None
        frappedoc: dict = dict(lineextensionamount=lineextensionamount_.text,
                               lineextensionamountcurrencyid=lineextensionamount_.attrib.get('currencyID'),
                               taxexclusiveamount=taxexclusiveamount_.text,
                               taxexclusiveamountcurrencyid=taxexclusiveamount_.attrib.get('currencyID'),
                               taxinclusiveamount=taxinclusiveamount_.text,
                               taxinclusiveamountcurrencyid=taxinclusiveamount_.attrib.get('currencyID'),
                               payableamount=payableamount_.text,
                               payableamountcurrencyid=payableamount_.attrib.get('currencyID')
                               )
        # ['AllowanceTotalAmount'] = ('cbc', 'allowancetotalamount', 'Seçimli (0...1)')
        allowancetotalamount_: Element = element.find('./' + cbcnamespace + 'AllowanceTotalAmount')
        if allowancetotalamount_ is not None:
            if allowancetotalamount_.text is not None:
                frappedoc['allowancetotalamount'] = allowancetotalamount_.text
                frappedoc['allowancetotalamountcurrencyid'] = allowancetotalamount_.attrib.get(
                    'currencyID')
        # ['ChargeTotalAmount'] = ('cbc', 'chargetotalamount', 'Seçimli (0...1)')
        chargetotalamount_: Element = element.find('./' + cbcnamespace + 'ChargeTotalAmount')
        if chargetotalamount_ is not None:
            if chargetotalamount_.text is not None:
                frappedoc['chargetotalamount'] = chargetotalamount_.text
                frappedoc['chargetotalamountcurrencyid'] = chargetotalamount_.attrib.get(
                    'currencyID')
        # ['PayableRoundingAmount'] = ('cbc', 'payableroundingamount', 'Seçimli (0...1)')
        payableroundingamount_: Element = element.find('./' + cbcnamespace + 'PayableRoundingAmount')
        if payableroundingamount_ is not None:
            if payableroundingamount_.text is not None:
                frappedoc['payableroundingamount'] = payableroundingamount_.text
                frappedoc['payableroundingamountcurrencyid'] = payableroundingamount_.attrib.get(
                    'currencyID')

        return self._get_frappedoc(self._frappeDoctype, frappedoc, False)
