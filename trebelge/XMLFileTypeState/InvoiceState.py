# from __future__ import annotations
import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileProcessStrategy.CBCNamespace import CBCNamespace
from trebelge.XMLFileProcessStrategy.UUID import UUID
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategyContext import XMLFileProcessStrategyContext
from trebelge.XMLFileTypeState.AbstractXMLFileTypeState import AbstractXMLFileTypeState
from trebelge.XMLFileTypeState.NewInvoiceState import NewInvoiceState


class InvoiceState(AbstractXMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self):
        file_path: str = self.get_context().get_file_path()
        context = XMLFileProcessStrategyContext()
        context.set_file_path(file_path)
        context.set_strategy(CBCNamespace())
        cbc_namespace: str = context.return_file_data()
        context.set_strategy(UUID())
        uuid: str = context.return_file_data()

        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "uuid": ET.parse(file_path).getroot().find(cbc_namespace + uuid).text}):
            self.get_context().set_state(NewInvoiceState())

    def initiate_new_record(self) -> None:
        pass
