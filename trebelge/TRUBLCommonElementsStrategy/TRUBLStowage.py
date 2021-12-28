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
        # ['Location'] = ('cac', 'Location', 'Seçimli (0...n)')
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)', 'measurementdimension')
        cacsecimli0n: list = \
            [{'Tag': 'Location', 'strategy': TRUBLLocation(), 'fieldName': 'location'},
             {'Tag': 'MeasurementDimension', 'strategy': TRUBLDimension(), 'fieldName': 'measurementdimension'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall('./' + cacnamespace + element_.get('Tag'))
            if tagelements_:
                tagelements: list = []
                for tagelement in tagelements_:
                    tagelements.append(element_.get('strategy').process_element(tagelement,
                                                                                cbcnamespace,
                                                                                cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
