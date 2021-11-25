# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class MonetaryTotal(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _mapping = dict()
    _elementTag: str = 'LegalMonetaryTotal'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): LineExtensionAmount
        self._mapping['LineExtensionAmount'] = ('cbc', '', 'Zorunlu(1)', True, True, True)
        # Zorunlu(1): TaxExclusiveAmount
        self._mapping['TaxExclusiveAmount'] = ('cbc', '', 'Zorunlu(1)', True, True, True)
        # Zorunlu(1): TaxInclusiveAmount
        self._mapping['TaxInclusiveAmount'] = ('cbc', '', 'Zorunlu(1)', True, True, True)
        # Seçimli(0..1): AllowanceTotalAmount
        self._mapping['AllowanceTotalAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): ChargeTotalAmount
        self._mapping['ChargeTotalAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): PayableRoundingAmount
        self._mapping['PayableRoundingAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Zorunlu(1): PayableAmount
        self._mapping['PayableAmount'] = ('cbc', '', 'Zorunlu(1)', True, True, True)
        # attrib currencyID for tags endswith('Amount')
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
