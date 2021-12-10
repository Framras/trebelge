from xml.etree.ElementTree import Element

from frappe import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLFinancialInstitution(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        'UBL TR FinancialInstitution'
        # ['Name'] = ('cbc', 'name', 'Seçimli(0..1)')
        financialInstitution: dict = {}
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            financialInstitution['financialinstitutionname'] = name_.text

        if not frappe.get_all(self._frappeDoctype, filters=documentreference):
            pass
        else:
            newdocumentreference = documentreference
        newdocumentreference['doctype'] = self._frappeDoctype
        _frappeDoc = frappe.get_doc(newdocumentreference)
        _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=documentreference)
