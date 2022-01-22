import xml.etree.ElementTree as ET

import frappe
from trebelge.TRUBLBuilder.TRUBLDirector import TRUBLDirector
from trebelge.TRUBLBuilder.TRUBLReceiptAdviceBuilder import TRUBLReceiptAdviceBuilder
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler


class ReceiptAdviceHandler(AbstractXMLFileHandler):
    """
    This Handler has no successor.
    CoR Handler method for checking if the FileType is DespatchAdvice.
    """
    _eBelgeSettingsDoctype: str = 'UBL TR Namespace Specifications'
    _eBelgeTag: str = 'ReceiptAdvice'
    _successor: AbstractXMLFileHandler = None

    def handle_xml_file(self, file_path: str):
        for namespace in frappe.get_all(self._eBelgeSettingsDoctype,
                                        filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                                        fields={"namespace_specification"}):
            if ET.parse(file_path).getroot().tag == namespace.get('namespace_specification') + self._eBelgeTag:
                frappe.log_error('processing file' + file_path, 'File')
                builder = TRUBLReceiptAdviceBuilder(file_path)
                director = TRUBLDirector(builder)
                director.make_tr_ubl_receiptadvice()
                builder.get_document()
            else:
                # TODO: Raise 'File is of unknown type' warning and leave it be
                pass
