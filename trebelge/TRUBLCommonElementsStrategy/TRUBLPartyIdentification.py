from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPartyIdentification(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Party Identification'
    _frappeDoc = None

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        # ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        # ['schemeID'] = ('', 'schemeid', 'Zorunlu (1)')
        partyidentification_ = element.find(cbcnamespace + 'ID')
        partyidentification: dict = {'id': partyidentification_.text,
                                     'schemeid': partyidentification_.attrib.get('schemeID')}
        frappe.get_all(self._frappeDoctype, filters=partyidentification,
                       fields={"name"})
        # TODO convert to table multiselect
        if frappe.db.exists(partyidentification):
            self._frappeDoc = frappe.get_doc(partyidentification)
        else:
            a = {'doctype': self._frappeDoctype}

            self._frappeDoc = frappe.get_doc(partyidentification)
            self._frappeDoc.insert()

        return self._frappeDoc.get_value('name')
