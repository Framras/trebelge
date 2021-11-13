# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class DespatchLine(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'DespatchLine'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..n): Note
        self._mapping['Note'] = ('cbc', '', 'Seçimli(0..n)', False, False, True)
        # Seçimli(0..1): DeliveredQuantity
        self._mapping['DeliveredQuantity'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): OutstandingQuantity
        self._mapping['OutstandingQuantity'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Seçimli(0..n): OutstandingReason
        self._mapping['OutstandingReason'] = ('cbc', '', 'Seçimli(0..n)', False, False, True)
        # Seçimli(0..1): OversupplyQuantity
        self._mapping['OversupplyQuantity'] = ('cbc', '', 'Seçimli(0..1)', False, False, True)
        # Zorunlu(1): OrderLineReference:OrderLineReference
        self._mapping['OrderLineReference'] = ('cac', 'OrderLineReference', 'Zorunlu(1)', True, False, False)
        # Seçimli(0..n): DocumentReference:DocumentReference
        self._mapping['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli(0..n)', True, False, False)
        # Zorunlu(1): Item:Item
        self._mapping['Item'] = ('cac', 'Item', 'Zorunlu(1)', True, False, False)
        # Seçimli(0..n): Shipment:Shipment
        self._mapping['Shipment'] = ('cac', 'Shipment', 'Seçimli(0..n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
