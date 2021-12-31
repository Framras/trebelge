import xml.etree.ElementTree as ET

import frappe
from trebelge.TRUBLBuilder.TRUBLDespatchAdviceBuilder import TRUBLDespatchAdviceBuilder
from trebelge.TRUBLBuilder.TRUBLDirector import TRUBLDirector
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.ReceiptAdviceHandler import ReceiptAdviceHandler


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
                builder = TRUBLDespatchAdviceBuilder(file_path)
                director = TRUBLDirector(builder)
                director.make_tr_ubl_despatchadvice()
                builder.get_document()
            else:
                self._successor.handle_xml_file(file_path)
