# from __future__ import annotations
import xml.etree.ElementTree as ET

from trebelge.XMLFileCoR import AbstractXMLFileHandler
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler
from trebelge.XMLFileState import AbstractXMLFileState


class XMLFileStateContext:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """
    _state: AbstractXMLFileState = None
    """
    A reference to the current state of the Context.
    """
    _file_path: str = ''
    _namespaces = dict()
    _default_namespace: str = ''
    _cbc_namespace: str = ''
    _cac_namespace: str = ''
    _uuid: str = ''
    # initiate CoR pattern for xmlFile
    _hXMLFileHandler: AbstractXMLFileHandler = InvoiceHandler()

    def __init__(self, file_path: str):
        # TODO: Take it from here (The current State in StateContext is the next step)
        self._cXMLFileTypeStateContext.list_file_namespaces()

    def set_state(self, state: AbstractXMLFileState):
        """
        The Context allows changing the State object at runtime.
        """
        self._state = state
        self._state.set_context(self)

    def set_file_path(self, file_path: str):
        self._file_path = file_path

    def get_file_path(self):
        return self._file_path

    def _set_namespaces(self, file_path: str):
        # read all namespaces
        self._namespaces = dict([node for _, node in ET.iterparse(file_path, events=['start-ns'])])
        self._set_default_namespace()
        self._set_cac_namespace()
        self._set_cbc_namespace()
        uuid_: str = ET.parse(file_path).getroot().find(cbc_namespace + 'UUID').text
        self._uuid = ET.parse(file_path).getroot().find(cbc_namespace + uuid).text}

        def get_namespaces(self):
            # return all namespaces
            return self._namespaces

        def _set_default_namespace(self):
            self._default_namespace = '{' + self.get_namespaces().get('') + '}'

        def get_default_namespace(self):
            return self._default_namespace

        def _set_cac_namespace(self):
            self._cac_namespace = '{' + self.get_namespaces().get('cac') + '}'

        def get_cac_namespace(self):
            return self._cac_namespace

        def _set_cbc_namespace(self):
            self._cbc_namespace = '{' + self.get_namespaces().get('cbc') + '}'

        def get_cbc_namespace(self):
            return self._cbc_namespace

        """
        The Context delegates part of its behavior to the current State object.
        """

        def find_ebelge_type(self):
            self._state.find_ebelge_type(self.get_file_path())

        def find_ebelge_status(self):
            self._state.find_ebelge_status()

        def initiate_new_record(self):
            self._state.initiate_new_record()
