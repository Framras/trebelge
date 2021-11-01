import xml.etree.ElementTree as ET
import frappe
from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler
from trebelge.XMLFileTypeCoR.DespatchAdviceHandler import DespatchAdviceHandler


class InvoiceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    successor: AbstractXMLFileTypeHandler = DespatchAdviceHandler()
    invoiceNamespace = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                  'invoice_namespace_specification')

    def handle_request(self, file_path):
        if ET.parse(file_path).getroot().tag == self.invoiceNamespace + 'Invoice':
            pass
        else:
            self.successor.handle_request(file_path)
