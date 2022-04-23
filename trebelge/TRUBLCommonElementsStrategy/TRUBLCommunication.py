from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommunication(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Communication'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ChannelCode'] = ('cbc', 'channelcode', 'Zorunlu(1)')
        channelcode: Element = element.find('./' + cbcnamespace + 'ChannelCode')
        # ['Value'] = ('cbc', 'value', 'Zorunlu(1)')
        value: Element = element.find('./' + cbcnamespace + 'Value')
        if channelcode is not None:
            if channelcode.text is not None:
                frappedoc['channelcode'] = channelcode.text.strip()
        if value is not None:
            if value.text is not None:
                frappedoc['value'] = value.text.strip()
        # ['Channel'] = ('cbc', 'channel', 'Seçimli (0...1)')
        channel_: Element = element.find('./' + cbcnamespace + 'Channel')
        if channel_ is not None:
            if channel_.text is not None:
                frappedoc['channel'] = channel_.text.strip()
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
