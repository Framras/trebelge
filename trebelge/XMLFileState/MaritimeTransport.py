# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class MaritimeTransport(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'MaritimeTransport'

    def find_ebelge_status(self):
        pass

    def define_mappings(self):
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        # Seçimli(0..1): VesselID
        self._mapping['VesselID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): VesselName
        self._mapping['VesselName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): RadioCallSignID
        self._mapping['RadioCallSignID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..n): ShipsRequirements
        self._mapping['ShipsRequirements'] = ('cbc', '', 'Seçimli (0...n)', False, False, True)
        # Seçimli(0..1): GrossTonnageMeasure
        self._mapping['GrossTonnageMeasure'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): NetTonnageMeasure
        self._mapping['NetTonnageMeasure'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
        # Seçimli(0..1): RegistryCertificateDocumentReference:DocumentReference
        self._mapping['RegistryCertificateDocumentReference'] = (
            'cac', 'DocumentReference', 'Seçimli (0...1)', True, False, False)
        # Seçimli(0..1): RegistryPortLocation:Location
        self._mapping['RegistryPortLocation'] = (
            'cac', 'Location', 'Seçimli (0...1)', True, False, False)
        self._mapping[self._elementTag] = ('cac', '', '', False, False, True)
