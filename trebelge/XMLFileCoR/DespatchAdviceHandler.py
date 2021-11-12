import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileState.DespatchAdviceState import DespatchAdviceState


class DespatchAdviceHandler(AbstractXMLFileHandler):
    """
    This Handler has no successor.
    CoR Handler method for checking if the FileType is DespatchAdvice.
    """
    _successor: AbstractXMLFileHandler = None
    _eBelgeTag: str = 'DespatchAdvice'
    _eBelgeNamespace: str = frappe.db.get_single_value('TR GIB eBelge Switchboard',
                                                       'despatch_advice_namespace_specification')

    def handle_xml_file(self, file_path: str):
        if ET.parse(file_path).getroot().tag == self._eBelgeNamespace + self._eBelgeTag:
            return DespatchAdviceState()
        else:
            # TODO: Raise 'File is of unknown type' warning and leave it be
            pass
