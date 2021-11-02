import xml.etree.ElementTree as ET
import frappe

from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileTypeHandler
from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeState.DespatchAdviceState import DespatchAdviceState


class DespatchAdviceHandler(AbstractXMLFileTypeHandler):
    """
    This Handler has no successor.
    CoR Handler method for checking if the FileType is DespatchAdvice.
    """
    despatchAdviceNamespace: str = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                              'despatch_advice_namespace_specification')

    def handle_xml_file_type(self, file_path: str, xml_file_type_context: XMLFileTypeContext):
        if ET.parse(file_path).getroot().tag == self.despatchAdviceNamespace + 'DespatchAdvice':
            xml_file_type_context.set_state = DespatchAdviceState()
        else:
            # TODO: Raise 'File is of unknown type' warning and leave it be
            pass
