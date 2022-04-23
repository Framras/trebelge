from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLTemperature(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Temperature'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['AttributeID'] = ('cbc', '', 'Zorunlu (1)')
        # ['Measure'] = ('cbc', '', 'Zorunlu (1)')
        attributeid_: Element = element.find('./' + cbcnamespace + 'AttributeID')
        measure_: Element = element.find('./' + cbcnamespace + 'Measure')
        if attributeid_ is None or attributeid_.text is None \
                or measure_ is None or measure_.text is None:
            return None
        frappedoc: dict = dict(attributeid=attributeid_.text,
                               measure=measure_.text,
                               measureunitcode=measure_.attrib.get('unitCode')
                               )
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['Description'] = ('cbc', '', 'Seçimli (0...n)')
        descriptions_: list = element.findall('./' + cbcnamespace + 'Description')
        if len(descriptions_) != 0:
            for description_ in descriptions_:
                element_ = description_.text
                if element_ is not None and element_.strip() != '':
                    document.append("description", dict(note=element_.strip()))
                    document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
