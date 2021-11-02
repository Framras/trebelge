# from __future__ import annotations

from trebelge.XMLFileTypeState.AbstractXMLFileTypeState import AbstractXMLFileTypeState


class NewInvoiceState(AbstractXMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self):
        pass

    def list_file_namespaces(self) -> None:
        pass
