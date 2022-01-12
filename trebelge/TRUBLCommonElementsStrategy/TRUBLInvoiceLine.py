from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal


class TRUBLInvoiceLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR InvoiceLine'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        # ['InvoicedQuantity'] = ('cbc', '', 'Zorunlu (1)')
        # ['LineExtensionAmount'] = ('cbc', '', 'Zorunlu (1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        invoicedquantity: Element = element.find('./' + cbcnamespace + 'InvoicedQuantity')
        lineextensionamount: Element = element.find('./' + cbcnamespace + 'LineExtensionAmount')
        if id_ is None or id_.text is None or \
                invoicedquantity is None or invoicedquantity.text is None or \
                lineextensionamount is None or lineextensionamount.text is None:
            return None
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text,
                           'invoicedquantity': invoicedquantity.text,
                           'invoicedquantityunitcode': invoicedquantity.attrib.get('unitCode'),
                           'lineextensionamount': lineextensionamount.text,
                           'lineextensionamountcurrencyid': lineextensionamount.attrib.get('currencyID')}
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        note_ = element.find('./' + cbcnamespace + 'Note')
        if note_ is not None:
            if note_.text is not None:
                frappedoc['note'] = note_
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        tmp = TRUBLItem().process_element(item_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc['item'] = tmp.name
        # ['Price'] = ('cac', 'Price', 'Zorunlu (1)')
        price_: Element = element.find('./' + cacnamespace + 'Price')
        # self._mapping['PriceAmount'] = ('cbc', '', 'Zorunlu(1)')
        priceamount = price_.find('./' + cbcnamespace + 'PriceAmount')
        if priceamount is not None and priceamount.text is not None:
            frappedoc['priceamount'] = priceamount.text
            frappedoc['priceamountcurrencyid'] = priceamount.attrib.get('currencyID')
        # ['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)')
        taxtotal_: Element = element.find('./' + cacnamespace + 'TaxTotal')
        if taxtotal_ is not None:
            tmp = TRUBLTaxTotal().process_element(taxtotal_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['taxtotal'] = tmp.name
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...n)')
        orderlinereference = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'OrderLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLOrderLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    orderlinereference.append(tmp)
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        despatchlinereference = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'DespatchLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    despatchlinereference.append(tmp)
        # ['ReceiptLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        receiptlinereference = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'ReceiptLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    receiptlinereference.append(tmp)
        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)')
        delivery = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'Delivery')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLDelivery().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    delivery.append(tmp)
        # ['WithholdingTaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...n)')
        withholdingtaxtotal = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'WithholdingTaxTotal')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLTaxTotal().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    withholdingtaxtotal.append(tmp)
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)')
        allowancecharge = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'AllowanceCharge')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLAllowanceCharge().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    allowancecharge.append(tmp)
        # ['SubInvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli (0...n)')
        subinvoiceline = list()
        tagelements_: list = element.findall('./' + cacnamespace + 'SubInvoiceLine')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLInvoiceLine().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    subinvoiceline.append(tmp)
        if len(orderlinereference) + len(despatchlinereference) + len(receiptlinereference) + \
                len(delivery) + len(withholdingtaxtotal) + len(allowancecharge) + \
                len(subinvoiceline):
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(orderlinereference) != 0:
                document.orderlinereference = orderlinereference
            if len(despatchlinereference) != 0:
                document.despatchlinereference = despatchlinereference
            if len(receiptlinereference) != 0:
                document.receiptlinereference = receiptlinereference
            if len(delivery) != 0:
                document.delivery = delivery
            if len(withholdingtaxtotal) != 0:
                document.withholdingtaxtotal = withholdingtaxtotal
            if len(allowancecharge) != 0:
                document.allowancecharge = allowancecharge
            if len(subinvoiceline) != 0:
                document.subinvoiceline = subinvoiceline
            document.save()

        return document
