from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractXMLFileTypeHandler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def handle_request(self, filepath):
        pass
