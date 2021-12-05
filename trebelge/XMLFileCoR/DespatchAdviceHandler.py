import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.ReceiptAdviceHandler import ReceiptAdviceHandler
from trebelge.XMLFileState.DespatchAdviceState import DespatchAdviceState


class DespatchAdviceHandler(AbstractXMLFileHandler):
    """
    This Handler's successor:
    CoR Handler method for checking if the FileType is DespatchAdvice.
    """
    _eBelgeSettingsDoctype: str = 'UBL TR Namespace Specifications'
    _eBelgeTag: str = 'DespatchAdvice'
    _successor: AbstractXMLFileHandler = ReceiptAdviceHandler()

    def handle_xml_file(self, file_path: str):
        for namespace in frappe.get_all(
                self._eBelgeSettingsDoctype, filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                fields={"namespace_specification"}):
            if ET.parse(file_path).getroot().tag == namespace.get('namespace_specification') + self._eBelgeTag:
                return DespatchAdviceState()
            else:
                self._successor.handle_xml_file(file_path)
