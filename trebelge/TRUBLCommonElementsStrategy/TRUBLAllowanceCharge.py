from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAllowanceCharge(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AllowanceCharge'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['ChargeIndicator'] = ('cbc', 'chargeindicator', 'Zorunlu (1)')
        # ['Amount'] = ('cbc', 'allowancechargeamount', 'Zorunlu (1)')
        # ['currencyID'] = ('', 'allowancechargeamount_currencyid', 'Zorunlu(1)')
        amount_ = element.find(cbcnamespace + 'Amount')
        allowancecharge: dict = {'chargeindicator': element.find(cbcnamespace + 'ChargeIndicator'),
                                 'amount': amount_.text,
                                 'amountcurrencyid': amount_.attrib.get('currencyID')}

        # ['AllowanceChargeReason'] = ('cbc', 'allowancechargereason', 'Seçimli (0...1)')
        # ['MultiplierFactorNumeric'] = ('cbc', 'multiplierfactornumeric', 'Seçimli (0...1)')
        # ['SequenceNumeric'] = ('cbc', 'sequencenumeric', 'Seçimli (0...1)')
        cbcsecimli01: list = ['AllowanceChargeReason', 'MultiplierFactorNumeric', 'SequenceNumeric']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                allowancecharge[field_.tag.lower()] = field_.text

        # ['BaseAmount'] = ('cbc', 'baseamount', 'Seçimli (0...1)')
        # ['currencyID'] = ('', 'baseamount_currencyid', 'Zorunlu(1)')
        baseamount_ = element.find(cbcnamespace + 'BaseAmount')
        if baseamount_ is not None:
            allowancecharge['baseamount'] = baseamount_.text
            allowancecharge['baseamountcurrencyid'] = baseamount_.attrib.get('currencyID')
        # ['PerUnitAmount'] = ('cbc', 'perunitamount', 'Seçimli (0...1)')
        # ['currencyID'] = ('', 'perunitamount_currencyid', 'Zorunlu(1)')
        perunitamount_ = element.find(cbcnamespace + 'PerUnitAmount')
        if perunitamount_ is not None:
            allowancecharge['perunitamount'] = perunitamount_.text
            allowancecharge['perunitamountcurrencyid'] = perunitamount_.attrib.get('currencyID')

        if not frappe.get_all(self._frappeDoctype, filters=allowancecharge):
            pass
        else:
            newallowancecharge = allowancecharge
            newallowancecharge['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newallowancecharge)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=allowancecharge)
