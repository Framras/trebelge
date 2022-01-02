from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRoadTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR RoadTransport'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['LicensePlateID'] = ('cbc', 'licenseplateid', 'Zorunlu (1)')
        licenseplateid_ = element.find('./' + cbcnamespace + 'LicensePlateID')
        if licenseplateid_.text is not None:
            frappedoc: dict = {'licenseplateid': licenseplateid_.text}
        else:
            return None
        schemeid_: str = licenseplateid_.attrib.get('schemeID')
        if schemeid_ is not None:
            frappedoc['schemeid'] = schemeid_

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
