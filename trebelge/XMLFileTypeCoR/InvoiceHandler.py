import xml.etree.ElementTree as ET
import frappe

from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler
from trebelge.XMLFileTypeCoR.DespatchAdviceHandler import DespatchAdviceHandler
from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeState.InvoiceState import InvoiceState


class InvoiceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    successor: AbstractXMLFileTypeHandler = DespatchAdviceHandler()
    invoiceNamespace: str = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                       'invoice_namespace_specification')

    def handle_xml_file_type(self, file_path: str, xml_file_type_context: XMLFileTypeContext):
        if ET.parse(file_path).getroot().tag == self.invoiceNamespace + 'Invoice':
            xml_file_type_context.set_state = InvoiceState()

        else:
            self.successor.handle_xml_file_type(file_path, xml_file_type_context)
