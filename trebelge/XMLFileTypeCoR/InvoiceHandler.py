from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler
import xml.etree.ElementTree as ET
import frappe


class InvoiceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler declares a method for building the chain of handlers.
    Handler method for checking if the FileType is Invoice.
    """

    def handleRequest(self, filepath):
        if ET.parse(filepath).getroot().tag == frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                                          'invoice_namespace_specification'
                                                                          ) + 'Invoice':
            pass
        else:
            self.successor.handleRequest(filepath)

    def setSuccessor(self, successor):
        pass

    def __init__(self):
        self.successor =
