from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommunication import TRUBLCommunication
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyIdentification import TRUBLPartyIdentification


class TRUBLParty(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['WebsiteURI'] = ('cbc', 'websiteuri', 'Seçimli (0...1)')
        ['EndpointID'] = ('cbc', 'endpointid', 'Seçimli (0...1)')
        ['IndustryClassificationCode'] = ('cbc', 'industryclassificationcode', 'Seçimli (0...1)')
        ['PartyIdentification'] = ('cac', PartyIdentification(), 'Zorunlu (1...n)', partyidentification)
        ['PartyName'] = ('cac', PartyName(), 'Seçimli (0...1)')
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

        telefax_ = element.find(cbcnamespace + 'Telefax')
        if telefax_ is not None:
            contact[telefax_.tag.lower()] = telefax_.text
        electronicmail_ = element.find(cbcnamespace + 'ElectronicMail')
        if electronicmail_ is not None:
            contact[electronicmail_.tag.lower()] = electronicmail_.text
        note_ = element.find(cbcnamespace + 'Note')
        if note_ is not None:
            contact[note_.tag.lower()] = note_.text
        othercommunications_ = element.findall(cacnamespace + 'OtherCommunication')
        if othercommunications_ is not None:
            strategy: TRUBLCommonElement = TRUBLCommunication()
            self._strategyContext.set_strategy(strategy)
            communications: list = []
            for othercommunication in othercommunications_:
                communication_ = self._strategyContext.return_element_data(othercommunication, cbcnamespace,
                                                                           cacnamespace)
                communications.append(communication_)
            contact['othercommunications'] = communications

        return contact
