from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLLegalMonetaryTotal(TRUBLCommonElement):

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        pass

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        # ['LineExtensionAmount'] = ('cbc', 'lineextensionamount', 'Zorunlu(1)')
        lineextensionamount_: Element = element.find('./' + cbcnamespace + 'LineExtensionAmount')
        # ['TaxExclusiveAmount'] = ('cbc', 'taxexclusiveamount', 'Zorunlu(1)')
        taxexclusiveamount_: Element = element.find('./' + cbcnamespace + 'TaxExclusiveAmount')
        # ['TaxInclusiveAmount'] = ('cbc', 'taxinclusiveamount', 'Zorunlu(1)')
        taxinclusiveamount_: Element = element.find('./' + cbcnamespace + 'TaxInclusiveAmount')
        # ['PayableAmount'] = ('cbc', 'payableamount', 'Zorunlu(1)')
        payableamount_: Element = element.find('./' + cbcnamespace + 'PayableAmount')
        frappedata = dict(lineextensionamount=lineextensionamount_.text.strip(),
                          lineextensionamountcurrencyid=lineextensionamount_.attrib.get('currencyID'),
                          taxexclusiveamount=taxexclusiveamount_.text.strip(),
                          taxexclusiveamountcurrencyid=taxexclusiveamount_.attrib.get('currencyID'),
                          taxinclusiveamount=taxinclusiveamount_.text.strip(),
                          taxinclusiveamountcurrencyid=taxinclusiveamount_.attrib.get('currencyID'),
                          payableamount=payableamount_.text.strip(),
                          payableamountcurrencyid=payableamount_.attrib.get('currencyID')
                          )
        # ['AllowanceTotalAmount'] = ('cbc', 'allowancetotalamount', 'Seçimli (0...1)')
        allowancetotalamount_: Element = element.find('./' + cbcnamespace + 'AllowanceTotalAmount')
        if allowancetotalamount_ is not None and allowancetotalamount_.text is not None:
            frappedata.allowancetotalamount = allowancetotalamount_.text.strip()
            frappedata.allowancetotalamountcurrencyid = allowancetotalamount_.attrib.get('currencyID')
        # ['ChargeTotalAmount'] = ('cbc', 'chargetotalamount', 'Seçimli (0...1)')
        chargetotalamount_: Element = element.find('./' + cbcnamespace + 'ChargeTotalAmount')
        if chargetotalamount_ is not None and chargetotalamount_.text is not None:
            frappedata.chargetotalamount = chargetotalamount_.text.strip()
            frappedata.chargetotalamountcurrencyid = chargetotalamount_.attrib.get('currencyID')
        # ['PayableRoundingAmount'] = ('cbc', 'payableroundingamount', 'Seçimli (0...1)')
        payableroundingamount_: Element = element.find('./' + cbcnamespace + 'PayableRoundingAmount')
        if payableroundingamount_ is not None and payableroundingamount_.text is not None:
            frappedata.payableroundingamount = payableroundingamount_.text.strip()
            frappedata.payableroundingamountcurrencyid = payableroundingamount_.attrib.get('currencyID')

        return frappedata
