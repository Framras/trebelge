import xml.etree.ElementTree as ET

import frappe
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.DespatchAdviceHandler import DespatchAdviceHandler
from trebelge.XMLFileState.InvoiceState import InvoiceState


class InvoiceHandler(AbstractXMLFileHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    _eBelgeSettingsDoctype: str = 'TR UBL Namespace Specifications'
    _eBelgeTag: str = 'Invoice'
    _successor: AbstractXMLFileHandler = DespatchAdviceHandler()

    def handle_xml_file(self, file_path: str):
        for namespace in frappe.get_all(
                self._eBelgeSettingsDoctype, filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                fields={"namespace_specification"}):
            if ET.parse(file_path).getroot().tag == namespace + self._eBelgeTag:
                return InvoiceState()
            else:
                self._successor.handle_xml_file(file_path)
