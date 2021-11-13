# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class ExchangeRate(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'TaxExchangeRate'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): SourceCurrencyCode
        self._mapping['SourceCurrencyCode'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Zorunlu(1): TargetCurrencyCode
        self._mapping['TargetCurrencyCode'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Zorunlu(1): CalculationRate
        self._mapping['CalculationRate'] = ('cbc', '', 'Zorunlu(1)', False, False, True)
        # Seçimli(0..1): Date
        self._mapping['Date'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
