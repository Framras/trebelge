# from __future__ import annotations
import xml.etree.ElementTree as ET

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class NewInvoiceState(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR UBL Received Invoice'
    _mapping = dict()

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        pass

    def read_element_by_action(self, event: str, element: ET.Element):
        pass

    def read_xml_file(self):
        for event, elem in ET.iterparse(self.get_context().get_file_path(), events=("start", "end")):
            self.get_context().read_element_by_action(event, elem)
