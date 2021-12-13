from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element

import frappe


class TRUBLCommonElement(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @staticmethod
    def get_frappedoc(frappedoctype: str, frappedoc: dict) -> list:
        if not frappe.get_all(frappedoctype, filters=frappedoc):
            pass
        else:
            newfrappedoc = frappedoc
            newfrappedoc['doctype'] = frappedoctype
            _frappeDoc = frappe.get_doc(newfrappedoc)
            _frappeDoc.insert()

        return frappe.get_all(frappedoctype, filters=frappedoc)

    @abstractmethod
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        pass
