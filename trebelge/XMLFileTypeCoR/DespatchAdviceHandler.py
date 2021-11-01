from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler
import xml.etree.ElementTree as ET
import frappe


class DespatchAdviceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler has no successor.
    CoR Handler method for checking if the FileType is DespatchAdvice.
    """
    despatchAdvice_namespace = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                          'despatch_advice_namespace_specification')

    def handleRequest(self, filepath):
        if ET.parse(filepath).getroot().tag == self.despatchAdvice_namespace + 'DespatchAdvice':
            # TODO: Implement DespatchAdvice processing
            pass
        else:
            # TODO: Raise 'File is of unknown type' warning and leave it be
            pass
