# from __future__ import annotations
import xml.etree.ElementTree as ET
from abc import ABC

import frappe
from trebelge.XMLFileTypeState.XMLFileTypeState import XMLFileTypeState


class NewInvoiceState(XMLFileTypeState, ABC):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self, file_path: str):
        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "uuid": ET.parse(filePath).getroot().find(cbc_namespace + 'UUID').text}):

    def handle2(self) -> None:
        pass
