from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote


class TRUBLDimension(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Dimension'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        attributeid_ = element.find('./' + cbcnamespace + 'AttributeID')
        # ['AttributeID'] = ('cbc', 'attributeid', 'Zorunlu(1)')
        if attributeid_.text is not None:
            frappedoc: dict = {'attributeid': attributeid_.text}
        else:
            return None
        # ['Measure'] = ('cbc', 'measure', 'Seçimli (0...1)')
        measure_: Element = element.find('./' + cbcnamespace + 'Measure')
        if measure_ is not None:
            if measure_.text is not None:
                frappedoc['measure'] = measure_.text
                frappedoc['measureunitcode'] = measure_.attrib.get('unitCode')
        # ['MinimumMeasure'] = ('cbc', 'minimummeasure', 'Seçimli(0..1)')
        minimummeasure_: Element = element.find('./' + cbcnamespace + 'MinimumMeasure')
        if minimummeasure_ is not None:
            if minimummeasure_.text is not None:
                frappedoc['minimummeasure'] = minimummeasure_.text
                frappedoc['minimummeasureunitcode'] = minimummeasure_.attrib.get('unitCode')
        # ['MaximumMeasure'] = ('cbc', 'maximummeasure', 'Seçimli(0..1)')
        maximummeasure_: Element = element.find('./' + cbcnamespace + 'MaximumMeasure')
        if maximummeasure_ is not None:
            if maximummeasure_.text is not None:
                frappedoc['maximummeasure'] = maximummeasure_.text
                frappedoc['maximummeasureunitcode'] = maximummeasure_.attrib.get('unitCode')
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['Description'] = ('cbc', 'descriptions', 'Seçimli(0..n)', 'description')
        descriptions_: list = element.findall('./' + cbcnamespace + 'Description')
        if len(descriptions_) != 0:
            descriptions: list = []
            for description_ in descriptions_:
                tmp = TRUBLNote().process_element(description_,
                                                  cbcnamespace,
                                                  cacnamespace)
                if tmp is not None:
                    descriptions.append(tmp)
            if len(descriptions) != 0:
                document.description = descriptions
                document.save()

        return document
