# from __future__ import annotations
from trebelge.XMLFileTypeState.AbstractXMLFileTypeState import AbstractXMLFileTypeState


class DespatchAdviceState(AbstractXMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self) -> None:
        pass

    def handle2(self) -> None:
        pass