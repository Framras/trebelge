from datetime import datetime
from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPeriod(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Period'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['StartDate'] = ('cbc', 'startdate', 'Seçimli (0...1)')
        # ['StartTime'] = ('cbc', 'starttime', 'Seçimli (0...1)')
        # ['EndDate'] = ('cbc', 'enddate', 'Seçimli (0...1)')
        # ['EndTime'] = ('cbc', 'endtime', 'Seçimli (0...1)')
        # ['Description'] = ('cbc', 'description', 'Seçimli (0...1)')
        cbcsecimli01: list = ['StartDate', 'EndDate', 'Description']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text.strip()
        # ['StartTime'] = ('cbc', '', 'Seçimli (0...1)')
        starttime_: Element = element.find('./' + cbcnamespace + 'StartTime')
        if starttime_ is not None:
            try:
                frappedoc['starttime'] = datetime.strptime(starttime_.text, '%H:%M:%S')
            except ValueError:
                pass
        # ['EndTime'] = ('cbc', '', 'Seçimli (0...1)')
        endtime_: Element = element.find('./' + cbcnamespace + 'EndTime')
        if endtime_ is not None:
            try:
                frappedoc['endtime'] = datetime.strptime(endtime_.text, '%H:%M:%S')
            except ValueError:
                pass
        # ['DurationMeasure'] = ('cbc', 'durationmeasure', 'Seçimli (0...1)')
        durationmeasure_: Element = element.find('./' + cbcnamespace + 'DurationMeasure')
        if durationmeasure_ is not None:
            frappedoc['durationmeasure'] = durationmeasure_.text.strip()
            frappedoc['unitcode'] = durationmeasure_.attrib.get('unitCode').strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
