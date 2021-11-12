# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Period(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['StartDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['StartTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['EndDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['EndTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['DurationMeasure'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        self._mapping['unitCode'] = ('cbc', '', 'Zorunlu (1)', True, False, False)
        self._mapping['Description'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Period'] = ('cac', 'Period', '', False, False, True)
