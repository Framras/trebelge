from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyIdentification import TRUBLPartyIdentification
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyLegalEntity import TRUBLPartyLegalEntity
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyName import TRUBLPartyName
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyTaxScheme import TRUBLPartyTaxScheme


class TRUBLParty(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['WebsiteURI'] = ('cbc', 'websiteuri', 'Seçimli (0...1)')
        ['EndpointID'] = ('cbc', 'endpointid', 'Seçimli (0...1)')
        ['IndustryClassificationCode'] = ('cbc', 'industryclassificationcode', 'Seçimli (0...1)')
        ['PartyIdentification'] = ('cac', PartyIdentification(), 'Zorunlu (1...n)', partyidentification)
        ['PartyName'] = ('cac', PartyName(), 'Seçimli (0...1)', partyname)
        ['PostalAddress'] = ('cac', Address(), 'Zorunlu (1)', 'postaladdress')
        ['PhysicalLocation'] = ('cac', Location(), 'Seçimli (0...1)', 'physicallocation')
        ['PartyTaxScheme'] = ('cac', TaxScheme(), 'Seçimli (0...1)', 'partytaxscheme')
        ['PartyLegalEntity'] = ('cac', PartyLegalEntity(), 'Seçimli (0...n)', 'partylegalentities')
        ['Contact'] = ('cac', Contact(), 'Seçimli (0...1)', 'contact')
        ['Person'] = ('cac', Person(), 'Seçimli (0...1)', 'person')
        ['AgentParty'] = ('cac', Party(), 'Seçimli (0...1)', 'agentparty')
        """
        party: dict = {}
        websiteuri_ = element.find(cbcnamespace + 'WebsiteURI')
        if websiteuri_ is not None:
            party[websiteuri_.tag.lower()] = websiteuri_.text
        endpointid_ = element.find(cbcnamespace + 'EndpointID')
        if endpointid_ is not None:
            party[endpointid_.tag.lower()] = endpointid_.text
        industryclassificationcode_ = element.find(cbcnamespace + 'IndustryClassificationCode')
        if industryclassificationcode_ is not None:
            party[industryclassificationcode_.tag.lower()] = industryclassificationcode_.text
        partyidentifications_ = element.findall(cacnamespace + 'PartyIdentification')
        strategy: TRUBLCommonElement = TRUBLPartyIdentification()
        self._strategyContext.set_strategy(strategy)
        partyidentifications: list = []
        for partyidentification in partyidentifications_:
            partyidentifications.append(self._strategyContext.return_element_data(partyidentification, cbcnamespace,
                                                                                  cacnamespace))
        party['partyidentifications'] = partyidentifications
        partyname_ = element.find(cacnamespace + 'PartyName')
        if partyname_ is not None:
            strategy: TRUBLCommonElement = TRUBLPartyName()
            self._strategyContext.set_strategy(strategy)
            partyname = self._strategyContext.return_element_data(partyname_, cbcnamespace,
                                                                  cacnamespace)
            party['partyname'] = partyname.get('partyname')
        postaladdress_ = element.find(cacnamespace + 'PostalAddress')
        strategy: TRUBLCommonElement = TRUBLAddress()
        self._strategyContext.set_strategy(strategy)
        postaladdress = self._strategyContext.return_element_data(postaladdress_, cbcnamespace,
                                                                  cacnamespace)
        for key in postaladdress.keys():
            party['postaladdress_' + key] = postaladdress.get(key)
        party['partyidentifications'] = partyidentifications
        physicallocation_ = element.find(cacnamespace + 'PhysicalLocation')
        if physicallocation_ is not None:
            strategy: TRUBLCommonElement = TRUBLLocation()
            self._strategyContext.set_strategy(strategy)
            location = self._strategyContext.return_element_data(physicallocation_, cbcnamespace,
                                                                 cacnamespace)
            for key in location.keys():
                party['location_' + key] = location.get(key)
        partytaxscheme_ = element.find(cacnamespace + 'PartyTaxScheme')
        if partytaxscheme_ is not None:
            strategy: TRUBLCommonElement = TRUBLPartyTaxScheme()
            self._strategyContext.set_strategy(strategy)
            partytaxscheme = self._strategyContext.return_element_data(partytaxscheme_, cbcnamespace,
                                                                       cacnamespace)
            for key in partytaxscheme.keys():
                party['partytaxscheme_' + key] = partytaxscheme.get(key)
        partylegalentity_ = element.find(cacnamespace + 'PartyLegalEntity')
        if partylegalentity_ is not None:
            strategy: TRUBLCommonElement = TRUBLPartyLegalEntity()
            self._strategyContext.set_strategy(strategy)
            partylegalentities = self._strategyContext.return_element_data(partytaxscheme_, cbcnamespace,
                                                                           cacnamespace)
            partylegalentities_: list = []
            for partylegalentity in partylegalentities:
                partylegalentities_.append(partylegalentity)
            party['partylegalentities'] = partylegalentities_
        contact_ = element.find(cacnamespace + 'Contact')
        person_ = element.find(cacnamespace + 'Person')
        agentparty_ = element.find(cacnamespace + 'AgentParty')

        return party
