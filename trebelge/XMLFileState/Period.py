# from __future__ import annotations
from xml.etree import ElementTree as ET

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Period(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'InvoicePeriod'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli (0..1): StartDate
        self._mapping['StartDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli (0..1): StartTime
        self._mapping['StartTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): EndDate
        self._mapping['EndDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli (0..1): EndTime
        self._mapping['EndTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): DurationMeasure
        self._mapping['DurationMeasure'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        self._mapping['unitCode'] = ('cbc', '', 'Zorunlu (1)', True, False, False)
        # Seçimli(0..1): Description
        self._mapping['Description'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)

    def read_xml_file(self):
        pass

    def read_element_by_action(self, event: str, element: ET.Element):
        "invoiceperiod_startdate"
        "invoiceperiod_starttime"
        "invoiceperiod_durationmeasure"
        "invoiceperiod_enddate"
        "invoiceperiod_endtime"
        "invoiceperiod_durationmeasure_unitcode"
        "invoiceperiod_description"
