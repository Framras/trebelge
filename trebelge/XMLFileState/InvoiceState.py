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

    def find_ebelge_status(self):
        file_path: str = self.get_context().get_file_path()
        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "uuid": ET.parse(file_path).getroot().find(cbc_namespace + uuid).text}):
            self.get_context().set_state(NewInvoiceState())
