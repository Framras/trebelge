# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class AllowanceCharge(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'AllowanceCharge'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Zorunlu(1): ChargeIndicator
        self._mapping['ChargeIndicator'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        """
        İskonto ise “false”, artırım ise “true”
        """
        # Seçimli(0..1): AllowanceChargeReason
        self._mapping['AllowanceChargeReason'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): MultiplierFactorNumeric
        self._mapping['MultiplierFactorNumeric'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): SequenceNumeric
        self._mapping['SequenceNumeric'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Zorunlu(1): Amount
        self._mapping['Amount'] = ('cbc', '', 'Zorunlu (1)', True, True, True)
        # Seçimli(0..1): BaseAmount
        self._mapping['BaseAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        # Seçimli(0..1): PerUnitAmount
        self._mapping['PerUnitAmount'] = ('cbc', '', 'Seçimli (0...1)', True, True, True)
        self._mapping['currencyID'] = ('', '', 'Zorunlu (1)', False, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
