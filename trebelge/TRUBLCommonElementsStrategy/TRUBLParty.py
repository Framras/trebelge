from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyIdentification import TRUBLPartyIdentification
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyLegalEntity import TRUBLPartyLegalEntity
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyName import TRUBLPartyName
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyTaxScheme import TRUBLPartyTaxScheme
from trebelge.TRUBLCommonElementsStrategy.TRUBLPerson import TRUBLPerson


class TRUBLParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Party'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['PostalAddress'] = ('cac', Address(), 'Zorunlu (1)', 'postaladdress')
        postaladdress_: Element = element.find('./' + cacnamespace + 'PostalAddress')
        tmp = TRUBLAddress().process_element(postaladdress_,
                                             cbcnamespace,
                                             cacnamespace)
        if tmp is not None:
            frappedoc['postaladdress'] = tmp.name
        # ['WebsiteURI'] = ('cbc', 'websiteuri', 'Seçimli (0...1)')
        # ['EndpointID'] = ('cbc', 'endpointid', 'Seçimli (0...1)')
        # ['IndustryClassificationCode'] = ('cbc', 'industryclassificationcode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['WebsiteURI', 'EndpointID', 'IndustryClassificationCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['PartyName'] = ('cac', PartyName(), 'Seçimli (0...1)', partyname)
        # ['PhysicalLocation'] = ('cac', Location(), 'Seçimli (0...1)', 'physicallocation')
        # ['PartyTaxScheme'] = ('cac', PartyTaxScheme(), 'Seçimli (0...1)', 'partytaxscheme')
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
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                tmp = element_.get('strategy').process_element(tagelement_,
                                                               cbcnamespace,
                                                               cacnamespace)
                if tmp is not None:
                    frappedoc[element_.get('fieldName')] = tmp.name
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['PartyIdentification'] = ('cac', PartyIdentification(), 'Zorunlu (1...n)', partyidentification)
        partyidentifications_: list = element.findall('./' + cacnamespace + 'PartyIdentification')
        partyidentifications: list = []
        for partyidentification in partyidentifications_:
            partyidentifications.append(TRUBLPartyIdentification().process_element(partyidentification,
                                                                                   cbcnamespace,
                                                                                   cacnamespace))
        document.partyidentification = partyidentifications
        document.save()
        # ['PartyLegalEntity'] = ('cac', PartyLegalEntity(), 'Seçimli (0...n)', 'partylegalentity')
        partylegalentity_: Element = element.find('./' + cacnamespace + 'PartyLegalEntity')
        if partylegalentity_ is not None:
            partylegalentities: list = []
            for partylegalentity in partylegalentity_:
                partylegalentities.append(TRUBLPartyLegalEntity().process_element(partylegalentity,
                                                                                  cbcnamespace,
                                                                                  cacnamespace))
            document.partylegalentity = partylegalentities
            document.save()

        return document
