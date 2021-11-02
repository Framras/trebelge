from __future__ import annotations

from trebelge.XMLFileTypeState import XMLFileTypeState


class XMLFileTypeContext:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: XMLFileTypeState) -> None:
        self.set_state(state)

    def set_state(self, state: XMLFileTypeState):
        """
        The Context allows changing the State object at runtime.
        """

        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()
