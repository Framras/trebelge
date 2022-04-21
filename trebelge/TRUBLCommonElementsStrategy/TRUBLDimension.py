from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLDimension(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Dimension'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['AttributeID'] = ('cbc', 'attributeid', 'Zorunlu(1)')
        attributeid_: Element = element.find('./' + cbcnamespace + 'AttributeID')
        if attributeid_ is not None:
            if attributeid_.text is not None:
                frappedoc['attributeid'] = attributeid_.text.strip()
        # ['Measure'] = ('cbc', 'measure', 'Seçimli (0...1)')
        measure_: Element = element.find('./' + cbcnamespace + 'Measure')
        if measure_ is not None:
            if measure_.text is not None:
                frappedoc['measure'] = measure_.text.strip()
                frappedoc['measureunitcode'] = measure_.attrib.get('unitCode').strip()
        # ['MinimumMeasure'] = ('cbc', 'minimummeasure', 'Seçimli(0..1)')
        minimummeasure_: Element = element.find('./' + cbcnamespace + 'MinimumMeasure')
        if minimummeasure_ is not None:
            if minimummeasure_.text is not None:
                frappedoc['minimummeasure'] = minimummeasure_.text.strip()
                frappedoc['minimummeasureunitcode'] = minimummeasure_.attrib.get('unitCode').strip()
        # ['MaximumMeasure'] = ('cbc', 'maximummeasure', 'Seçimli(0..1)')
        maximummeasure_: Element = element.find('./' + cbcnamespace + 'MaximumMeasure')
        if maximummeasure_ is not None:
            if maximummeasure_.text is not None:
                frappedoc['maximummeasure'] = maximummeasure_.text.strip()
                frappedoc['maximummeasureunitcode'] = maximummeasure_.attrib.get('unitCode').strip()
        if frappedoc == {}:
            return None
        # ['Description'] = ('cbc', 'descriptions', 'Seçimli(0..n)', 'description')
        descriptions_: list = element.findall('./' + cbcnamespace + 'Description')
        if len(descriptions_) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            for description_ in descriptions_:
                element_ = description_.text
                if element_ is not None and element_.strip() != '':
                    document.append("description", dict(note=element_.strip()))
                    document.save()

        return document
