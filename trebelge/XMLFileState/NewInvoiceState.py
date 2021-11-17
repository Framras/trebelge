# from __future__ import annotations
import xml.etree.ElementTree as ET

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class NewInvoiceState(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        pass

    def read_element_by_action(self, event: str, element: ET.Element):
        pass
