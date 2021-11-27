from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCorporateRegistrationScheme import TRUBLCorporateRegistrationScheme
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLPartyLegalEntity(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        ['RegistrationDate'] = ('cbc', 'registrationdate', 'Seçimli (0...1)')
        ['SolePrioprietorshipIndicator'] = ('cbc', 'soleprioprietorshipindicator', 'Seçimli (0...1)')
        ['CorporateStockAmount'] = ('cbc', 'corporatestockamount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'corporatestockamount_currencyid', 'Zorunlu(1)')
        ['FullyPaidSharesIndicator'] = ('cbc', 'fullypaidsharesindicator', 'Seçimli (0...1)')
        ['CorporateRegistrationScheme'] = ('cac', 'CorporateRegistrationScheme()', 'Seçimli (0...1)',
                            'corporateregistrationscheme')
        ['HeadOfficeParty'] = ('cac', 'Party()', 'Seçimli (0...1)', 'headofficeparty')
        """
        partylegalentity: dict = {}
        registrationname_ = element.find(cbcnamespace + 'RegistrationName')
        if registrationname_ is not None:
            partylegalentity[registrationname_.tag.lower()] = registrationname_.text
        companyid_ = element.find(cbcnamespace + 'CompanyID')
        if companyid_ is not None:
            partylegalentity[companyid_.tag.lower()] = companyid_.text
        registrationdate_ = element.find(cbcnamespace + 'RegistrationDate')
        if registrationdate_ is not None:
            partylegalentity[registrationdate_.tag.lower()] = registrationdate_.text
        soleprioprietorshipindicator_ = element.find(cbcnamespace + 'SolePrioprietorshipIndicator')
        if soleprioprietorshipindicator_ is not None:
            partylegalentity[soleprioprietorshipindicator_.tag.lower()] = soleprioprietorshipindicator_.text
        corporatestockamount_ = element.find(cbcnamespace + 'CorporateStockAmount')
        if corporatestockamount_ is not None:
            partylegalentity[corporatestockamount_.tag.lower()] = corporatestockamount_.text
            partylegalentity[corporatestockamount_.tag.lower() + '_currencyid'] = corporatestockamount_.attrib.get(
                'currencyID')
        fullypaidsharesindicator_ = element.find(cbcnamespace + 'FullyPaidSharesIndicator')
        if fullypaidsharesindicator_ is not None:
            partylegalentity[fullypaidsharesindicator_.tag.lower()] = fullypaidsharesindicator_.text
        corporateregistrationscheme_ = element.find(cacnamespace + 'CorporateRegistrationScheme')
        if corporateregistrationscheme_ is not None:
            strategy: TRUBLCommonElement = TRUBLCorporateRegistrationScheme()
            self._strategyContext.set_strategy(strategy)
            corporateregistrationscheme = self._strategyContext.return_element_data(corporateregistrationscheme_,
                                                                                    cbcnamespace, cacnamespace)
            for key in corporateregistrationscheme.keys():
                partylegalentity['corporateregistrationscheme_' + key] = corporateregistrationscheme.get(key)
        headofficeparty_ = element.find(cacnamespace + 'HeadOfficeParty')
        if headofficeparty_ is not None:
            strategy: TRUBLCommonElement = TRUBLParty()
            self._strategyContext.set_strategy(strategy)
            headofficeparty = self._strategyContext.return_element_data(headofficeparty_, cbcnamespace, cacnamespace)
            for key in headofficeparty.keys():
                partylegalentity['headofficeparty_' + key] = headofficeparty.get(key)

        return partylegalentity
