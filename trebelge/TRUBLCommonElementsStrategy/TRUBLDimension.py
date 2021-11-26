from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLDimension(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['AttributeID'] = ('cbc', 'attributeid', 'Zorunlu(1)')
        ['Measure'] = ('cbc', 'measure', 'Seçimli (0...1)')
        ['unitCode'] = ('', 'measure_unitcode', 'Zorunlu(1)')
        ['Description'] = ('cbc', 'descriptions', 'Seçimli(0..n)', 'description')
        ['MinimumMeasure'] = ('cbc', 'minimummeasure', 'Seçimli(0..1)')
        ['unitCode'] = ('', 'minimummeasure_unitcode', 'Zorunlu(1)')
        ['MaximumMeasure'] = ('cbc', 'maximummeasure', 'Seçimli(0..1)')
        ['unitCode'] = ('', 'maximummeasure_unitcode', 'Zorunlu(1)')
        """
        dimension: dict = {'attributeid': element.find(cbcnamespace + 'AttributeID').text}
        measure_ = element.find(cbcnamespace + 'Measure')
        if measure_ is not None:
            dimension['measure'] = measure_.text
            dimension['measure_unitcode'] = measure_.attrib.get(
                'unitCode')
        descriptions_ = element.findall(cbcnamespace + 'Description')
        if descriptions_ is not None:
            descriptions: list = []
            for description in descriptions_:
                descriptions.append({'description': description.text})
            dimension['descriptions'] = descriptions
        minimummeasure_ = element.find(cbcnamespace + 'MinimumMeasure')
        if minimummeasure_ is not None:
            dimension['minimummeasure'] = minimummeasure_.text
            dimension['minimummeasure_unitcode'] = minimummeasure_.attrib.get(
                'unitCode')
        maximummeasure_ = element.find(cbcnamespace + 'MaximumMeasure')
        if maximummeasure_ is not None:
            dimension['maximummeasure'] = maximummeasure_.text
            dimension['maximummeasure_unitcode'] = maximummeasure_.attrib.get(
                'unitCode')

        return dimension
