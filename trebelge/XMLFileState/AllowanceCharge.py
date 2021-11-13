# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class AllowanceCharge(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        self._mapping['ChargeIndicator'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        """
        İskonto ise “false”, artırım ise “true”
        """
        self._mapping['AllowanceChargeReason'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['MultiplierFactorNumeric'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['SequenceNumeric'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['Amount'] = ('cbc', '', 'Zorunlu (1)', False, False, True)
        self._mapping['BaseAmount'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['PerUnitAmount'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        self._mapping['AllowanceCharge'] = ('cac', 'AllowanceCharge', '', False, False, True)
