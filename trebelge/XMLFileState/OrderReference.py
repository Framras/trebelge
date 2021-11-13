# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class OrderReference(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'OrderReference'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): SalesOrderID
        self._mapping['SalesOrderID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Zorunlu(1): IssueDate
        self._mapping['IssueDate'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): OrderTypeCode
        self._mapping['OrderTypeCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): DocumentReference:DocumentReference
        self._mapping['DocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
