from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommunication(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Communication'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ChannelCode'] = ('cbc', 'channelcode', 'Zorunlu(1)')
        # ['Value'] = ('cbc', 'value', 'Zorunlu(1)')
        frappedoc: dict = {'channelcode': element.find(cbcnamespace + 'ChannelCode').text,
                           'value': element.find(cbcnamespace + 'Value').text}
        # ['Channel'] = ('cbc', 'channel', 'Seçimli (0...1)')
        channel_: Element = element.find(cbcnamespace + 'Channel')
        if channel_:
            frappedoc['channel'] = channel_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
