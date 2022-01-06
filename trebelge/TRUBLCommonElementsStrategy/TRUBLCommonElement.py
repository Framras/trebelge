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
    def _get_frappedoc(frappedoctype: str, frappedoc: dict, leaf: bool = True) -> Document:
        if leaf:
            if len(frappe.get_all(frappedoctype, filters=frappedoc)) == 0:
                newfrappedoc = dict(frappedoc)
                newfrappedoc['doctype'] = frappedoctype
                frappedoc_ = frappe.get_doc(newfrappedoc)
                return frappedoc_.insert()
            else:
                return frappe.get_doc(
                    frappedoctype,
                    frappe.get_all(frappedoctype, filters=frappedoc)[0]["name"])
        else:
            newfrappedoc = dict(frappedoc)
            newfrappedoc['doctype'] = frappedoctype
            frappedoc_ = frappe.get_doc(newfrappedoc)
            return frappedoc_.insert()

    @staticmethod
    def _update_frappedoc(frappedoctype: str, frappedoc: dict, document: Document) -> Document:
        if len(frappe.get_all(frappedoctype, filters=frappedoc)) == 0:
            return document
        else:
            frappe.rename_doc(frappedoctype,
                              document.name,
                              frappe.get_doc(frappedoctype,
                                             frappe.get_all(frappedoctype, filters=frappedoc)[0]["name"]),
                              merge=True)
            return frappe.get_doc(
                frappedoctype,
                frappe.get_all(frappedoctype, filters=frappedoc)[0]["name"])

    @abstractmethod
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        pass
