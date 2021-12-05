from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAllowanceCharge(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ChargeIndicator'] = ('cbc', 'chargeindicator', 'Zorunlu (1)')
        ['AllowanceChargeReason'] = ('cbc', 'allowancechargereason', 'Seçimli (0...1)')
        ['MultiplierFactorNumeric'] = ('cbc', 'multiplierfactornumeric', 'Seçimli (0...1)')
        ['SequenceNumeric'] = ('cbc', 'sequencenumeric', 'Seçimli (0...1)')
        ['Amount'] = ('cbc', 'allowancechargeamount', 'Zorunlu (1)')
        ['currencyID'] = ('', 'allowancechargeamount_currencyid', 'Zorunlu(1)')
        ['BaseAmount'] = ('cbc', 'baseamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'baseamount_currencyid', 'Zorunlu(1)')
        ['PerUnitAmount'] = ('cbc', 'perunitamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'perunitamount_currencyid', 'Zorunlu(1)')
        """
        amount_ = element.find(cbcnamespace + 'Amount')
        allowancecharge: dict = {'chargeindicator': element.find(cbcnamespace + 'ChargeIndicator'),
                                 'allowancechargeamount': amount_.text,
                                 'allowancechargeamount_currencyid': amount_.attrib.get('currencyID')}
        cbcsecimli01: list = ['AllowanceChargeReason', 'MultiplierFactorNumeric', 'SequenceNumeric']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                allowancecharge[field_.tag.lower()] = field_.text

        baseamount_ = element.find(cbcnamespace + 'BaseAmount')
        if baseamount_ is not None:
            allowancecharge['baseamount'] = baseamount_.text
            allowancecharge['baseamount_currencyid'] = baseamount_.attrib.get('currencyID')
        perunitamount_ = element.find(cbcnamespace + 'PerUnitAmount')
        if perunitamount_ is not None:
            allowancecharge['perunitamount'] = perunitamount_.text
            allowancecharge['perunitamount_currencyid'] = perunitamount_.attrib.get('currencyID')

        return allowancecharge
