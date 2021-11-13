# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Stowage(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Stowage'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): LocationID
        self._mapping['LocationID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): Location:Location
        self._mapping['Location'] = (
            'cac', 'Location', 'Seçimli (0...n)', True, False, False)
        # Seçimli(0..n): MeasurementDimension:Dimension
        self._mapping['MeasurementDimension'] = (
            'cac', 'Dimension', 'Seçimli (0...n)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
