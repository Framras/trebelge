# from __future__ import annotations
from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileTypeState


class DespatchAdviceState(AbstractXMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self) -> None:
        pass

    def initiate_new_record(self) -> None:
        pass
