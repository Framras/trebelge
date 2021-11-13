# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Temperature(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Temperature'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): AttributeID
        self._mapping['AttributeID'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        # Zorunlu(1): Measure
        self._mapping['Measure'] = ('cbc', '', 'Zorunlu (1)', True, True, True)
        # Seçimli(0..n): Description
        self._mapping['Description'] = ('cbc', '', 'Seçimli (0...n)', False, False, True)
        # unitCode
        self._mapping['unitCode'] = ('', '', 'Zorunlu(1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
