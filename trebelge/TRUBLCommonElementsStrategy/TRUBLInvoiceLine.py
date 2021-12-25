from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLPrice import TRUBLPrice
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal


class TRUBLInvoiceLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR InvoiceLine'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        # ['InvoicedQuantity'] = ('cbc', '', 'Zorunlu (1)')
        # ['LineExtensionAmount'] = ('cbc', '', 'Zorunlu (1)')
        invoicedquantity: Element = element.find('./' + cbcnamespace + 'InvoicedQuantity')
        lineextensionamount: Element = element.find('./' + cbcnamespace + 'LineExtensionAmount')
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text,
                           'invoicedquantity': invoicedquantity.text,
                           'invoicedquantityunitcode': invoicedquantity.attrib.get('unitCode'),
                           'lineextensionamount': lineextensionamount.text,
                           'lineextensionamountcurrencyid': lineextensionamount.attrib.get('currencyID')}
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        note_: Element = element.find('./' + cbcnamespace + 'Note')
        if note_ is not None:
            frappedoc['note'] = note_.text
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        strategy: TRUBLCommonElement = TRUBLItem()
        self._strategyContext.set_strategy(strategy)
        frappedoc['item'] = [self._strategyContext.return_element_data(item_,
                                                                       cbcnamespace,
                                                                       cacnamespace)]
        # ['Price'] = ('cac', 'Price', 'Zorunlu (1)')
        price_: Element = element.find('./' + cacnamespace + 'Price')
        strategy: TRUBLCommonElement = TRUBLPrice()
        self._strategyContext.set_strategy(strategy)
        frappedoc['price'] = [self._strategyContext.return_element_data(price_,
                                                                        cbcnamespace,
                                                                        cacnamespace)]
        # ['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)')
        taxtotal_: Element = element.find('./' + cacnamespace + 'TaxTotal')
        if taxtotal_ is not None:
            strategy: TRUBLCommonElement = TRUBLTaxTotal()
            self._strategyContext.set_strategy(strategy)
            frappedoc['taxtotal'] = [self._strategyContext.return_element_data(taxtotal_,
                                                                               cbcnamespace,
                                                                               cacnamespace)]
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...n)')
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        # ['ReceiptLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)')
        # ['WithholdingTaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...n)')
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)')
        # ['SubInvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli (0...n)')
        cacsecimli0n: list = \
            [{'Tag': 'OrderLineReference', 'strategy': TRUBLOrderLineReference(), 'fieldName': 'orderlinereference'},
             {'Tag': 'DespatchLineReference', 'strategy': TRUBLLineReference(), 'fieldName': 'despatchlinereference'},
             {'Tag': 'ReceiptLineReference', 'strategy': TRUBLLineReference(), 'fieldName': 'receiptlinereference'},
             {'Tag': 'Delivery', 'strategy': TRUBLDelivery(), 'fieldName': 'delivery'},
             {'Tag': 'WithholdingTaxTotal', 'strategy': TRUBLTaxTotal(), 'fieldName': 'withholdingtaxtotal'},
             {'Tag': 'AllowanceCharge', 'strategy': TRUBLAllowanceCharge(), 'fieldName': 'allowancecharge'},
             {'Tag': 'SubInvoiceLine', 'strategy': TRUBLInvoiceLine(), 'fieldName': 'subinvoiceline'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall('./' + cacnamespace + element_.get('Tag'))
            if tagelements_ is not None:
                tagelements: list = []
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                for tagelement in tagelements_:
                    tagelements.append(self._strategyContext.return_element_data(tagelement,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
