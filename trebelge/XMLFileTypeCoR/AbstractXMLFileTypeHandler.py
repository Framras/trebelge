from __future__ import annotations
from abc import ABC, abstractmethod

from trebelge.XMLFileTypeState import XMLFileTypeContext


class AbstractXMLFileTypeHandler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def handle_request(self, file_path: str, xml_file_type_context: XMLFileTypeContext):
        pass
