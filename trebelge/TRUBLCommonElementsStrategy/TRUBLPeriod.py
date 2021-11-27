from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPeriod(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
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
        startdate_ = element.find(cbcnamespace + 'StartDate')
        if startdate_ is not None:
            period[startdate_.tag.lower()] = startdate_.text
        starttime_ = element.find(cbcnamespace + 'StartTime')
        if starttime_ is not None:
            period[starttime_.tag.lower()] = starttime_.text
        enddate_ = element.find(cbcnamespace + 'EndDate')
        if enddate_ is not None:
            period[enddate_.tag.lower()] = enddate_.text
        endtime_ = element.find(cbcnamespace + 'EndTime')
        if endtime_ is not None:
            period[endtime_.tag.lower()] = endtime_.text
        durationmeasure_ = element.find(cbcnamespace + 'DurationMeasure')
        if durationmeasure_ is not None:
            period['durationmeasure'] = durationmeasure_.text
            period['durationmeasure_unitcode'] = durationmeasure_.attrib.get(
                'unitCode')
        description_ = element.find(cbcnamespace + 'Description')
        if description_ is not None:
            period[description_.tag.lower()] = description_.text

        return period
