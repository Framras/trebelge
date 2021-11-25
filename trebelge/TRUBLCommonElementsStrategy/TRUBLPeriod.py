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
        period_startdate = element.find(cbcnamespace + 'StartDate')
        if period_startdate is not None:
            period['startdate'] = period_startdate.text
        period_starttime = element.find(cbcnamespace + 'StartTime')
        if period_starttime is not None:
            period['starttime'] = period_starttime.text
        period_enddate = element.find(cbcnamespace + 'EndDate')
        if period_enddate is not None:
            period['enddate'] = period_enddate.text
        period_endtime = element.find(cbcnamespace + 'EndTime')
        if period_endtime is not None:
            period['endtime'] = period_endtime.text
        period_durationmeasure = element.find(cbcnamespace + 'DurationMeasure')
        if period_durationmeasure is not None:
            period['durationmeasure'] = period_durationmeasure.text
            period['durationmeasure_unitcode'] = period_durationmeasure.attrib.get(
                'unitCode')
        period_description = element.find(cbcnamespace + 'Description')
        if period_description is not None:
            period['description'] = period_description.text

        return period
