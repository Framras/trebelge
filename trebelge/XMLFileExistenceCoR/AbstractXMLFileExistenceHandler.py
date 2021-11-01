from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractXMLFileExistenceHandler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def handleRequest(self, filepath):
        pass

    @abstractmethod
    def setSuccessor(self, successor):
        pass
