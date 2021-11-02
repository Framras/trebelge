# from __future__ import annotations
from trebelge.XMLFileProcessStrategy import XMLFileProcessStrategy


class XMLFileProcessStrategyContext:
    """
    The Context defines the interface of interest to clients.
    """
    _file_path: str = ''
    _strategy: XMLFileProcessStrategy = None
    """
    Usually, the Context accepts a strategy through the constructor, but
    also provides a setter to change it at runtime.
    """

    def set_strategy(self, strategy: XMLFileProcessStrategy):
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def get_strategy(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """
        return self._strategy

    def set_file_path(self, file_path: str):
        self._file_path = file_path

    def get_file_path(self):
        return self._file_path

    def return_file_data(self):
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        return self._strategy.return_file_data(self)
