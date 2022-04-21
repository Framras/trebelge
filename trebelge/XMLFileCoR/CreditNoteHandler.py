import xml.etree.ElementTree as ET

import frappe
from trebelge.TRUBLBuilder.TRUBLCreditNoteBuilder import TRUBLCreditNoteBuilder
from trebelge.TRUBLBuilder.TRUBLDirector import TRUBLDirector
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler


class CreditNoteHandler(AbstractXMLFileHandler):
    """
    This Handler has no successor.
    CoR Handler method for checking if the FileType is CreditNote.
    """
    _eBelgeSettingsDoctype: str = 'UBL TR Namespace Specifications'
    _eBelgeTag: str = 'CreditNote'
    _successor: AbstractXMLFileHandler = None

    def handle_xml_file(self, file_path: str):
        for namespace in frappe.get_all(self._eBelgeSettingsDoctype,
                                        filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                                        fields={"namespace_specification"}):
            if ET.parse(file_path).getroot().tag == namespace.get('namespace_specification') + self._eBelgeTag:
                builder = TRUBLCreditNoteBuilder(file_path)
                director = TRUBLDirector(builder)
                director.make_tr_ubl_creditnote()
                builder.get_document()
                frappe.db.commit()
            else:
                # TODO: Raise 'File is of unknown type' warning and leave it be
                pass
