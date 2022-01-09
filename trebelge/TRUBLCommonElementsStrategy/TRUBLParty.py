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
        # ['PostalAddress'] = ('cac', Address(), 'Zorunlu (1)', 'postaladdress')
        postaladdress_: Element = element.find('./' + cacnamespace + 'PostalAddress')
        tmp = TRUBLAddress().process_element(postaladdress_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc: dict = dict(postaladdress=tmp.name)
        # ['WebsiteURI'] = ('cbc', 'websiteuri', 'Seçimli (0...1)')
        # ['EndpointID'] = ('cbc', 'endpointid', 'Seçimli (0...1)')
        # ['IndustryClassificationCode'] = ('cbc', 'industryclassificationcode', 'Seçimli (0...1)')
        cbcsecimli01: list = ['WebsiteURI', 'EndpointID', 'IndustryClassificationCode']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['PartyName'] = ('cac', PartyName(), 'Seçimli (0...1)', partyname)
        tagelement_: Element = element.find('./' + cacnamespace + 'PartyName')
        if tagelement_ is not None:
            tmp = TRUBLPartyName().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['partyname'] = tmp.name
        # ['PhysicalLocation'] = ('cac', Location(), 'Seçimli (0...1)', 'physicallocation')
        tagelement_: Element = element.find('./' + cacnamespace + 'PhysicalLocation')
        if tagelement_ is not None:
            tmp = TRUBLLocation().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['physicallocation'] = tmp.name
        # ['PartyTaxScheme'] = ('cac', PartyTaxScheme(), 'Seçimli (0...1)', 'partytaxscheme')
        tagelement_: Element = element.find('./' + cacnamespace + 'PartyTaxScheme')
        if tagelement_ is not None:
            tmp = TRUBLPartyTaxScheme().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['partytaxscheme'] = tmp.name
        # ['Contact'] = ('cac', Contact(), 'Seçimli (0...1)', 'contact')
        tagelement_: Element = element.find('./' + cacnamespace + 'Contact')
        if tagelement_ is not None:
            tmp = TRUBLContact().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['contact'] = tmp.name
        # ['Person'] = ('cac', Person(), 'Seçimli (0...1)', 'person')
        tagelement_: Element = element.find('./' + cacnamespace + 'Person')
        if tagelement_ is not None:
            tmp = TRUBLPerson().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['person'] = tmp.name
        # ['AgentParty'] = ('cac', Party(), 'Seçimli (0...1)', 'agentparty')
        tagelement_: Element = element.find('./' + cacnamespace + 'AgentParty')
        if tagelement_ is not None:
            tmp = TRUBLParty().process_element(tagelement_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['agentparty'] = tmp.name
        # ['PartyIdentification'] = ('cac', PartyIdentification(), 'Zorunlu (1...n)', partyidentification)
        partyidentifications_: list = element.findall('./' + cacnamespace + 'PartyIdentification')
        partyidentifications: list = []
        for partyidentification in partyidentifications_:
            tmp = TRUBLPartyIdentification().process_element(partyidentification, cbcnamespace, cacnamespace)
            if tmp is not None:
                partyidentifications.append(tmp)
        # ['PartyLegalEntity'] = ('cac', PartyLegalEntity(), 'Seçimli (0...n)', 'partylegalentity')
        partylegalentities: list = []
        partylegalentity_: Element = element.find('./' + cacnamespace + 'PartyLegalEntity')
        if partylegalentity_ is not None:
            for partylegalentity in partylegalentity_:
                tmp = TRUBLPartyLegalEntity().process_element(partylegalentity, cbcnamespace, cacnamespace)
                if tmp is not None:
                    partylegalentities.append(tmp)

        if len(partyidentifications) + len(partylegalentities) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(partyidentifications) != 0:
                document.partyidentification = partyidentifications
            if len(partylegalentities) != 0:
                document.partylegalentity = partylegalentities
            document.save()

        return document
