from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLExternalReference import TRUBLExternalReference


class TRUBLAttachment(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ExternalReference'] = ('cac', 'ExternalReference()', 'Seçimli (0..1)', 'externalreference')
        ['EmbeddedDocumentBinaryObject'] = ('cbc', 'embeddeddocumentbinaryobject', 'Seçimli (0..1)')
        characterSetCode: 'UTF-8'
        filename: 'TN22021000283169.xslt'
        encodingCode: 'Base64'
        mimeCode: 'application/xml'
        """
        attachment: dict = {}
        externalreference_ = element.find(cacnamespace + 'ExternalReference')
        if externalreference_ is not None:
            strategy: TRUBLCommonElement = TRUBLExternalReference()
            self._strategyContext.set_strategy(strategy)
            externalreference = self._strategyContext.return_element_data(externalreference_, cbcnamespace,
                                                                          cacnamespace)
            for key in externalreference.keys():
                attachment['externalreference_' + key] = externalreference.get(key)
        # TODO implement Base64 decoder
        embeddeddocumentbinaryobject_ = element.find(cacnamespace + 'EmbeddedDocumentBinaryObject')
        if embeddeddocumentbinaryobject_ is not None:
            for key in embeddeddocumentbinaryobject_.attrib.keys():
                attachment[('EmbeddedDocumentBinaryObject_' + key).lower()] = embeddeddocumentbinaryobject_.attrib.get(
                    key)

        return attachment
