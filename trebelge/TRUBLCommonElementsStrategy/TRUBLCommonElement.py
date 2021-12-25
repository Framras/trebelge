from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document


class TRUBLCommonElement(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @staticmethod
    def _get_frappedoc(frappedoctype: str, frappedoc: dict) -> Document:
        if frappedoc is not None:
            if frappe.get_all(frappedoctype, filters=frappedoc) is not None:
                pass
            else:
                newfrappedoc = dict(frappedoc)
                newfrappedoc['doctype'] = frappedoctype
                _frappeDoc = frappe.get_doc(newfrappedoc)
                _frappeDoc.insert()

            return frappe.get_doc(
                frappedoctype,
                frappe.get_all(frappedoctype, filters=frappedoc)[0]['name'])
        else:
            frappe.log_error('Not enough data for Doctype' + frappedoctype, 'TRUBLCommonElement')

    @abstractmethod
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        pass
