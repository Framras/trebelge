from __future__ import annotations
from abc import ABC, abstractmethod

from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeState.XMLFileTypeState import XMLFileTypeState


class DespatchAdviceState(XMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    def find_record_status(self) -> None:
        pass

    def handle2(self) -> None:
        pass
