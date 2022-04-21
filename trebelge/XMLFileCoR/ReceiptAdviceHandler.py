import xml.etree.ElementTree as ET

import frappe
from trebelge.TRUBLBuilder.TRUBLDirector import TRUBLDirector
from trebelge.TRUBLBuilder.TRUBLReceiptAdviceBuilder import TRUBLReceiptAdviceBuilder
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.CreditNoteHandler import CreditNoteHandler


class ReceiptAdviceHandler(AbstractXMLFileHandler):
    """
    This Handler's successor is for CreditNote FileType.
    CoR Handler method for checking if the FileType is ReceiptAdvice.
    """
    _eBelgeSettingsDoctype: str = 'UBL TR Namespace Specifications'
    _eBelgeTag: str = 'ReceiptAdvice'
    _successor: AbstractXMLFileHandler = CreditNoteHandler()

    def handle_xml_file(self, file_path: str):
        for namespace in frappe.get_all(self._eBelgeSettingsDoctype,
                                        filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                                        fields={"namespace_specification"}):
            if ET.parse(file_path).getroot().tag == namespace.get('namespace_specification') + self._eBelgeTag:
                builder = TRUBLReceiptAdviceBuilder(file_path)
                director = TRUBLDirector(builder)
                director.make_tr_ubl_receiptadvice()
                builder.get_document()
                frappe.db.commit()
            else:
                self._successor.handle_xml_file(file_path)
