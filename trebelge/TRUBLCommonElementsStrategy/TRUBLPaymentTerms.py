from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLPaymentTerms(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR PaymentTerms'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        # ['PenaltySurchargePercent'] = ('cbc', 'penaltysurchargepercent', 'Seçimli (0...1)')
        # ['PaymentDueDate'] = ('cbc', 'paymentduedate', 'Seçimli (0...1)')
        cbcsecimli01: list = ['Note', 'PenaltySurchargePercent', 'PaymentDueDate']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['Amount'] = ('cbc', 'amount', 'Seçimli (0...1)')
        amount_: Element = element.find('./' + cbcnamespace + 'Amount')
        if amount_ is not None:
            if amount_.text is not None:
                frappedoc['amount'] = amount_.text
                frappedoc['amountcurrencyid'] = amount_.attrib.get('currencyID')
        # ['PenaltyAmount'] = ('cbc', 'penaltyamount', 'Seçimli (0...1)')
        penaltyamount_: Element = element.find('./' + cbcnamespace + 'PenaltyAmount')
        if penaltyamount_ is not None:
            if penaltyamount_.text is not None:
                frappedoc['penaltyamount'] = penaltyamount_.text
                frappedoc['penaltyamountcurrencyid'] = penaltyamount_.attrib.get('currencyID')
        # ['SettlementPeriod'] = ('cac', 'settlementperiod', 'Seçimli (0...1)')
        settlementperiod_: Element = element.find('./' + cbcnamespace + 'SettlementPeriod')
        if settlementperiod_ is not None:
            tmp = TRUBLPeriod().process_element(settlementperiod_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['settlementperiod'] = tmp.name
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)
