# from __future__ import annotations
from abc import ABC, abstractmethod

from trebelge.XMLFileTypeState import XMLFileTypeStateContext


class XMLFileTypeState(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a reference to the Context object,
    associated with the State. This reference can be used by States to
    transition the Context to another State.
    """

    _context: XMLFileTypeStateContext = None

    def get_context(self):
        return self._context

    def set_context(self, context: XMLFileTypeStateContext):
        self._context = context

    @abstractmethod
    def find_record_status(self):
        pass

    @abstractmethod
    def list_file_namespaces(self):
        pass
