# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class FinancialAccount(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'PayeeFinancialAccount'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ID
        self._mapping['ID'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): CurrencyCode
        self._mapping['CurrencyCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): PaymentNote
        self._mapping['PaymentNote'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): FinancialInstitutionBranch:Branch
        self._mapping['FinancialInstitutionBranch'] = ('cac', 'Branch', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
