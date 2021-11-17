# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class CustomerParty(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'CustomerParty'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): Party:Party
        self._mapping['Party'] = ('cac', 'Party', 'Zorunlu(1)', True, False, False)
        # Seçimli(0..1): DeliveryContact:Contact
        self._mapping['DeliveryContact'] = ('cac', 'Contact', 'Seçimli(0..1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
