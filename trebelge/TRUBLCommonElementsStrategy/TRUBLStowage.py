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
        if locationid_:
            frappedoc['locationid'] = locationid_.text
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        cacsecimli0n: list = \
            [{'Tag': 'Location', 'strategy': TRUBLLocation(), 'fieldName': 'location'},
             {'Tag': 'MeasurementDimension', 'strategy': TRUBLDimension(), 'fieldName': 'measurementdimension'}
             ]
        # ['Location'] = ('cac', 'Location', 'Seçimli (0...n)')
        locations_: list = element.findall('./' + cacnamespace + 'Location')
        if len(locations_) != 0:
            locations: list = []
            for location_ in locations_:
                locations.append(TRUBLLocation().process_element(location_,
                                                                 cbcnamespace,
                                                                 cacnamespace))
            document.location = locations
            document.save()
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)', 'measurementdimension')
        measurementdimensions_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if len(measurementdimensions_) != 0:
            measurementdimensions: list = []
            for measurementdimension_ in measurementdimensions_:
                measurementdimensions.append(TRUBLDimension().process_element(measurementdimension_,
                                                                              cbcnamespace,
                                                                              cacnamespace))
            document.measurementdimension = measurementdimensions
            document.save()

        return
