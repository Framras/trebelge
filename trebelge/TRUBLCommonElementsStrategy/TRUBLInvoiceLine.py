from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLPrice import TRUBLPrice
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
        tmp = TRUBLPrice().process_element(price_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc['price'] = tmp.name
        # ['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)')
        taxtotal_: Element = element.find('./' + cacnamespace + 'TaxTotal')
        if taxtotal_ is not None:
            tmp = TRUBLTaxTotal().process_element(taxtotal_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['taxtotal'] = tmp.name
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'OrderLineReference')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement_ in tagelements_:
                tmp = TRUBLOrderLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.orderlinereference = tagelements
                document.save()
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'DespatchLineReference')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.despatchlinereference = tagelements
                document.save()
        # ['ReceiptLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'ReceiptLineReference')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.receiptlinereference = tagelements
                document.save()
        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'Delivery')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement_ in tagelements_:
                tmp = TRUBLDelivery().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.delivery = tagelements
                document.save()
        # ['WithholdingTaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'WithholdingTaxTotal')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement_ in tagelements_:
                tmp = TRUBLTaxTotal().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.withholdingtaxtotal = tagelements
                document.save()
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'AllowanceCharge')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement_ in tagelements_:
                tmp = TRUBLAllowanceCharge().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.allowancecharge = tagelements
                document.save()
        # ['SubInvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'SubInvoiceLine')
        if len(tagelements_) != 0:
            tagelements: list = []
            for tagelement_ in tagelements_:
                tmp = TRUBLInvoiceLine().process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    tagelements.append(tmp)
            if len(tagelements) != 0:
                document.subinvoiceline = tagelements
                document.save()

        return document
