# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class OrderLineReference(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'OrderLineReference'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): LineID
        self._mapping['LineID'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): SalesOrderLineID
        self._mapping['SalesOrderLineID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): UUID
        self._mapping['UUID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): LineStatusCode
        self._mapping['LineStatusCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): OrderReference:OrderReference
        self._mapping['OrderReference'] = (
            'cac', 'OrderReference', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
