# from __future__ import annotations
import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState
from trebelge.XMLFileState.NewInvoiceState import NewInvoiceState


class InvoiceState(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR UBL Received Invoice'
    _mapping = dict()

    def find_ebelge_status(self):
        if not frappe.db.exists({"doctype": self._frappeDoctype,
                                 "uuid": self.get_context().get_uuid()}):
            self.define_mappings()
            self.get_context().set_state(NewInvoiceState())

    def define_mappings(self):
        pass

    def read_element_by_action(self, event: str, element: ET.Element):
        pass
