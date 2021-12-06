from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPeriod(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        """
        ['StartDate'] = ('cbc', 'startdate', 'Seçimli (0...1)')
        ['StartTime'] = ('cbc', 'starttime', 'Seçimli (0...1)')
        ['EndDate'] = ('cbc', 'enddate', 'Seçimli (0...1)')
        ['EndTime'] = ('cbc', 'endtime', 'Seçimli (0...1)')
        ['DurationMeasure'] = ('cbc', 'durationmeasure', 'Seçimli (0...1)')
        ['unitCode'] = ('', 'durationmeasure_unitcode', 'Zorunlu (1)')
        ['Description'] = ('cbc', 'description', 'Seçimli (0...1)')
        """
        period: dict = {}
        cbcsecimli01: list = ['StartDate', 'StartTime', 'EndDate', 'EndTime', 'Description']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                period[field_.tag.lower()] = field_.text

        durationmeasure_ = element.find(cbcnamespace + 'DurationMeasure')
        if durationmeasure_ is not None:
            period['durationmeasure'] = durationmeasure_.text
            period['durationmeasure_unitcode'] = durationmeasure_.attrib.get(
                'unitCode')

        return period
