# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Party(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Party'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['WebsiteURI'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['EndpointID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['IndustryClassificationCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['PartyIdentification'] = ('cac', 'PartyIdentification', 'Zorunlu (1...n)', True, False, False)
        self._mapping['PartyName'] = ('cac', 'PartyName', 'Seçimli (0...1)', True, False, False)
        self._mapping['PostalAddress'] = ('cac', 'PostalAddress', 'Zorunlu (1)', True, False, False)
        self._mapping['PhysicalLocation'] = ('cac', 'PhysicalLocation', 'Seçimli (0...1)', True, False, False)
        self._mapping['PartyTaxScheme'] = ('cac', 'PartyTaxScheme', 'Seçimli (0...1)', True, False, False)
        self._mapping['PartyLegalEntity'] = ('cac', 'PartyLegalEntity', 'Seçimli (0...n)', True, False, False)
        self._mapping['Contact'] = ('cac', 'Contact', 'Seçimli (0...1)', True, False, False)
        self._mapping['Person'] = ('cac', 'Person', 'Seçimli (0...1)', True, False, False)
        self._mapping['AgentParty'] = ('cac', 'AgentParty', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
