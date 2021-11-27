from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommunication(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ChannelCode'] = ('cbc', 'channelcode', 'Zorunlu(1)')
        ['Channel'] = ('cbc', 'channel', 'Seçimli (0...1)')
        ['Value'] = ('cbc', 'value', 'Zorunlu(1)')
        """
        communication: dict = {'channelcode': element.find(cbcnamespace + 'ChannelCode').text,
                               'channel': element.find(cbcnamespace + 'Channel').text}
        value_ = element.find(cbcnamespace + 'Value')
        if value_ is not None:
            communication[value_.tag.lower()] = value_.text

        return communication
