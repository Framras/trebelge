from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler
import xml.etree.ElementTree as ET
import frappe


class InvoiceHandler(AbstractXMLFileTypeHandler):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    def handleRequest(self, filepath):
        if ET.parse(filepath).getroot().tag == frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                                          'invoice_namespace_specification'
                                                                          ) + 'Invoice':

    def setSuccessor(self, successor):
        pass
