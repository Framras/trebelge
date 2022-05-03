from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAllowanceCharge import TRUBLAllowanceCharge
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxSubtotal import TRUBLTaxSubtotal
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal


class TRUBLInvoiceLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR InvoiceLine'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        from trebelge.TRUBLCommonElementsStrategy.TRUBLDelivery import TRUBLDelivery
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Zorunlu(1)')
        # Kalem sıra numarası girilir.
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None:
            if id_.text is not None:
                frappedoc['id'] = id_.text.strip()
        # ['InvoicedQuantity'] = ('cbc', '', 'Zorunlu (1)')
        # Mal/hizmet miktarı birimi ile birlikte
        # girilir.
        invoicedquantity: Element = element.find('./' + cbcnamespace + 'InvoicedQuantity')
        if invoicedquantity is not None:
            if invoicedquantity.text is not None:
                frappedoc['invoicedquantity'] = invoicedquantity.text.strip()
                frappedoc['invoicedquantityunitcode'] = invoicedquantity.attrib.get('unitCode').strip()
        # ['LineExtensionAmount'] = ('cbc', '', 'Zorunlu (1)')
        # Mal/hizmet miktarı ile Mal/hizmet
        # birim fiyatının çarpımı ile bulunan tutardır (varsa iskonto
        # düşülür).
        lineextensionamount: Element = element.find('./' + cbcnamespace + 'LineExtensionAmount')
        if lineextensionamount is not None:
            if lineextensionamount.text is not None:
                frappedoc['lineextensionamount'] = lineextensionamount.text.strip()
                frappedoc['lineextensionamountcurrencyid'] = lineextensionamount.attrib.get('currencyID').strip()
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        note_ = element.find('./' + cbcnamespace + 'Note')
        if note_ is not None:
            if note_.text is not None:
                frappedoc['note'] = note_.text.strip()
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        # Mal/hizmet hakkında bilgiler buraya girilir.
        item_: Element = element.find('./' + cacnamespace + 'Item')
        tmp = TRUBLItem().process_element(item_, cbcnamespace, cacnamespace)
        if tmp is not None:
            frappedoc['item'] = tmp.name
        # ['Price'] = ('cac', 'Price', 'Zorunlu (1)')
        # Mal/hizmet birim fiyatı hakkında bilgiler buraya girilir.
        price_: Element = element.find('./' + cacnamespace + 'Price')
        # ['PriceAmount'] = ('cbc', '', 'Zorunlu(1)')
        priceamount: Element = price_.find('./' + cbcnamespace + 'PriceAmount')
        if priceamount is not None:
            if priceamount.text is not None:
                frappedoc['priceamount'] = priceamount.text.strip()
                frappedoc['priceamountcurrencyid'] = priceamount.attrib.get('currencyID').strip()
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)')
        taxtotal_: Element = element.find('./' + cacnamespace + 'TaxTotal')
        if taxtotal_ is not None:
            # ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
            taxamount_: Element = taxtotal_.find('./' + cbcnamespace + 'TaxAmount')
            if taxamount_ is not None:
                if taxamount_.text != '':
                    document.taxamount = taxamount_.text.strip()
                    document.taxamountcurrencyid = taxamount_.attrib.get('currencyID')
                    document.save()
            # ['TaxSubtotal'] = ('cac', 'taxsubtotals', 'Zorunlu(1..n)', 'taxsubtotal')
            taxsubtotals = list()
            for taxsubtotal_ in taxtotal_.findall('./' + cacnamespace + 'TaxSubtotal'):
                tmp = TRUBLTaxSubtotal().process_element(taxsubtotal_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    taxsubtotals.append(tmp)
            if len(taxsubtotals) != 0:
                doc_append = document.append("taxsubtotals", {})
                for taxsubtotal in taxsubtotals:
                    doc_append.taxsubtotals = taxsubtotal.name
                    document.save()
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'OrderLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLOrderLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                doc_append = document.append("orderlinereference", {})
                if tmp is not None:
                    doc_append.orderlinereference = tmp.name
                    document.save()
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'DespatchLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                doc_append = document.append("despatchlinereference", {})
                if tmp is not None:
                    doc_append.linereference = tmp.name
                    document.save()
        # ['ReceiptLineReference'] = ('cac', 'LineReference', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'ReceiptLineReference')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLLineReference().process_element(tagelement_, cbcnamespace, cacnamespace)
                doc_append = document.append("receiptlinereference", {})
                if tmp is not None:
                    doc_append.linereference = tmp.name
                    document.save()
        # ['Delivery'] = ('cac', 'Delivery', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'Delivery')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLDelivery().process_element(tagelement_, cbcnamespace, cacnamespace)
                doc_append = document.append("delivery", {})
                if tmp is not None:
                    doc_append.delivery = tmp.name
                    document.save()
        # ['WithholdingTaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'WithholdingTaxTotal')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLTaxTotal().process_element(tagelement_, cbcnamespace, cacnamespace)
                doc_append = document.append("withholdingtaxtotal", {})
                if tmp is not None:
                    doc_append.taxtotal = tmp.name
                    document.save()
        # ['AllowanceCharge'] = ('cac', 'AllowanceCharge', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'AllowanceCharge')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLAllowanceCharge().process_element(tagelement_, cbcnamespace, cacnamespace)
                doc_append = document.append("allowancecharge", {})
                if tmp is not None:
                    doc_append.allowancecharge = tmp.name
                    document.save()
        # ['SubInvoiceLine'] = ('cac', 'InvoiceLine', 'Seçimli (0...n)')
        tagelements_: list = element.findall('./' + cacnamespace + 'SubInvoiceLine')
        if len(tagelements_) != 0:
            for tagelement_ in tagelements_:
                tmp = TRUBLInvoiceLine().process_element(tagelement_, cbcnamespace, cacnamespace)
                doc_append = document.append("subinvoiceline", {})
                if tmp is not None:
                    doc_append.invoiceline = tmp.name
                    document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
