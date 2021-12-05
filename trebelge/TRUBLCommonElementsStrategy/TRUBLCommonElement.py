from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element


class TRUBLCommonElement(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
