from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyName(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Partyname'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        # ['Name'] = ('cbc', 'partyname', 'Zorunlu (1)')
        partyname: dict = {'partyname': element.find(cbcnamespace + 'Name')}

        if not frappe.get_all(self._frappeDoctype, filters=partyname):
            pass
        else:
            newpartyname = partyname
            newpartyname['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newpartyname)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=partyname)
