from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote


class TRUBLMaritimeTransport(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR MaritimeTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['VesselID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['VesselName'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RadioCallSignID'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['VesselID', 'VesselName', 'RadioCallSignID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['GrossTonnageMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        grosstonnagemeasure_: Element = element.find('./' + cbcnamespace + 'GrossTonnageMeasure')
        if grosstonnagemeasure_:
            frappedoc['grosstonnagemeasure'] = grosstonnagemeasure_.text
            frappedoc['grosstonnagemeasureunitcode'] = grosstonnagemeasure_.attrib.get('unitCode')
        # ['NetTonnageMeasure'] = ('cbc', '', 'Seçimli (0...1)')
        nettonnagemeasure_: Element = element.find('./' + cbcnamespace + 'NetTonnageMeasure')
        if nettonnagemeasure_:
            frappedoc['nettonnagemeasure'] = nettonnagemeasure_.text
            frappedoc['nettonnagemeasureunitcode'] = nettonnagemeasure_.attrib.get('unitCode')
        # ['ShipsRequirements'] = ('cbc', '', 'Seçimli (0...n)')
        shipsrequirements_: list = element.findall('./' + cbcnamespace + 'ShipsRequirements')
        if len(shipsrequirements_) != 0:
            requirements: list = []
            for shipsrequirement_ in shipsrequirements_:
                requirements.append(TRUBLNote.process_element(shipsrequirement_,
                                                              cbcnamespace,
                                                              cacnamespace))
            frappedoc['shipsrequirements'] = requirements
        # ['RegistryCertificateDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...1)')
        # ['RegistryPortLocation'] = ('cac', 'Location', 'Seçimli (0...1)')
        cacsecimli01: list = \
            [{'Tag': 'RegistryCertificateDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'registrycertificatedocumentreference'},
             {'Tag': 'RegistryPortLocation', 'strategy': TRUBLLocation(), 'fieldName': 'registryportlocation'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_:
                frappedoc[element_.get('fieldName')] = element_.get('strategy').process_element(tagelement_,
                                                                                                cbcnamespace,
                                                                                                cacnamespace).name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
