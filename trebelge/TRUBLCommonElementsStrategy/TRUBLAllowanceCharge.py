from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLAllowanceCharge(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR AllowanceCharge'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ChargeIndicator'] = ('cbc', 'chargeindicator', 'Zorunlu (1)')
        chargeindicator_: Element = element.find('./' + cbcnamespace + 'ChargeIndicator')
        if chargeindicator_ is not None:
            if chargeindicator_.text is not None:
                frappedoc['chargeindicator'] = chargeindicator_.text.strip()
        # ['Amount'] = ('cbc', 'allowancechargeamount', 'Zorunlu (1)')
        amount_: Element = element.find('./' + cbcnamespace + 'Amount')
        if amount_ is not None:
            if amount_.text is not None:
                frappedoc['amount'] = amount_.text.strip()
                frappedoc['amountcurrencyid'] = amount_.attrib.get('currencyID').strip()
        # ['AllowanceChargeReason'] = ('cbc', 'allowancechargereason', 'Seçimli (0...1)')
        # ['MultiplierFactorNumeric'] = ('cbc', 'multiplierfactornumeric', 'Seçimli (0...1)')
        # ['SequenceNumeric'] = ('cbc', 'sequencenumeric', 'Seçimli (0...1)')
        cbcsecimli01: list = ['AllowanceChargeReason', 'MultiplierFactorNumeric', 'SequenceNumeric']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['BaseAmount'] = ('cbc', 'baseamount', 'Seçimli (0...1)')
        baseamount_: Element = element.find('./' + cbcnamespace + 'BaseAmount')
        if baseamount_ is not None:
            if baseamount_.text is not None:
                frappedoc['baseamount'] = baseamount_.text.strip()
                frappedoc['baseamountcurrencyid'] = baseamount_.attrib.get('currencyID').strip()
        # ['PerUnitAmount'] = ('cbc', 'perunitamount', 'Seçimli (0...1)')
        perunitamount_: Element = element.find('./' + cbcnamespace + 'PerUnitAmount')
        if perunitamount_ is not None:
            if perunitamount_.text is not None:
                frappedoc['perunitamount'] = perunitamount_.text.strip()
                frappedoc['perunitamountcurrencyid'] = perunitamount_.attrib.get('currencyID').strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc, False)
