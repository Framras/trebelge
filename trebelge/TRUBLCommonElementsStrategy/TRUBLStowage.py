from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation


class TRUBLStowage(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Stowage'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['LocationID'] = ('cbc', 'locationid', 'Seçimli (0...1)')
        locationid_: Element = element.find('./' + cbcnamespace + 'LocationID')
        if locationid_ is not None:
            if locationid_.text is not None:
                frappedoc['locationid'] = locationid_.text
        if frappedoc == {}:
            return None
        # ['Location'] = ('cac', 'Location', 'Seçimli (0...n)')
        locations: list = []
        locations_: list = element.findall('./' + cacnamespace + 'Location')
        if len(locations_) != 0:
            for location_ in locations_:
                tmp = TRUBLLocation().process_element(location_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    locations.append(tmp)
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)', 'measurementdimension')
        measurementdimensions: list = []
        measurementdimensions_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if len(measurementdimensions_) != 0:
            for measurementdimension_ in measurementdimensions_:
                tmp = TRUBLDimension().process_element(measurementdimension_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    measurementdimensions.append(tmp)
        if len(locations) + len(measurementdimensions) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(locations) != 0:
                document.location = locations
            if len(measurementdimensions) != 0:
                document.measurementdimension = measurementdimensions
            document.save()

        return document
