# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class TaxSubtotal(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'TaxSubtotal'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): TaxableAmount
        self._mapping['TaxableAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Zorunlu(1): TaxAmount
        self._mapping['TaxAmount'] = ('cbc', '', 'Zorunlu(1)', True, True, True)
        # Seçimli(0..1): CalculationSequenceNumeric
        self._mapping['CalculationSequenceNumeric'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): TransactionCurrencyTaxAmount
        self._mapping['TransactionCurrencyTaxAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): Percent
        self._mapping['Percent'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): BaseUnitMeasure
        self._mapping['BaseUnitMeasure'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): PerUnitAmount
        self._mapping['PerUnitAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Zorunlu(1): TaxCategory:TaxCategory
        self._mapping['TaxCategory'] = ('cac', 'TaxCategory', 'Zorunlu(1)', True, False, False)
        # attrib currencyID for tags endswith('Amount')
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
