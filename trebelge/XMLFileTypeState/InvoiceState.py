# from __future__ import annotations
from abc import ABC, abstractmethod

from trebelge.XMLFileProcessStrategy.XMLFileProcessContext import XMLFileProcessContext
from trebelge.XMLFileProcessStrategy.XMLNamespaces import XMLNamespaces
from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeState.XMLFileTypeState import XMLFileTypeState

import xml.etree.ElementTree as ET
import frappe


class InvoiceState(XMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self, file_path: str) -> None:
        # read all namespaces
        context = XMLFileProcessContext(XMLNamespaces())
        namespaces = context.return_file_data(file_path)

        default_namespace: str = '{' + namespaces.get('') + '}'
        cbc_namespace: str = '{' + namespaces.get('cbc') + '}'
        cac_namespace: str = '{' + namespaces.get('cac') + '}'

        if not frappe.db.exists({"doctype": "TR GIB eFatura Gelen",
                                 "uuid": ET.parse(file_path).getroot().find(cbc_namespace + 'UUID').text}):

    def handle2(self) -> None:
        pass
