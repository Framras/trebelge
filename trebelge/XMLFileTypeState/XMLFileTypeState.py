from __future__ import annotations
from abc import ABC, abstractmethod

from trebelge.XMLFileTypeState import XMLFileTypeContext


class XMLFileTypeState(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
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
