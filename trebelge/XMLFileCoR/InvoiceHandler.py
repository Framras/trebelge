import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.DespatchAdviceHandler import DespatchAdviceHandler
from trebelge.XMLFileState.InvoiceState import InvoiceState
from trebelge.XMLFileState.XMLFileStateContext import XMLFileTypeStateContext


class InvoiceHandler(AbstractXMLFileHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    _successor: AbstractXMLFileHandler = DespatchAdviceHandler()
    _invoiceNamespace: str = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                        'invoice_namespace_specification')

    def handle_xml_file(self, xml_file_type_context: XMLFileTypeStateContext):
        file_path = xml_file_type_context.get_file_path()
        if ET.parse(file_path).getroot().tag == self._invoiceNamespace + 'Invoice':
            xml_file_type_context.set_state = InvoiceState()
        else:
            self._successor.handle_xml_file(xml_file_type_context)
