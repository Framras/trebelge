from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAttachment import TRUBLAttachment
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLDocumentReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DocumentReference'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
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
            strategy: TRUBLCommonElement = TRUBLAttachment()
            self._strategyContext.set_strategy(strategy)
            frappedoc['attachment'] = [self._strategyContext.return_element_data(attachment_,
                                                                                 cbcnamespace,
                                                                                 cacnamespace)]
        validityperiod_ = element.find('./' + cacnamespace + 'ValidityPeriod')
        if validityperiod_:
            strategy: TRUBLCommonElement = TRUBLPeriod()
            self._strategyContext.set_strategy(strategy)
            frappedoc['validityperiod'] = [self._strategyContext.return_element_data(validityperiod_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)]
        issuerparty_ = element.find('./' + cacnamespace + 'IssuerParty')
        if issuerparty_:
            strategy: TRUBLCommonElement = TRUBLParty()
            self._strategyContext.set_strategy(strategy)
            frappedoc['issuerparty'] = [self._strategyContext.return_element_data(issuerparty_,
                                                                                  cbcnamespace,
                                                                                  cacnamespace)]
        # ['DocumentDescription'] = ('cbc', '', 'Seçimli(0..n)', 'documentdescription')
        documentdescriptions_: list = element.findall('./' + cbcnamespace + 'DocumentDescription')
        if documentdescriptions_:
            documentdescriptions: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for documentdescription_ in documentdescriptions_:
                documentdescriptions.append(self._strategyContext.return_element_data(documentdescription_,
                                                                                      cbcnamespace,
                                                                                      cacnamespace))
            frappedoc['documentdescription'] = documentdescriptions

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
