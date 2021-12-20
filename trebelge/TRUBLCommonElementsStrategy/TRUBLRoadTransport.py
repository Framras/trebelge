from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRoadTransport(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR RoadTransport'

    def process_element(self, element: Element, cbcnamespace: str) -> Document:
        # ['LicensePlateID'] = ('cbc', 'licenseplateid', 'Zorunlu (1)')
        licenseplateid_ = element.find(cbcnamespace + 'LicensePlateID')
        frappedoc: dict = {'licenseplateid': licenseplateid_.text}
        # ['schemeID'] = ('', 'licenseplateid_schemeid', 'Seçimli (0...1)')
        licenseplateid_schemeid = licenseplateid_.attrib.get('schemeID')
        if licenseplateid_schemeid is not None:
            frappedoc['licenseplateid_schemeid'] = licenseplateid_schemeid

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
