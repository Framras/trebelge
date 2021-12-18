from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLMonetaryTotal(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        """
        ['LineExtensionAmount'] = ('cbc', 'lineextensionamount', 'Zorunlu(1)')
        ['currencyID'] = ('', 'lineextensionamount_currencyid', 'Zorunlu(1)')
        ['TaxExclusiveAmount'] = ('cbc', 'taxexclusiveamount', 'Zorunlu(1)')
        ['currencyID'] = ('', 'taxexclusiveamount_currencyid', 'Zorunlu(1)')
        ['TaxInclusiveAmount'] = ('cbc', 'taxinclusiveamount', 'Zorunlu(1)')
        ['currencyID'] = ('', 'taxinclusiveamount_currencyid', 'Zorunlu(1)')
        ['AllowanceTotalAmount'] = ('cbc', 'allowancetotalamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'allowancetotalamount_currencyid', 'Zorunlu(1)')
        ['ChargeTotalAmount'] = ('cbc', 'chargetotalamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'chargetotalamount_currencyid', 'Zorunlu(1)')
        ['PayableRoundingAmount'] = ('cbc', 'payableroundingamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'payableroundingamount_currencyid', 'Zorunlu(1)')
        ['PayableAmount'] = ('cbc', 'payableamount', 'Zorunlu(1)')
        ['currencyID'] = ('', 'payableamount_currencyid', 'Zorunlu(1)')
        """
        lineextensionamount_ = element.find(cbcnamespace + 'LineExtensionAmount')
        taxexclusiveamount_ = element.find(cbcnamespace + 'TaxExclusiveAmount')
        taxinclusiveamount_ = element.find(cbcnamespace + 'TaxInclusiveAmount')
        payableamount_ = element.find(cbcnamespace + 'PayableAmount')
        monetarytotal: dict = {'lineextensionamount': lineextensionamount_.text,
                               'lineextensionamount_currencyid': lineextensionamount_.attrib.get('currencyID'),
                               'taxexclusiveamount': taxexclusiveamount_.text,
                               'taxexclusiveamount_currencyid': taxexclusiveamount_.attrib.get('currencyID'),
                               'taxinclusiveamount': taxinclusiveamount_.text,
                               'taxinclusiveamount_currencyid': taxinclusiveamount_.attrib.get('currencyID'),
                               'payableamount': payableamount_.text,
                               'payableamount_currencyid': payableamount_.attrib.get('currencyID')
                               }
        allowancetotalamount_ = element.find(cbcnamespace + 'AllowanceTotalAmount')
        if allowancetotalamount_ is not None:
            monetarytotal['allowancetotalamount'] = allowancetotalamount_.text
            monetarytotal['allowancetotalamount_currencyid'] = allowancetotalamount_.attrib.get(
                'currencyID')
        chargetotalamount_ = element.find(cbcnamespace + 'ChargeTotalAmount')
        if chargetotalamount_ is not None:
            monetarytotal['chargetotalamount'] = chargetotalamount_.text
            monetarytotal['chargetotalamount_currencyid'] = chargetotalamount_.attrib.get(
                'currencyID')
        payableroundingamount_ = element.find(cbcnamespace + 'PayableRoundingAmount')
        if payableroundingamount_ is not None:
            monetarytotal['payableroundingamount'] = payableroundingamount_.text
            monetarytotal['payableroundingamount_currencyid'] = payableroundingamount_.attrib.get(
                'currencyID')

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
