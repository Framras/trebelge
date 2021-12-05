from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRoadTransport(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str):
        """
        ['LicensePlateID'] = ('cbc', 'licenseplateid', 'Zorunlu (1)')
        ['schemeID'] = ('', 'licenseplateid_schemeid', 'Seçimli (0...1)')
        """
        licenseplateid_ = element.find(cbcnamespace + 'LicensePlateID')
        roadTransport: dict = {'licenseplateid': licenseplateid_.text}
        licenseplateid_schemeid = licenseplateid_.attrib.get('schemeID')
        if licenseplateid_schemeid is not None:
            roadTransport['licenseplateid_schemeid'] = licenseplateid_schemeid

        return roadTransport
