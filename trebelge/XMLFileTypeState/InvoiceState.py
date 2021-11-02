from __future__ import annotations
from abc import ABC, abstractmethod

import frappe
from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeState.XMLFileTypeState import XMLFileTypeState


class InvoiceState(XMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def check_record_status(self) -> None:
        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "uuid": ET.parse(filePath).getroot().find(cbc_namespace + 'UUID').text}):

    def handle2(self) -> None:
        pass
