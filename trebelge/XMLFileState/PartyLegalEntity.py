# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class PartyLegalEntity(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'PartyLegalEntity'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['RegistrationName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['CompanyID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['RegistrationDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['SolePrioprietorshipIndicator'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['CorporateStockAmount'] = (
            'cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['FullyPaidSharesIndicator'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['CorporateRegistrationScheme'] = (
            'cac', 'CorporateRegistrationScheme', 'Seçimli (0...1)', True, False, False)
        self._mapping['HeadOfficeParty'] = ('cac', 'HeadOfficeParty', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
