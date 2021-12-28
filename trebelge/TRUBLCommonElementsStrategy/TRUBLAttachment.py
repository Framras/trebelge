from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLExternalReference import TRUBLExternalReference


class TRUBLAttachment(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Attachment'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ExternalReference'] = ('cac', 'ExternalReference()', 'Seçimli (0..1)', 'externalreference')
        externalreference_: Element = element.find('./' + cacnamespace + 'ExternalReference')
        if externalreference_ is not None:
            frappedoc['externalreference'] = [TRUBLExternalReference.process_element(externalreference_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)]
        # TODO implement Base64 decoder
        # ['EmbeddedDocumentBinaryObject'] = ('cbc', 'embeddeddocumentbinaryobject', 'Seçimli (0..1)')
        # characterSetCode: 'UTF-8'
        # filename: 'TN22021000283169.xslt'
        # encodingCode: 'Base64'
        # mimeCode: 'application/xml'
        embeddeddocumentbinaryobject_: Element = element.find('./' + cacnamespace + 'EmbeddedDocumentBinaryObject')
        if embeddeddocumentbinaryobject_ is not None:
            pass

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
