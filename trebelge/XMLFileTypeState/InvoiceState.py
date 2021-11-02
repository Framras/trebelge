# from __future__ import annotations
import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategyContext import XMLFileProcessStrategyContext
from trebelge.XMLFileProcessStrategy.XMLNamespaces import XMLNamespaces
from trebelge.XMLFileTypeState.AbstractXMLFileTypeState import AbstractXMLFileTypeState


class InvoiceState(AbstractXMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self):
        file_path: str = self.get_context().get_file_path()
        # read all namespaces
        namespaces_strategy = XMLFileProcessStrategyContext(XMLNamespaces())
        namespaces = namespaces_strategy.return_file_data(file_path)
        # read cbc namespace
        cbc_namespace: str = '{' + namespaces.get('cbc') + '}'

        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "uuid": ET.parse(file_path).getroot().find(cbc_namespace + 'UUID').text}):
            pass

    def list_file_namespaces(self) -> None:
        pass
