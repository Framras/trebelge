from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler
import xml.etree.ElementTree as ET
import frappe


class DespatchAdviceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler declares a method for building the chain of handlers.
    Handler method for checking if the FileType is Invoice.
    """

    def handleRequest(self, filepath):
        if ET.parse(filepath).getroot().tag == frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                                          'despatch_advice_namespace_specification'
                                                                          ) + 'DespatchAdvice':
            pass
        else:
            pass

    def setSuccessor(self, successor):
        pass
