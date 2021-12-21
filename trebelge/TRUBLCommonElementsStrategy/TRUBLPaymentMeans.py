from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext

from apps.frappe.frappe.model.document import Document


class TRUBLPaymentMeans(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['PaymentMeansCode'] = ('cbc', '', 'Zorunlu(1)')
        frappedoc: dict = {'paymentmeanscode': element.find(cbcnamespace + 'PaymentMeansCode').text}
        # ['PaymentDueDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['PaymentChannelCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['InstructionNote'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['PaymentDueDate', 'PaymentChannelCode', 'InstructionNote']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        # ['PayerFinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)')
        # ['PayeeFinancialAccount'] = ('cac', 'FinancialAccount', 'Seçimli (0...1)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
