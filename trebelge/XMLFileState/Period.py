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
    _elementTag: str = 'Period'
    _invoiceElementTag: str = 'InvoicePeriod'

    def find_ebelge_status(self):
        pass

    def define_mappings(self, tag: str, initiator: AbstractXMLFileState):
        if tag == self._invoiceElementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Seçimli (0..1): StartDate
            self._mapping['StartDate'] = ('cbc', 'invoiceperiod_startdate', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli (0..1): StartTime
            self._mapping['StartTime'] = ('cbc', 'invoiceperiod_starttime', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1): EndDate
            self._mapping['EndDate'] = ('cbc', 'invoiceperiod_enddate', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli (0..1): EndTime
            self._mapping['EndTime'] = ('cbc', 'invoiceperiod_endtime', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1): DurationMeasure
            self._mapping['DurationMeasure'] = (
                'cbc', 'invoiceperiod_durationmeasure', 'Seçimli (0...1)', True, True, True, '')
            self._mapping['unitCode'] = (
                'cbc', 'invoiceperiod_durationmeasure_unitcode', 'Zorunlu (1)', True, False, False, '')
            # Seçimli(0..1): Description
            self._mapping['Description'] = (
                'cbc', 'invoiceperiod_description', 'Seçimli (0...1)', False, False, True, '')
            self._mapping[self._invoiceElementTag] = ('cac', initiator, '', False, False, True, '')
        elif tag == self._elementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Seçimli (0..1): StartDate
            self._mapping['StartDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli (0..1): StartTime
            self._mapping['StartTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1): EndDate
            self._mapping['EndDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli (0..1): EndTime
            self._mapping['EndTime'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1): DurationMeasure
            self._mapping['DurationMeasure'] = (
                'cbc', '', 'Seçimli (0...1)', True, True, True, '')
            self._mapping['unitCode'] = (
                'cbc', '', 'Zorunlu (1)', True, False, False, '')
            # Seçimli(0..1): Description
            self._mapping['Description'] = (
                'cbc', '', 'Seçimli (0...1)', False, False, True, '')
            self._mapping[self._elementTag] = ('cac', initiator, '', False, False, True, '')

    def read_element_by_action(self, event: str, element: ET.Element):
        tag: str = ''
        if element.tag.startswith(self.get_context().get_cac_namespace()):
            tag = element.tag[len(self.get_context().get_cac_namespace()):]
        elif element.tag.startswith(self.get_context().get_cbc_namespace()):
            tag = element.tag[len(self.get_context().get_cbc_namespace()):]
        if self._mapping[tag] is not None:
            if event == 'start' and self._mapping[tag][3]:
                if element.tag.startswith(self.get_context().get_cbc_namespace()):
                    if self._mapping[tag][4]:
                        for key in element.attrib.keys():
                            if self._mapping[key] is not None:
                                self.get_context().set_new_frappe_doc(
                                    self._mapping[key][1], element.attrib.get(key))
                    else:
                        pass
                elif element.tag.startswith(self.get_context().get_cac_namespace()):
                    if self._mapping[tag][2] in ['Zorunlu (1)', 'Seçimli (0..1)']:
                        self.get_context().set_state = self._mapping[tag][1]
                        self.get_context().define_mappings(tag, self)
                        self.get_context().read_element_by_action(event, element)
                    elif self._mapping[tag][2] in ['Seçimli (0...n)']:
                        pass
            elif event == 'end' and self._mapping[tag][5]:
                if element.tag.startswith(self.get_context().get_cbc_namespace()):
                    if self._mapping[tag][2] in ['Zorunlu (1)', 'Seçimli (0..1)']:
                        self.get_context().set_new_frappe_doc(
                            self._mapping[tag][1], element.text)
                    elif self._mapping[tag][2] in ['Seçimli (0...n)']:
                        if self.get_context().get_new_frappe_doc(self)[self._mapping[tag][1]] is None:
                            self.get_context().set_new_frappe_doc(
                                self._mapping[tag][1], {self._mapping[tag][6]: element.text})
                        else:
                            self.get_context().append_new_frappe_doc_field(
                                self._mapping[tag][1], {self._mapping[tag][6]: element.text})
                elif element.tag.startswith(self.get_context().get_cac_namespace()):
                    self.get_context().set_state = self._mapping[tag][1]
