from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialAccount import TRUBLFinancialAccount

from apps.frappe.frappe.model.document import Document


class TRUBLPaymentMeans(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR PaymentMeans'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['PaymentMeansCode'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'paymentmeanscode': element.find('./' + cbcnamespace + 'PaymentMeansCode').text}
        # ['PaymentDueDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['PaymentChannelCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['InstructionNote'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['PaymentDueDate', 'PaymentChannelCode', 'InstructionNote']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['PayerFinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)')
        payerfinancialaccount_ = element.find('./' + cacnamespace + 'PayerFinancialAccount')
        if payerfinancialaccount_:
            strategy: TRUBLCommonElement = TRUBLFinancialAccount()
            self._strategyContext.set_strategy(strategy)
            frappedoc['payerfinancialaccount'] = [self._strategyContext.return_element_data(payerfinancialaccount_,
                                                                                            cbcnamespace,
                                                                                            cacnamespace)]
        # ['PayeeFinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)')
        payeefinancialaccount_ = element.find('./' + cacnamespace + 'PayeeFinancialAccount')
        if payeefinancialaccount_:
            strategy: TRUBLCommonElement = TRUBLFinancialAccount()
            self._strategyContext.set_strategy(strategy)
            frappedoc['payeefinancialaccount'] = [self._strategyContext.return_element_data(payeefinancialaccount_,
                                                                                            cbcnamespace,
                                                                                            cacnamespace)]

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
