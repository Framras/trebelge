# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class TaxTotal(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'TaxTotal'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): TaxAmount
        self._mapping['TaxAmount'] = ('cbc', '', 'Zorunlu(1)', True, True, True)
        # Zorunlu(1..n): TaxSubtotal:TaxSubtotal
        self._mapping['TaxSubtotal'] = ('cac', 'TaxSubtotal', 'Zorunlu(1..n)', True, False, False)
        # attrib currencyID for tags endswith('Amount')
        self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
