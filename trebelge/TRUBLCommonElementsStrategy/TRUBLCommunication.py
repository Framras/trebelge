from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCommunication(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Communication'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['ChannelCode'] = ('cbc', 'channelcode', 'Zorunlu(1)')
        # ['Value'] = ('cbc', 'value', 'Zorunlu(1)')
        communication: dict = {'channelcode': element.find(cbcnamespace + 'ChannelCode').text,
                               'value': element.find(cbcnamespace + 'Value').text}
        # ['Channel'] = ('cbc', 'channel', 'Seçimli (0...1)')
        channel_ = element.find(cbcnamespace + 'Channel')
        if channel_ is not None:
            communication['channel'] = channel_.text

        if not frappe.get_all(self._frappeDoctype, filters=communication):
            pass
        else:
            newcommunication = communication
            newcommunication['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newcommunication)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=communication)
