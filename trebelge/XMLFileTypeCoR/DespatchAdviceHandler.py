import xml.etree.ElementTree as ET
import frappe
from trebelge.XMLFileTypeCoR.AbstractXMLFileTypeHandler import AbstractXMLFileTypeHandler


class DespatchAdviceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler has no successor.
    CoR Handler method for checking if the FileType is DespatchAdvice.
    """
    despatchAdviceNamespace: str = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                              'despatch_advice_namespace_specification')

    def handle_request(self, file_path):
        if ET.parse(file_path).getroot().tag == self.despatchAdviceNamespace + 'DespatchAdvice':
            # TODO: Implement DespatchAdvice processing
            pass
        else:
            # TODO: Raise 'File is of unknown type' warning and leave it be
            pass
