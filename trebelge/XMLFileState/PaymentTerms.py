# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class PaymentTerms(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'PaymentTerms'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): Note
        self._mapping['Note'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): PenaltySurchargePercent
        self._mapping['PenaltySurchargePercent'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): Amount
        self._mapping['Amount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): PenaltyAmount
        self._mapping['PenaltyAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): PaymentDueDate
        self._mapping['PaymentDueDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): SettlementPeriod:Period
        self._mapping['SettlementPeriod'] = (
            'cac', 'Period', 'Seçimli (0...1)', True, False, False)
        # attrib currencyID for tags endswith('Amount')
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
