from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAllowanceCharge(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AllowanceCharge'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ChargeIndicator'] = ('cbc', 'chargeindicator', 'Zorunlu (1)')
        # ['Amount'] = ('cbc', 'allowancechargeamount', 'Zorunlu (1)')
        amount_: Element = element.find('./' + cbcnamespace + 'Amount')
        frappedoc: dict = {'chargeindicator': element.find('./' + cbcnamespace + 'ChargeIndicator'),
                           'amount': amount_.text,
                           'amountcurrencyid': amount_.attrib.get('currencyID')}
        # ['AllowanceChargeReason'] = ('cbc', 'allowancechargereason', 'Seçimli (0...1)')
        # ['MultiplierFactorNumeric'] = ('cbc', 'multiplierfactornumeric', 'Seçimli (0...1)')
        # ['SequenceNumeric'] = ('cbc', 'sequencenumeric', 'Seçimli (0...1)')
        cbcsecimli01: list = ['AllowanceChargeReason', 'MultiplierFactorNumeric', 'SequenceNumeric']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[elementtag_.lower()] = field_.text
        # ['BaseAmount'] = ('cbc', 'baseamount', 'Seçimli (0...1)')
        baseamount_: Element = element.find('./' + cbcnamespace + 'BaseAmount')
        if baseamount_:
            frappedoc['baseamount'] = baseamount_.text
            frappedoc['baseamountcurrencyid'] = baseamount_.attrib.get('currencyID')
        # ['PerUnitAmount'] = ('cbc', 'perunitamount', 'Seçimli (0...1)')
        perunitamount_: Element = element.find('./' + cbcnamespace + 'PerUnitAmount')
        if perunitamount_:
            frappedoc['perunitamount'] = perunitamount_.text
            frappedoc['perunitamountcurrencyid'] = perunitamount_.attrib.get('currencyID')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
