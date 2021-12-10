from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLAttachment import TRUBLAttachment
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLDocumentReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Document Reference'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:

        # ['ID'] = ('cbc', '', 'Zorunlu (1)', 'id')
        # ['IssueDate'] = ('cbc', '', 'Zorunlu (1)', 'issuedate')
        documentreference: dict = {'id': element.find(cbcnamespace + 'ID').text,
                                   'issuedate': element.find(cbcnamespace + 'IssueDate').text}

        # ['DocumentTypeCode'] = ('cbc', '', 'Seçimli (0...1)', 'documenttypecode')
        # ['DocumentType'] = ('cbc', '', 'Seçimli (0...1)', 'documenttype')
        cbcsecimli01: list = ['DocumentTypeCode', 'DocumentType']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                documentreference[field_.tag.lower()] = field_.text

        # ['Attachment'] = ('cac', 'Attachment', 'Seçimli (0...1)', 'attachment')
        # ['ValidityPeriod'] = ('cac', 'Period', 'Seçimli (0...1)', 'validityperiod')
        # ['IssuerParty'] = ('cac', 'Party', 'Seçimli (0...1)', 'issuerparty')
        cacsecimli01: list = \
            [{'Tag': 'Attachment', 'strategy': TRUBLAttachment(), 'docType': 'UBL TR Attachment',
              'fieldName': 'attachment'},
             {'Tag': 'ValidityPeriod', 'strategy': TRUBLPeriod(), 'docType': 'UBL TR Period',
              'fieldName': 'validityperiod'},
             {'Tag': 'IssuerParty', 'strategy': TRUBLParty(), 'docType': 'UBL TR Party', 'fieldName': 'issuerparty'}
             ]
        for element_ in cacsecimli01:
            tagelement_ = element.find(cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                documentreference[element_.get('fieldName')] = [frappe.get_doc(
                    element_.get('docType'),
                    self._strategyContext.return_element_data(tagelement_, cbcnamespace,
                                                              cacnamespace)[0]['name'])]

        # ['DocumentDescription'] = ('cbc', '', 'Seçimli(0..n)', 'documentdescription')
        documentdescription_ = element.find(cacnamespace + 'PartyLegalEntity')
        if documentdescription_ is not None:
            strategy: TRUBLCommonElement = TRUBLPartyLegalEntity()
            self._strategyContext.set_strategy(strategy)
            partylegalentities: list = []
            for partylegalentity in documentdescription_:
                partylegalentities.append(
                    frappe.get_doc(
                        'UBL TR PartyLegalEntity',
                        self._strategyContext.return_element_data(partylegalentity,
                                                                  cbcnamespace,
                                                                  cacnamespace)[0]['name']))
            documentreference['documentdescription'] = partylegalentities

        if not frappe.get_all(self._frappeDoctype, filters=documentreference):
            pass
        else:
            newdocumentreference = documentreference
            newdocumentreference['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newdocumentreference)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=documentreference)
