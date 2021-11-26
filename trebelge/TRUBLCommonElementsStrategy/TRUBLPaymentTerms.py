from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLPaymentTerms(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        ['PenaltySurchargePercent'] = ('cbc', 'penaltysurchargepercent', 'Seçimli (0...1)')
        ['Amount'] = ('cbc', 'amount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'amount_currencyid', 'Zorunlu(1)')
        ['PenaltyAmount'] = ('cbc', 'penaltyamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'penaltyamount_currencyid', 'Zorunlu(1)')
        ['PaymentDueDate'] = ('cbc', 'paymentduedate', 'Seçimli (0...1)')
        ['SettlementPeriod'] = ('cac', 'settlementperiod', 'Seçimli (0...1)')
        """
        paymentterms: dict = {}
        note_ = element.find(cbcnamespace + 'Note')
        if note_ is not None:
            paymentterms['note'] = note_.text
        penaltysurchargepercent_ = element.find(cbcnamespace + 'PenaltySurchargePercent')
        if penaltysurchargepercent_ is not None:
            paymentterms['penaltysurchargepercent'] = penaltysurchargepercent_.text
        amount_ = element.find(cbcnamespace + 'Amount')
        if amount_ is not None:
            paymentterms['amount'] = amount_.text
            paymentterms['amount_currencyid'] = amount_.attrib.get('currencyID')
        penaltyamount_ = element.find(cbcnamespace + 'PenaltyAmount')
        if penaltyamount_ is not None:
            paymentterms['penaltyamount'] = penaltyamount_.text
            paymentterms['penaltyamount_currencyid'] = penaltyamount_.attrib.get('currencyID')
        paymentduedate_ = element.find(cbcnamespace + 'PaymentDueDate')
        if paymentduedate_ is not None:
            paymentterms['paymentduedate'] = paymentduedate_.text
        settlementperiod_ = element.find(cbcnamespace + 'SettlementPeriod')
        if settlementperiod_ is not None:
            strategy: TRUBLCommonElement = TRUBLPeriod()
            self._strategyContext.set_strategy(strategy)
            period_ = self._strategyContext.return_element_data(settlementperiod_, cbcnamespace, cacnamespace)
            for key in period_.keys():
                if period_.get(key) is not None:
                    paymentterms['settlementperiod_' + key] = period_.get(key)

        return paymentterms
