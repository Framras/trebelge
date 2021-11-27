from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyIdentification import TRUBLPartyIdentification
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyName import TRUBLPartyName


class TRUBLParty(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['WebsiteURI'] = ('cbc', 'websiteuri', 'Seçimli (0...1)')
        ['EndpointID'] = ('cbc', 'endpointid', 'Seçimli (0...1)')
        ['IndustryClassificationCode'] = ('cbc', 'industryclassificationcode', 'Seçimli (0...1)')
        ['PartyIdentification'] = ('cac', PartyIdentification(), 'Zorunlu (1...n)', partyidentification)
        ['PartyName'] = ('cac', PartyName(), 'Seçimli (0...1)', partyname)
        ['PostalAddress'] = ('cac', Address(), 'Zorunlu (1)')
        ['PhysicalLocation'] = ('cac', Location(), 'Seçimli (0...1)')
        ['PartyTaxScheme'] = ('cac', TaxScheme(), 'Seçimli (0...1)')
        ['PartyLegalEntity'] = ('cac', PartyLegalEntity(), 'Seçimli (0...n)')
        ['Contact'] = ('cac', Contact(), 'Seçimli (0...1)')
        ['Person'] = ('cac', Person(), 'Seçimli (0...1)')
        ['AgentParty'] = ('cac', Party(), 'Seçimli (0...1)')
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

        return party
