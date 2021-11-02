# from __future__ import annotations
from trebelge.XMLFileProcessStrategy import XMLFileProcessStrategy


class XMLFileProcessContext:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: XMLFileProcessStrategy):
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    def strategy(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """
        return self._strategy

    def set_strategy(self, strategy: XMLFileProcessStrategy):
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def return_file_data(self, file_path: str):
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        return self._strategy.return_file_data(file_path)
