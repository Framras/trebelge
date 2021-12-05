from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLRailTransport(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str):
        """
        ['TrainID'] = ('cbc', 'TrainID', 'Zorunlu(1)')
        ['RailCarID'] = ('cbc', 'RailCarID', 'Seçimli (0...1)')
        """
        railTransport: dict = {'trainid': element.find(cbcnamespace + 'TrainID').text}
        railcarid_ = element.find(cbcnamespace + 'RailCarID')
        if railcarid_ is not None:
            railTransport[railcarid_.tag.lower()] = railcarid_.text

        return railTransport
