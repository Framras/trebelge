# from __future__ import annotations

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class Party(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'
    _mapping = dict()
    _elementTag: str = 'Party'
    _invoiceElementTag: str = 'AccountingSupplierParty'
    _despatchElementTag: str = 'DespatchSupplierParty'
    _initiatorTag: str = ''

    def find_ebelge_status(self):
        pass

    def define_mappings(self, tag: str, initiator: AbstractXMLFileState):
        self._initiatorTag = tag
        #         "accountingsupplierparty_partyidentification_schemeid"
        #         "accountingsupplierparty_partyidentificationid"
        #         "accountingsupplierparty_partyname"
        #         "accountingsupplierparty_postaladdress_id"
        #         "accountingsupplierparty_postaladdress_postbox"
        #         "accountingsupplierparty_postaladdress_room"
        #         "accountingsupplierparty_postaladdress_streetname"
        #         "accountingsupplierparty_postaladdress_blockname"
        #         "accountingsupplierparty_postaladdress_buildingname"
        #         "accountingsupplierparty_postaladdress_buildingnumber"
        #         "accountingsupplierparty_postaladdress_citysubdivisionname"
        #         "accountingsupplierparty_postaladdress_cityname"
        #         "accountingsupplierparty_postaladdress_postalzone"
        #         "accountingsupplierparty_postaladdress_region"
        #         "accountingsupplierparty_postaladdress_district"
        #         "accountingsupplierparty_postaladdress_country"
        if tag == self._invoiceElementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Seçimli(0..1): WebsiteURI
            self._mapping['WebsiteURI'] = (
                'cbc', 'accountingsupplierparty_websiteuri', 'Seçimli (0...1)', False, False, True)
            self._mapping['EndpointID'] = (
                'cbc', 'accountingsupplierparty_endpointid', 'Seçimli (0...1)', False, False, True)
            # Seçimli(0..1): IndustryClassificationCode
            self._mapping['IndustryClassificationCode'] = (
                'cbc', 'accountingsupplierparty_industryclassificationcode', 'Seçimli (0...1)', False, False, True)
            # Zorunlu(1..n): PartyIdentification
            self._mapping['PartyIdentification'] = ('cac', 'PartyIdentification', 'Zorunlu (1...n)', True, False, False)
            # Seçimli(0..1): PartyName
            self._mapping['PartyName'] = ('cac', 'PartyName', 'Seçimli (0...1)', True, False, False)
            # Zorunlu(1): PostalAddress:Address
            self._mapping['PostalAddress'] = ('cac', 'Address', 'Zorunlu (1)', True, False, False)
            # Seçimli(0..1): PhysicalLocation:Location
            self._mapping['PhysicalLocation'] = ('cac', 'Location', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..1): PartyTaxScheme:TaxScheme
            self._mapping['PartyTaxScheme'] = ('cac', 'TaxScheme', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..n): PartyLegalEntity:PartyLegalEntity
            self._mapping['PartyLegalEntity'] = ('cac', 'PartyLegalEntity', 'Seçimli (0...n)', True, False, False)
            # Seçimli(0..1): Contact:Contact
            self._mapping['Contact'] = ('cac', 'Contact', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..1): Person:Person
            self._mapping['Person'] = ('cac', 'Person', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..1): AgentParty:Party
            self._mapping['AgentParty'] = ('cac', 'Party', 'Seçimli (0...1)', True, False, False)
            self._mapping[self._elementTag] = ('cac', '', '', False, False, True)

            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Seçimli(0..1): WebsiteURI
            self._mapping['WebsiteURI'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
            self._mapping['EndpointID'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
            # Seçimli(0..1): IndustryClassificationCode
            self._mapping['IndustryClassificationCode'] = ('cbc', '', 'Seçimli (0...1)', False, False, True)
            # Zorunlu(1..n): PartyIdentification
            self._mapping['PartyIdentification'] = ('cac', 'PartyIdentification', 'Zorunlu (1...n)', True, False, False)
            # Seçimli(0..1): PartyName
            self._mapping['PartyName'] = ('cac', 'PartyName', 'Seçimli (0...1)', True, False, False)
            # Zorunlu(1): PostalAddress:Address
            self._mapping['PostalAddress'] = ('cac', 'Address', 'Zorunlu (1)', True, False, False)
            # Seçimli(0..1): PhysicalLocation:Location
            self._mapping['PhysicalLocation'] = ('cac', 'Location', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..1): PartyTaxScheme:TaxScheme
            self._mapping['PartyTaxScheme'] = ('cac', 'TaxScheme', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..n): PartyLegalEntity:PartyLegalEntity
            self._mapping['PartyLegalEntity'] = ('cac', 'PartyLegalEntity', 'Seçimli (0...n)', True, False, False)
            # Seçimli(0..1): Contact:Contact
            self._mapping['Contact'] = ('cac', 'Contact', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..1): Person:Person
            self._mapping['Person'] = ('cac', 'Person', 'Seçimli (0...1)', True, False, False)
            # Seçimli(0..1): AgentParty:Party
            self._mapping['AgentParty'] = ('cac', 'Party', 'Seçimli (0...1)', True, False, False)
            self._mapping[self._elementTag] = ('cac', '', '', False, False, True)

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
                        self.get_context().define_mappings(tag, self)
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
