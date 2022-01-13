from xml.etree.ElementTree import Element

import frappe
from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLLocation import TRUBLLocation
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyLegalEntity import TRUBLPartyLegalEntity
from trebelge.TRUBLCommonElementsStrategy.TRUBLPartyTaxScheme import TRUBLPartyTaxScheme
from trebelge.TRUBLCommonElementsStrategy.TRUBLPerson import TRUBLPerson


class TRUBLParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Party'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc = dict()
        # ['PostalAddress'] = ('cac', Address(), 'Zorunlu (1)', 'postaladdress')
        postaladdress_: Element = element.find('./' + cacnamespace + 'PostalAddress')
        tmp = TRUBLAddress().process_element(postaladdress_, cbcnamespace, cacnamespace)
        if tmp is not None:
            frappedoc['postaladdress'] = tmp.name
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
            partyname_: Element = tagelement_.find('./' + cbcnamespace + 'Name')
            if partyname_ is not None and partyname_.text is not None:
                frappedoc['partyname'] = partyname_.text
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
        partyidentifications = list()
        partyidentifications_: list = element.findall('./' + cacnamespace + 'PartyIdentification')
        for partyidentification in partyidentifications_:
            partyidentification_: Element = partyidentification.find('./' + cbcnamespace + 'ID')
            if partyidentification_ is not None and partyidentification_.text is not None:
                partyidentifications.append(dict(id=partyidentification_.text,
                                                 schemeid=partyidentification_.attrib.get('schemeID')))
        # ['PartyLegalEntity'] = ('cac', PartyLegalEntity(), 'Seçimli (0...n)', 'partylegalentity')
        partylegalentities = list()
        partylegalentity_: list = element.findall('./' + cacnamespace + 'PartyLegalEntity')
        if len(partylegalentity_) != 0:
            for partylegalentity in partylegalentity_:
                tmp = TRUBLPartyLegalEntity().process_element(partylegalentity, cbcnamespace, cacnamespace)
                if tmp is not None:
                    partylegalentities.append(tmp)
        if frappedoc == {}:
            if len(partyidentifications) != 0:
                frappedoc['partyidentification'] = partyidentifications
            if len(partylegalentities) != 0:
                frappedoc['partylegalentity'] = partylegalentities
            if frappedoc != {}:
                return self._get_frappedoc(self._frappeDoctype, frappedoc, False)

        if len(frappe.get_all(self._frappeDoctype, filters=frappedoc)) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            for partyidentification_ in partyidentifications:
                doc_append = document.append("partyidentification", {})
                doc_append.id = partyidentification_.get('id')
                doc_append.schemeid = partyidentification_.get('schemeid')
                document.save()
            if len(partylegalentities) != 0:
                document.partylegalentity = partylegalentities
                document.save()
            return document

        if len(frappe.get_all(self._frappeDoctype, filters=frappedoc)) == 1:
            legacy_: Document = frappe.get_doc(self._frappeDoctype,
                                               frappe.get_all(self._frappeDoctype,
                                                              filters=frappedoc)[0]["name"])
            partyid: bool = False
            partylegal: bool = False
            if len(partyidentifications) != 0 and \
                    len(legacy_.partyidentification) != 0 and \
                    len(legacy_.partyidentification) == len(partyidentifications):
                for pid in legacy_.partyidentification:
                    if partyidentifications.count(dict(id=pid.id,
                                                       schemeid=pid.schemeID)) != 0:
                        frappedoc['partyidentification'] = partyidentifications
                    else:
                        partyid = True
            if len(partylegalentities) != 0 and \
                    len(legacy_.partylegalentity) != 0 and \
                    len(legacy_.partylegalentity) == len(partylegalentities):
                tmpple = list()
                for entity in partylegalentities:
                    tmpple.append(entity.name)
                for ple in legacy_.partylegalentity:
                    if tmpple.count(ple.name) != 0:
                        frappedoc['partylegalentity'] = partylegalentities
                    else:
                        partylegal = True
            if partyid and partylegal:
                return legacy_
            return self._get_frappedoc(self._frappeDoctype, frappedoc, False)
