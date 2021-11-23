# from __future__ import annotations
import xml.etree.ElementTree as ET

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
    _cac_namespace: str = ''
    _cbc_namespace: str = ''
    _uuid: str = ''
    _mapping = dict()
    _new_frappe_doc = dict()

    # initiate CoR pattern for xmlFile

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

    def _set_namespaces(self):
        # read all namespaces
        self._namespaces = dict([node for _, node in ET.iterparse(self.get_file_path(), events=['start-ns'])])
        self._set_default_namespace()
        self._set_cac_namespace()
        self._set_cbc_namespace()
        self._set_uuid()

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

    def _set_uuid(self):
        self._uuid = ET.parse(self.get_file_path()).getroot().find(self.get_cbc_namespace() + 'UUID').text

    def get_uuid(self):
        return self._uuid

    def set_mapping(self, mapping: dict):
        self._mapping = mapping

    def get_mapping(self):
        return self._mapping

    def set_new_frappe_doc(self, key: str, value):
        self._new_frappe_doc[key] = value

    def get_new_frappe_doc(self):
        return self._new_frappe_doc

    """
    The Context delegates part of its behavior to the current State object.
    """

    def read_xml_file(self):
        for event, elem in ET.iterparse(self.get_file_path(), events=("start", "end")):
            self.read_element_by_action(event, elem)

    def append_new_frappe_doc_field(self, key: str, value):
        self._new_frappe_doc[key].append = value

    def find_ebelge_status(self):
        self._state.find_ebelge_status()

    def define_mappings(self, tag: str, initiator: AbstractXMLFileState):
        self._state.define_mappings(tag, initiator)

    def read_element_by_action(self, event: str, element: ET.Element):
        self._state.read_element(event, element)
