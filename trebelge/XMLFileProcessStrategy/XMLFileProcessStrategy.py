from abc import ABC, abstractmethod

from trebelge.XMLFileProcessStrategy import XMLFileProcessStrategyContext


class XMLFileProcessStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def return_xml_file_data(self, context: XMLFileProcessStrategyContext):
        pass
