from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler
import xml.etree.ElementTree as ET
import frappe
from trebelge.XMLFileTypeCoR.DespatchAdviceHandler import DespatchAdviceHandler


class InvoiceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    successor: AbstractXMLFileTypeHandler = DespatchAdviceHandler()
    invoice_namespace = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                   'invoice_namespace_specification')

    def handleRequest(self, file_path):
        if ET.parse(file_path).getroot().tag == self.invoice_namespace + 'Invoice':
            pass
        else:
            self.successor.handleRequest(file_path)
