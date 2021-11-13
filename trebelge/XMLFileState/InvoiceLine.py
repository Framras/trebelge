# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class InvoiceLine(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'InvoiceLine'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Seçimli(0..1): Note
        self._mapping['Note'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Zorunlu(1): InvoicedQuantity
        self._mapping['InvoicedQuantity'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Zorunlu(1): LineExtensionAmount
        self._mapping['LineExtensionAmount'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Seçimli(0..n): OrderLineReference:OrderLineReference
        self._mapping['OrderLineReference'] = (
            'cac', 'OrderLineReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): DespatchLineReference:LineReference
        self._mapping['DespatchLineReference'] = (
            'cac', 'LineReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): ReceiptLineReference:LineReference
        self._mapping['ReceiptLineReference'] = (
            'cac', 'LineReference', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): Delivery:Delivery
        self._mapping['Delivery'] = (
            'cac', 'Delivery', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): AllowanceCharge:AllowanceCharge
        self._mapping['AllowanceCharge'] = (
            'cac', 'AllowanceCharge', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..1): TaxTotal:TaxTotal
        self._mapping['TaxTotal'] = ('cac', 'TaxTotal', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..n): WithholdingTaxTotal:TaxTotal
        self._mapping['WithholdingTaxTotal'] = (
            'cac', 'TaxTotal', 'Seçimli (0...n)', True, False, False)
        # Zorunlu(1): Item:Item
        self._mapping['Item'] = ('cac', 'Item', 'Zorunlu (1)', True, False, False)
        # Zorunlu(1): Price:Price
        self._mapping['Price'] = ('cac', 'Price', 'Zorunlu (1)', True, False, False)
        # Seçimli(0..n): SubInvoiceLine:InvoiceLine
        self._mapping['SubInvoiceLine'] = (
            'cac', 'InvoiceLine', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
