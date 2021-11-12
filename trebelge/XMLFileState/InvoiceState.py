# from __future__ import annotations

import frappe
from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState
from trebelge.XMLFileState.NewInvoiceState import NewInvoiceState


class InvoiceState(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'

    def find_ebelge_status(self):
        if not frappe.db.exists({"doctype": self._frappeDoctype,
                                 "uuid": self.get_context().get_uuid()}):
            self.get_context().set_state(NewInvoiceState())
