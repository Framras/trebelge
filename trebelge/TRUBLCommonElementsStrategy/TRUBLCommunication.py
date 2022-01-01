from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommunication(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Communication'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ChannelCode'] = ('cbc', 'channelcode', 'Zorunlu(1)')
        channelcode = element.find('./' + cbcnamespace + 'ChannelCode')
        # ['Value'] = ('cbc', 'value', 'Zorunlu(1)')
        value = element.find('./' + cbcnamespace + 'Value')
        if channelcode.text is not None and value.text is not None:
            frappedoc: dict = {'channelcode': channelcode.text,
                               'value': value.text}
            # ['Channel'] = ('cbc', 'channel', 'Seçimli (0...1)')
            channel_: Element = element.find('./' + cbcnamespace + 'Channel')
            if channel_ is not None:
                frappedoc['channel'] = channel_.text
        else:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
