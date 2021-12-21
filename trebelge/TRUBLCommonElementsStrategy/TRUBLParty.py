from xml.etree.ElementTree import Element

from frappe.model.document import Document
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

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['PartyIdentification'] = ('cac', PartyIdentification(), 'Zorunlu (1...n)', partyidentification)
        partyidentifications_: list = element.findall(cacnamespace + 'PartyIdentification')
        partyidentifications: list = []
        strategy: TRUBLCommonElement = TRUBLPartyIdentification()
        self._strategyContext.set_strategy(strategy)
        for partyidentification in partyidentifications_:
            partyidentifications.append(self._strategyContext.return_element_data(partyidentification,
                                                                                  cbcnamespace,
                                                                                  cacnamespace))
        frappedoc['partyidentification'] = partyidentifications
        # ['PostalAddress'] = ('cac', Address(), 'Zorunlu (1)', 'postaladdress')
        postaladdress_: Element = element.find(cacnamespace + 'PostalAddress')
        strategy: TRUBLCommonElement = TRUBLAddress()
        self._strategyContext.set_strategy(strategy)
        frappedoc['postaladdress'] = [self._strategyContext.return_element_data(postaladdress_,
                                                                                cbcnamespace,
                                                                                cacnamespace)]
        # ['WebsiteURI'] = ('cbc', 'websiteuri', 'Seçimli (0...1)')
        # ['EndpointID'] = ('cbc', 'endpointid', 'Seçimli (0...1)')
        # ['IndustryClassificationCode'] = ('cbc', 'industryclassificationcode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['WebsiteURI', 'EndpointID', 'IndustryClassificationCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text
        # ['PartyName'] = ('cac', PartyName(), 'Seçimli (0...1)', partyname)
        # ['PhysicalLocation'] = ('cac', Location(), 'Seçimli (0...1)', 'physicallocation')
        # ['PartyTaxScheme'] = ('cac', TaxScheme(), 'Seçimli (0...1)', 'partytaxscheme')
        # ['Contact'] = ('cac', Contact(), 'Seçimli (0...1)', 'contact')
        # ['Person'] = ('cac', Person(), 'Seçimli (0...1)', 'person')
        # ['AgentParty'] = ('cac', Party(), 'Seçimli (0...1)', 'agentparty')
        cacsecimli01: list = \
            [{'Tag': 'PartyName', 'strategy': TRUBLPartyName(), 'fieldName': 'partyname'},
             {'Tag': 'PhysicalLocation', 'strategy': TRUBLLocation(), 'fieldName': 'physicallocation'},
             {'Tag': 'PartyTaxScheme', 'strategy': TRUBLPartyTaxScheme(), 'fieldName': 'partytaxscheme'},
             {'Tag': 'Contact', 'strategy': TRUBLContact(), 'fieldName': 'contact'},
             {'Tag': 'Person', 'strategy': TRUBLPerson(), 'fieldName': 'person'},
             {'Tag': 'AgentParty', 'strategy': TRUBLParty(), 'fieldName': 'agentparty'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find(cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]
        # ['PartyLegalEntity'] = ('cac', PartyLegalEntity(), 'Seçimli (0...n)', 'partylegalentity')
        partylegalentity_: Element = element.find(cacnamespace + 'PartyLegalEntity')
        if partylegalentity_ is not None:
            partylegalentities: list = []
            strategy: TRUBLCommonElement = TRUBLPartyLegalEntity()
            self._strategyContext.set_strategy(strategy)
            for partylegalentity in partylegalentity_:
                partylegalentities.append(self._strategyContext.return_element_data(partylegalentity,
                                                                                    cbcnamespace,
                                                                                    cacnamespace))
            frappedoc['partylegalentity'] = partylegalentities

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
