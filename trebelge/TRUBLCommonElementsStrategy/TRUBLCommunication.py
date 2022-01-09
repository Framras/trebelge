from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommunication(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Communication'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ChannelCode'] = ('cbc', 'channelcode', 'Zorunlu(1)')
        channelcode: Element = element.find('./' + cbcnamespace + 'ChannelCode')
        # ['Value'] = ('cbc', 'value', 'Zorunlu(1)')
        value: Element = element.find('./' + cbcnamespace + 'Value')
        if channelcode is None or channelcode.text is None or \
                value is None or value.text is None:
            return None
        frappedoc: dict = dict(channelcode=channelcode.text,
                               value=value.text)
        # ['Channel'] = ('cbc', 'channel', 'Seçimli (0...1)')
        channel_: Element = element.find('./' + cbcnamespace + 'Channel')
        if channel_ is not None and channel_.text is not None:
            frappedoc['channel'] = channel_.text
        return self._get_frappedoc(self._frappeDoctype, frappedoc)
