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
        # Seçimli(0..1): RegistrationName
        self._mapping['RegistrationName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): CompanyID
        self._mapping['CompanyID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): RegistrationDate
        self._mapping['RegistrationDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): SolePrioprietorshipIndicator
        self._mapping['SolePrioprietorshipIndicator'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): CorporateStockAmount
        self._mapping['CorporateStockAmount'] = (
            'cbc', '', 'Seçimli (0...1)', True, True, True)
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False)
        # Seçimli(0..1): FullyPaidSharesIndicator
        self._mapping['FullyPaidSharesIndicator'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): CorporateRegistrationScheme
        self._mapping['CorporateRegistrationScheme'] = (
            'cac', 'CorporateRegistrationScheme', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): HeadOfficeParty
        self._mapping['HeadOfficeParty'] = ('cac', 'HeadOfficeParty', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)