from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLInvoiceLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR InvoiceLine'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        # ['InvoicedQuantity'] = ('cbc', '', 'Zorunlu (1)')
        # ['LineExtensionAmount'] = ('cbc', '', 'Zorunlu (1)')
        invoicedquantity: Element = element.find(cbcnamespace + 'InvoicedQuantity')
        lineextensionamount: Element = element.find(cbcnamespace + 'LineExtensionAmount')
        frappedoc: dict = {'id': element.find(cbcnamespace + 'ID').text,
                           'invoicedquantity': invoicedquantity.text,
                           'invoicedquantityunitcode': invoicedquantity.attrib.get('unitCode'),
                           'lineextensionamount': lineextensionamount.text,
                           'lineextensionamountcurrencyid': lineextensionamount.attrib.get('currencyID')}

        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        note_: Element = element.find(cbcnamespace + 'Note')
        if note_:
            frappedoc['note'] = note_.text

        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        # ['Price'] = ('cac', 'Price', 'Zorunlu (1)')

        # ['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)')

        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...n)')
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        # ['ReceiptLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)')
        # ['WithholdingTaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...n)')
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)')
        # ['SubInvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli (0...n)')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
