from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote


class TRUBLDimension(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Dimension'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['AttributeID'] = ('cbc', 'attributeid', 'Zorunlu(1)')
        frappedoc: dict = {'attributeid': element.find('./' + cbcnamespace + 'AttributeID').text}
        # ['Measure'] = ('cbc', 'measure', 'Seçimli (0...1)')
        measure_: Element = element.find('./' + cbcnamespace + 'Measure')
        if measure_ is not None:
            frappedoc['measure'] = measure_.text
            frappedoc['measureunitcode'] = measure_.attrib.get('unitCode')
        # ['Description'] = ('cbc', 'descriptions', 'Seçimli(0..n)', 'description')
        descriptions_: list = element.findall('./' + cbcnamespace + 'Description')
        if descriptions_ is not None:
            descriptions: list = []
            for description_ in descriptions_:
                descriptions.append(TRUBLNote.process_element(description_,
                                                              cbcnamespace,
                                                              cacnamespace))
            frappedoc['description'] = descriptions
        # ['MinimumMeasure'] = ('cbc', 'minimummeasure', 'Seçimli(0..1)')
        minimummeasure_: Element = element.find('./' + cbcnamespace + 'MinimumMeasure')
        if minimummeasure_ is not None:
            frappedoc['minimummeasure'] = minimummeasure_.text
            frappedoc['minimummeasureunitcode'] = minimummeasure_.attrib.get('unitCode')
        # ['MaximumMeasure'] = ('cbc', 'maximummeasure', 'Seçimli(0..1)')
        maximummeasure_: Element = element.find('./' + cbcnamespace + 'MaximumMeasure')
        if maximummeasure_ is not None:
            frappedoc['maximummeasure'] = maximummeasure_.text
            frappedoc['maximummeasureunitcode'] = maximummeasure_.attrib.get('unitCode')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
