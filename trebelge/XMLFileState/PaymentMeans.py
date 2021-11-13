# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class PaymentMeans(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'PaymentMeans'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): PaymentMeansCode
        self._mapping['PaymentMeansCode'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): PaymentDueDate
        self._mapping['PaymentDueDate'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): PaymentChannelCode
        self._mapping['PaymentChannelCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): InstructionNote
        self._mapping['InstructionNote'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): PayerFinancialAccount:FinancialAccount
        self._mapping['PayerFinancialAccount'] = (
            'cac', 'FinancialAccount', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): PayeeFinancialAccount:FinancialAccount
        self._mapping['PayeeFinancialAccount'] = (
            'cac', 'FinancialAccount', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
