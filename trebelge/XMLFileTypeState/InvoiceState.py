from __future__ import annotations
from abc import ABC, abstractmethod

from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeState.XMLFileTypeState import XMLFileTypeState


class InvoiceState(XMLFileTypeState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """

    @property
    def context(self) -> XMLFileTypeContext:
        return self._context

    @context.setter
    def context(self, context: XMLFileTypeContext) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass
