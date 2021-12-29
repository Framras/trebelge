from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAttachment import TRUBLAttachment
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLDocumentReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DocumentReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
        # ['ID'] = ('cbc', '', 'Zorunlu (1)', 'id')
        # ['IssueDate'] = ('cbc', '', 'Zorunlu (1)', 'issuedate')
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text,
                           'issuedate': element.find('./' + cbcnamespace + 'IssueDate').text}
        # ['DocumentTypeCode'] = ('cbc', '', 'Seçimli (0...1)', 'documenttypecode')
        # ['DocumentType'] = ('cbc', '', 'Seçimli (0...1)', 'documenttype')
        cbcsecimli01: list = ['DocumentTypeCode', 'DocumentType']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['Attachment'] = ('cac', 'Attachment', 'Seçimli (0...1)', 'attachment')
        # ['ValidityPeriod'] = ('cac', 'Period', 'Seçimli (0...1)', 'validityperiod')
        # ['IssuerParty'] = ('cac', 'Party', 'Seçimli (0...1)', 'issuerparty')
        attachment_ = element.find('./' + cacnamespace + 'Attachment')
        if attachment_:
            frappedoc['attachment'] = [TRUBLAttachment.process_element(attachment_,
                                                                       cbcnamespace,
                                                                       cacnamespace)]
        validityperiod_ = element.find('./' + cacnamespace + 'ValidityPeriod')
        if validityperiod_:
            frappedoc['validityperiod'] = [TRUBLPeriod.process_element(validityperiod_,
                                                                       cbcnamespace,
                                                                       cacnamespace)]
        issuerparty_ = element.find('./' + cacnamespace + 'IssuerParty')
        if issuerparty_:
            frappedoc['issuerparty'] = [TRUBLParty.process_element(issuerparty_,
                                                                   cbcnamespace,
                                                                   cacnamespace)]
        # ['DocumentDescription'] = ('cbc', '', 'Seçimli(0..n)', 'documentdescription')
        documentdescriptions_: list = element.findall('./' + cbcnamespace + 'DocumentDescription')
        if len(documentdescriptions_) != 0:
            documentdescriptions: list = []
            for documentdescription_ in documentdescriptions_:
                documentdescriptions.append(TRUBLNote.process_element(documentdescription_,
                                                                      cbcnamespace,
                                                                      cacnamespace))
            frappedoc['documentdescription'] = documentdescriptions

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
