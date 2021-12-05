from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyIdentification import TRUBLPartyIdentification
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyLegalEntity import TRUBLPartyLegalEntity
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyName import TRUBLPartyName
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyTaxScheme import TRUBLPartyTaxScheme
from trebelge.TRUBLCommonElementsStrategy.TRUBLPerson import TRUBLPerson


class TRUBLParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Party'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        party: dict = {}
        # ['PartyIdentification'] = ('cac', PartyIdentification(), 'Zorunlu (1...n)', partyidentification)
        partyidentifications_ = element.findall(cacnamespace + 'PartyIdentification')
        strategy: TRUBLCommonElement = TRUBLPartyIdentification()
        self._strategyContext.set_strategy(strategy)
        partyidentifications: list = []
        for partyidentification in partyidentifications_:
            partyidentifications.append(
                frappe.get_doc(
                    'UBL TR PartyIdentification',
                    self._strategyContext.return_element_data(partyidentification,
                                                              cbcnamespace,
                                                              cacnamespace)[0]['name']))
        party['partyidentification'] = partyidentifications

        # ['PostalAddress'] = ('cac', Address(), 'Zorunlu (1)', 'postaladdress')
        postaladdress_ = element.find(cacnamespace + 'PostalAddress')
        strategy: TRUBLCommonElement = TRUBLAddress()
        self._strategyContext.set_strategy(strategy)
        party['postaladdress'] = [frappe.get_doc(
            'UBL TR Address',
            self._strategyContext.return_element_data(postaladdress_, cbcnamespace,
                                                      cacnamespace)[0]['name'])]

        # ['WebsiteURI'] = ('cbc', 'websiteuri', 'Seçimli (0...1)')
        # ['EndpointID'] = ('cbc', 'endpointid', 'Seçimli (0...1)')
        # ['IndustryClassificationCode'] = ('cbc', 'industryclassificationcode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['WebsiteURI', 'EndpointID', 'IndustryClassificationCode']
        for elementtag_ in cbcsecimli01:
            field_ = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                party[field_.tag.lower()] = field_.text

        # ['PartyName'] = ('cac', PartyName(), 'Seçimli (0...1)', partyname)
        # ['PhysicalLocation'] = ('cac', Location(), 'Seçimli (0...1)', 'physicallocation')
        # ['PartyTaxScheme'] = ('cac', TaxScheme(), 'Seçimli (0...1)', 'partytaxscheme')
        # ['Contact'] = ('cac', Contact(), 'Seçimli (0...1)', 'contact')
        # ['Person'] = ('cac', Person(), 'Seçimli (0...1)', 'person')
        # ['AgentParty'] = ('cac', Party(), 'Seçimli (0...1)', 'agentparty')
        cacsecimli01: list = \
            [{'Tag': 'PartyName', 'strategy': TRUBLPartyName(), 'docType': 'UBL TR Party', 'fieldName': 'partyname'},
             {'Tag': 'PhysicalLocation', 'strategy': TRUBLLocation(), 'docType': 'UBL TR Location',
              'fieldName': 'physicallocation'},
             {'Tag': 'PartyTaxScheme', 'strategy': TRUBLPartyTaxScheme(), 'docType': 'UBL TR PartyTaxScheme',
              'fieldName': 'partytaxscheme'},
             {'Tag': 'Contact', 'strategy': TRUBLContact(), 'docType': 'UBL TR Contact', 'fieldName': 'contact'},
             {'Tag': 'Person', 'strategy': TRUBLPerson(), 'docType': 'UBL TR Person',
              'fieldName': 'person'},
             {'Tag': 'AgentParty', 'strategy': TRUBLParty(), 'docType': 'UBL TR Party',
              'fieldName': 'agentparty'}
             ]
        for element_ in cacsecimli01:
            tagelement_ = element.find(cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                party[element_.get('fieldName')] = [frappe.get_doc(
                    element_.get('docType'),
                    self._strategyContext.return_element_data(tagelement_, cbcnamespace,
                                                              cacnamespace)[0]['name'])]

        # ['PartyLegalEntity'] = ('cac', PartyLegalEntity(), 'Seçimli (0...n)', 'partylegalentity')
        partylegalentity_ = element.find(cacnamespace + 'PartyLegalEntity')
        if partylegalentity_ is not None:
            strategy: TRUBLCommonElement = TRUBLPartyLegalEntity()
            self._strategyContext.set_strategy(strategy)
            partylegalentities: list = []
            for partylegalentity in partylegalentity_:
                partylegalentities.append(
                    frappe.get_doc(
                        'UBL TR PartyLegalEntity',
                        self._strategyContext.return_element_data(partylegalentity,
                                                                  cbcnamespace,
                                                                  cacnamespace)[0]['name']))
            party['partylegalentity'] = partylegalentities

        if not frappe.get_all(self._frappeDoctype, filters=party):
            pass
        else:
            newparty = party
            newparty['doctype'] = self._frappeDoctype
            _frappeDoc = frappe.get_doc(newparty)
            _frappeDoc.insert()

        return frappe.get_all(self._frappeDoctype, filters=party)
