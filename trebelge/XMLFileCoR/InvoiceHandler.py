import xml.etree.ElementTree as ET
import frappe

from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.DespatchAdviceHandler import DespatchAdviceHandler
from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeState.InvoiceState import InvoiceState


class InvoiceHandler(AbstractXMLFileHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    successor: AbstractXMLFileHandler = DespatchAdviceHandler()
    invoiceNamespace: str = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                       'invoice_namespace_specification')

    def handle_xml_file(self, file_path: str, xml_file_type_context: XMLFileTypeContext):
        if ET.parse(file_path).getroot().tag == self.invoiceNamespace + 'Invoice':
            xml_file_type_context.set_state = InvoiceState()

        else:
            self.successor.handle_xml_file(file_path, xml_file_type_context)
