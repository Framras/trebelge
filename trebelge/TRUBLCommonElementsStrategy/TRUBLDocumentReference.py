from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAttachment import TRUBLAttachment
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod


class TRUBLDocumentReference(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DocumentReference'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Zorunlu (1)', 'id')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None:
            if id_.text is not None:
                frappedoc['id'] = id_.text.strip()
        # ['IssueDate'] = ('cbc', '', 'Zorunlu (1)', 'issuedate')
        issuedate_ = element.find('./' + cbcnamespace + 'IssueDate')
        # if id_.attrib.keys() is not None:
        #     return None
        if issuedate_ is not None:
            if issuedate_.text is not None:
                frappedoc['issuedate'] = issuedate_.text.strip()
        # ['DocumentTypeCode'] = ('cbc', '', 'Seçimli (0...1)', 'documenttypecode')
        # ['DocumentType'] = ('cbc', '', 'Seçimli (0...1)', 'documenttype')
        cbcsecimli01: list = ['DocumentTypeCode', 'DocumentType']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['Attachment'] = ('cac', 'Attachment', 'Seçimli (0...1)', 'attachment')
        attachment_ = element.find('./' + cacnamespace + 'Attachment')
        if attachment_ is not None:
            tmp = TRUBLAttachment().process_element(attachment_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['attachment'] = tmp.name
        # ['ValidityPeriod'] = ('cac', 'Period', 'Seçimli (0...1)', 'validityperiod')
        validityperiod_ = element.find('./' + cacnamespace + 'ValidityPeriod')
        if validityperiod_ is not None:
            tmp = TRUBLPeriod().process_elementasdict(validityperiod_, cbcnamespace, cacnamespace)
            if tmp != {}:
                for key in ['startdate', 'starttime', 'enddate', 'endtime', 'durationmeasure',
                            'durationmeasure_unitcode', 'description']:
                    try:
                        frappedoc[key] = tmp[key]
                    except KeyError:
                        pass
        # ['IssuerParty'] = ('cac', 'Party', 'Seçimli (0...1)', 'issuerparty')
        issuerparty_ = element.find('./' + cacnamespace + 'IssuerParty')
        if issuerparty_ is not None:
            tmp = TRUBLParty().process_element(issuerparty_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['issuerparty'] = tmp.name
        if frappedoc == {}:
            return None
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['DocumentDescription'] = ('cbc', '', 'Seçimli(0..n)', 'documentdescription')
        documentdescriptions_: list = element.findall('./' + cbcnamespace + 'DocumentDescription')
        if len(documentdescriptions_) != 0:
            for documentdescription_ in documentdescriptions_:
                element_ = documentdescription_.text
                if element_ is not None and element_.strip() != '':
                    document.append("documentdescription", dict(note=element_.strip()))
                    document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
