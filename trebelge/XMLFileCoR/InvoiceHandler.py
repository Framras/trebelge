import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.DespatchAdviceHandler import DespatchAdviceHandler
from trebelge.XMLFileState.InvoiceState import InvoiceState


class InvoiceHandler(AbstractXMLFileHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    _successor: AbstractXMLFileHandler = DespatchAdviceHandler()
    _eBelgeTag: str = 'Invoice'
    _eBelgeNamespace: str = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                       'invoice_namespace_specification')

    def handle_xml_file(self, file_path: str):
        if ET.parse(file_path).getroot().tag == self._eBelgeNamespace + self._eBelgeTag:
            return InvoiceState()
        else:
            self._successor.handle_xml_file(file_path)
