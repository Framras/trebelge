# from __future__ import annotations
from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileTypeState


class XMLFileStateContext:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """
    _file_path: str = ''
    _state: AbstractXMLFileTypeState = None
    """
    A reference to the current state of the Context.
    """
    # initiate CoR pattern for xmlFile
    _hXMLFileHandler: AbstractXMLFileHandler = InvoiceHandler()
    # initiate Context of State pattern
    _cXMLFileTypeStateContext = XMLFileTypeStateContext()

    def __init__(self, file_path: str):
        # initiate Context of State pattern for FileType
        self._cXMLFileTypeStateContext.set_file_path(file_path)
        # handle file by CoR to determine State
        self._hXMLFileHandler.handle_xml_file(self._cXMLFileTypeStateContext)
        # check on State if file is previously processed and recorded
        self._cXMLFileTypeStateContext.find_record_status()
        # TODO: Take it from here (The current State in StateContext is the next step)
        self._cXMLFileTypeStateContext.list_file_namespaces()

    def set_state(self, state: AbstractXMLFileTypeState):
        """
        The Context allows changing the State object at runtime.
        """
        self._state = state
        self._state.set_context(self)

    def set_file_path(self, file_path: str):
        self._file_path = file_path

    def get_file_path(self):
        return self._file_path

    """
    The Context delegates part of its behavior to the current State object.
    """

    def find_ebelge_type(self, file_path: str):
        self._state.find_ebelge_type(file_path)

    def find_record_status(self):
        self._state.find_record_status()

    def initiate_new_record(self):
        self._state.initiate_new_record()
