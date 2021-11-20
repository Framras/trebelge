# from __future__ import annotations
import xml.etree.ElementTree as ET

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState
from trebelge.XMLFileState.Country import Country


class Address(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _mapping = dict()
    _elementTag: str = 'Address'
    _invoiceElementTag: str = 'AccountingSupplierParty'
    _despatchElementTag: str = 'DespatchSupplierParty'
    _initiatorTag: str = ''

    def find_ebelge_status(self):
        pass

    def define_mappings(self, tag: str, initiator: AbstractXMLFileState):
        self._initiatorTag = tag
        #         "accountingsupplierparty_postaladdress_country"
        if tag == self._invoiceElementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Seçimli(0..1) : ID
            self._mapping['ID'] = (
                'cbc', 'accountingsupplierparty_postaladdress_id', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Postbox
            self._mapping['Postbox'] = (
                'cbc', 'accountingsupplierparty_postaladdress_postbox', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Room
            self._mapping['Room'] = (
                'cbc', 'accountingsupplierparty_postaladdress_room', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : StreetName
            self._mapping['StreetName'] = (
                'cbc', 'accountingsupplierparty_postaladdress_streetname', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : BlockName
            self._mapping['BlockName'] = (
                'cbc', 'accountingsupplierparty_postaladdress_blockname', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : BuildingName
            self._mapping['BuildingName'] = (
                'cbc', 'accountingsupplierparty_postaladdress_buildingname', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..n) : BuildingNumber
            self._mapping['BuildingNumber'] = (
                'cbc', 'accountingsupplierparty_postaladdress_buildingnumber', 'Seçimli(0..n)', False, False, True, '')
            # Zorunlu(1): CitySubdivisionName
            self._mapping['CitySubdivisionName'] = (
                'cbc', 'accountingsupplierparty_postaladdress_citysubdivisionname', 'Zorunlu(1)', False, False, True,
                '')
            # Zorunlu(1): CityName
            self._mapping['CityName'] = (
                'cbc', 'accountingsupplierparty_postaladdress_cityname', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1) : PostalZone
            self._mapping['PostalZone'] = (
                'cbc', 'accountingsupplierparty_postaladdress_postalzone', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Region
            self._mapping['Region'] = (
                'cbc', 'accountingsupplierparty_postaladdress_region', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : District
            self._mapping['District'] = (
                'cbc', 'accountingsupplierparty_postaladdress_district', 'Seçimli (0...1)', False, False, True, '')
        elif tag == self._despatchElementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Seçimli(0..1) : ID
            self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Postbox
            self._mapping['Postbox'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Room
            self._mapping['Room'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : StreetName
            self._mapping['StreetName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : BlockName
            self._mapping['BlockName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : BuildingName
            self._mapping['BuildingName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..n) : BuildingNumber
            self._mapping['BuildingNumber'] = ('cbc', '', 'Seçimli(0..n)', False, False, True, '')
            # Zorunlu(1): CitySubdivisionName
            self._mapping['CitySubdivisionName'] = ('cbc', '', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): CityName
            self._mapping['CityName'] = ('cbc', '', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1) : PostalZone
            self._mapping['PostalZone'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Region
            self._mapping['Region'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : District
            self._mapping['District'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
        elif tag == self._elementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Seçimli(0..1) : ID
            self._mapping['ID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Postbox
            self._mapping['Postbox'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Room
            self._mapping['Room'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : StreetName
            self._mapping['StreetName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : BlockName
            self._mapping['BlockName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : BuildingName
            self._mapping['BuildingName'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..n) : BuildingNumber
            self._mapping['BuildingNumber'] = ('cbc', '', 'Seçimli(0..n)', False, False, True, '')
            # Zorunlu(1): CitySubdivisionName
            self._mapping['CitySubdivisionName'] = ('cbc', '', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): CityName
            self._mapping['CityName'] = ('cbc', '', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1) : PostalZone
            self._mapping['PostalZone'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : Region
            self._mapping['Region'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Seçimli(0..1) : District
            self._mapping['District'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
            # Zorunlu(1): Country
        self._mapping['Country'] = ('cac', Country(), 'Zorunlu(1)', True, False, False, '')
        self._mapping[self._elementTag] = ('cac', initiator, '', False, False, True, '')

    def read_element_by_action(self, event: str, element: ET.Element):
        tag: str = ''
        if element.tag.startswith(self.get_context().get_cac_namespace()):
            tag = element.tag[len(self.get_context().get_cac_namespace()):]
        elif element.tag.startswith(self.get_context().get_cbc_namespace()):
            tag = element.tag[len(self.get_context().get_cbc_namespace()):]
        if self._mapping[tag] is not None:
            if event == 'start' and self._mapping[tag][3]:
                if element.tag.startswith(self.get_context().get_cbc_namespace()):
                    if self._mapping[tag][4]:
                        for key in element.attrib.keys():
                            if self._mapping[key] is not None:
                                self.get_context().set_new_frappe_doc(
                                    self._mapping[key][1], element.attrib.get(key))
                    else:
                        pass
                elif element.tag.startswith(self.get_context().get_cac_namespace()):
                    if self._mapping[tag][2] in ['Zorunlu (1)', 'Seçimli (0..1)']:
                        self.get_context().set_state = self._mapping[tag][1]
                        self.get_context().define_mappings(self._initiatorTag, self)
                        self.get_context().read_element_by_action(event, element)
                    elif self._mapping[tag][2] in ['Seçimli (0...n)']:
                        pass
            elif event == 'end' and self._mapping[tag][5]:
                if element.tag.startswith(self.get_context().get_cbc_namespace()):
                    if self._mapping[tag][2] in ['Zorunlu (1)', 'Seçimli (0..1)']:
                        self.get_context().set_new_frappe_doc(
                            self._mapping[tag][1], element.text)
                    elif self._mapping[tag][2] in ['Seçimli (0...n)']:
                        if self.get_context().get_new_frappe_doc(self)[self._mapping[tag][1]] is None:
                            self.get_context().set_new_frappe_doc(
                                self._mapping[tag][1], {self._mapping[tag][6]: element.text})
                        else:
                            self.get_context().append_new_frappe_doc_field(
                                self._mapping[tag][1], {self._mapping[tag][6]: element.text})
                elif element.tag.startswith(self.get_context().get_cac_namespace()):
                    self.get_context().set_state = self._mapping[tag][1]
