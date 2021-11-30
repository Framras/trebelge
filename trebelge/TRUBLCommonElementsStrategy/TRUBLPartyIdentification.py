from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyIdentification(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Party Identification'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        # ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        # ['schemeID'] = ('', 'schemeid', 'Zorunlu (1)')
        partyidentification_ = element.find(cbcnamespace + 'ID')
        partyidentification: dict = {'id': partyidentification_.text,
                                     'schemeid': partyidentification_.attrib.get('schemeID')}

        if not frappe.get_all(self._frappeDoctype, filters=partyidentification, fields={"name"}):
            pass
        else:
            newpartyidentification = partyidentification
            newpartyidentification['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newpartyidentification)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=partyidentification, fields={'name'})
