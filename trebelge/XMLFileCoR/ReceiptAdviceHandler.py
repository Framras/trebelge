import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileState.ReceiptAdviceState import ReceiptAdviceState


class ReceiptAdviceHandler(AbstractXMLFileHandler):
    """
    This Handler has no successor.
    CoR Handler method for checking if the FileType is DespatchAdvice.
    """
    _eBelgeSettingsDoctype: str = 'TR UBL Namespace Specifications'
    _eBelgeTag: str = 'ReceiptAdvice'
    _successor: AbstractXMLFileHandler = None

    def handle_xml_file(self, file_path: str):
        for namespace in frappe.get_all(
                self._eBelgeSettingsDoctype, filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                fields={"namespace_specification"}):
            if ET.parse(file_path).getroot().tag == namespace + self._eBelgeTag:
                return ReceiptAdviceState()
            else:
                # TODO: Raise 'File is of unknown type' warning and leave it be
                pass
