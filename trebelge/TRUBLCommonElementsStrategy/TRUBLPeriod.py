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
        cbcsecimli01: list = ['StartDate', 'StartTime', 'EndDate', 'EndTime', 'Description']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['DurationMeasure'] = ('cbc', 'durationmeasure', 'Seçimli (0...1)')
        durationmeasure_: Element = element.find('./' + cbcnamespace + 'DurationMeasure')
        if durationmeasure_:
            frappedoc['durationmeasure'] = durationmeasure_.text
            frappedoc['unitcode'] = durationmeasure_.attrib.get('unitCode')

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
