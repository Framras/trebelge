import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLBuilder.TRUBLDirector import TRUBLDirector
from trebelge.TRUBLBuilder.TRUBLInvoiceBuilder import TRUBLInvoiceBuilder
from trebelge.XMLFileCoR.AbstractXMLFileHandler import AbstractXMLFileHandler
from trebelge.XMLFileCoR.DespatchAdviceHandler import DespatchAdviceHandler


class InvoiceHandler(AbstractXMLFileHandler):
    """
    This Handler's successor is for DespatchAdvice FileType.
    CoR Handler method for checking if the FileType is Invoice.
    """
    _eBelgeSettingsDoctype: str = 'UBL TR Namespace Specifications'
    _eBelgeTag: str = 'Invoice'
    _frappeDoctype: str = 'UBL TR Invoice'
    _successor: AbstractXMLFileHandler = DespatchAdviceHandler()

    def handle_xml_file(self, file_path: str):
        root_: Element = ET.parse(file_path).getroot()
        for namespace in frappe.get_all(self._eBelgeSettingsDoctype,
                                        filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                                        fields={"namespace_specification"}):
            if root_.tag == namespace.get('namespace_specification') + self._eBelgeTag:
                _namespaces = dict([node for _, node in ET.iterparse(file_path, events=['start-ns'])])
                _cbc_ns = str('{' + _namespaces.get('cbc') + '}')
                uuid_ = root_.find('./' + _cbc_ns + 'UUID').text
                if len(frappe.get_all(self._frappeDoctype, filters={'uuid': uuid_})) == 0:
                    _cac_ns = str('{' + _namespaces.get('cac') + '}')
                    builder = TRUBLInvoiceBuilder(root_, _cac_ns, _cbc_ns, uuid_)
                    director = TRUBLDirector(builder)
                    director.make_tr_ubl_invoice()
                    builder.get_document()
                    frappe.db.commit()
            else:
                self._successor.handle_xml_file(file_path)
