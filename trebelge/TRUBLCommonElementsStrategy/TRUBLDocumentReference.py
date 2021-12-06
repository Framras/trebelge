from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLDocumentReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Document Reference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:

        # ['ID'] = ('cbc', '', 'Zorunlu (1)', 'id')
        # ['IssueDate'] = ('cbc', '', 'Zorunlu (1)', 'issuedate')
        documentreference: dict = {'id': element.find(cbcnamespace + 'ID').text,
                                   'issuedate': element.find(cbcnamespace + 'IssueDate').text}
        # ['DocumentTypeCode'] = ('cbc', '', 'Seçimli (0...1)', 'documenttypecode')
        # ['DocumentType'] = ('cbc', '', 'Seçimli (0...1)', 'documenttype')
        channel_ = element.find(cbcnamespace + 'Channel')
        if channel_ is not None:
            communication['channel'] = channel_.text

        # ['Attachment'] = ('cac', 'Attachment', 'Seçimli (0...1)', 'attachment')
        # ['ValidityPeriod'] = ('cac', 'Period', 'Seçimli (0...1)', 'validityperiod')
        # ['IssuerParty'] = ('cac', 'Party', 'Seçimli (0...1)', 'issuerparty')

        # ['DocumentDescription'] = ('cbc', '', 'Seçimli(0..n)', 'documentdescription')

        if not frappe.get_all(self._frappeDoctype, filters=communication):
            pass
        else:
            newcommunication = communication
            newcommunication['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newcommunication)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=communication)
