from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLPrice import TRUBLPrice
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal


class TRUBLInvoiceLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR InvoiceLine'

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
        frappedoc['item'] = TRUBLItem().process_element(item_,
                                                        cbcnamespace,
                                                        cacnamespace).name
        # ['Price'] = ('cac', 'Price', 'Zorunlu (1)')
        price_: Element = element.find('./' + cacnamespace + 'Price')
        frappedoc['price'] = TRUBLPrice().process_element(price_,
                                                          cbcnamespace,
                                                          cacnamespace).name
        # ['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)')
        taxtotal_: Element = element.find('./' + cacnamespace + 'TaxTotal')
        if taxtotal_ is not None:
            frappedoc['taxtotal'] = TRUBLTaxTotal().process_element(taxtotal_,
                                                                    cbcnamespace,
                                                                    cacnamespace).name
        document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
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
            if len(tagelements_) != 0:
                tagelements: list = []
                for tagelement_ in tagelements_:
                    tagelements.append(element_.get('strategy').process_element(tagelement_,
                                                                                cbcnamespace,
                                                                                cacnamespace))
                    element_.strategy = TRUBLAllowanceCharge()
                document.db_set(element_.get('fieldName'), tagelements)
                document.save()

        return document
