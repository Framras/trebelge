# from __future__ import annotations
import xml.etree.ElementTree as ET
from abc import ABC

import frappe
from trebelge.XMLFileTypeState.AbstractXMLFileTypeState import AbstractXMLFileTypeState


class NewInvoiceState(AbstractXMLFileTypeState, ABC):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self):
        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "uuid": ET.parse(filePath).getroot().find(cbc_namespace + 'UUID').text}):

    def list_file_namespaces(self) -> None:
        pass
