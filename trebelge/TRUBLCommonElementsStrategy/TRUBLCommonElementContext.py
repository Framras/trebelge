from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy import TRUBLCommonElement


class TRUBLCommonElementContext:
    """
    The Context defines the interface of interest to clients.
    """
    _strategy: TRUBLCommonElement = None
    """
    Usually, the Context accepts a strategy through the constructor, but
    also provides a setter to change it at runtime.
    """

    def set_strategy(self, strategy: TRUBLCommonElement):
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def get_strategy(self) -> TRUBLCommonElement:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """
        return self._strategy

    def return_element_data(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        return self._strategy.process_element(element, cbcnamespace, cacnamespace)
