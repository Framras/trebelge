from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCorporateRegistrationScheme import TRUBLCorporateRegistrationScheme
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLPartyLegalEntity(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR PartyLegalEntity'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        # ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        # ['RegistrationDate'] = ('cbc', 'registrationdate', 'Seçimli (0...1)')
        # ['SolePrioprietorshipIndicator'] = ('cbc', 'soleprioprietorshipindicator', 'Seçimli (0...1)')
        # ['FullyPaidSharesIndicator'] = ('cbc', 'fullypaidsharesindicator', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RegistrationName', 'CompanyID', 'RegistrationDate', 'SolePrioprietorshipIndicator',
                              'FullyPaidSharesIndicator']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if not field_:
                frappedoc[field_.tag.lower()] = field_.text
        # ['CorporateStockAmount'] = ('cbc', 'corporatestockamount', 'Seçimli (0...1)')
        corporatestockamount_: Element = element.find(cbcnamespace + 'CorporateStockAmount')
        if not corporatestockamount_:
            frappedoc['corporatestockamount'] = corporatestockamount_.text
            frappedoc['corporatestockamountcurrencyid'] = corporatestockamount_.attrib.get('currencyID')
        # ['CorporateRegistrationScheme'] = ('cac', 'CorporateRegistrationScheme()', 'Seçimli (0...1)',
        #                     'corporateregistrationscheme')
        # ['HeadOfficeParty'] = ('cac', 'Party()', 'Seçimli (0...1)', 'headofficeparty')
        cacsecimli01: list = \
            [{'Tag': 'CorporateRegistrationScheme', 'strategy': TRUBLCorporateRegistrationScheme(),
              'fieldName': 'corporateregistrationscheme'},
             {'Tag': 'HeadOfficeParty', 'strategy': TRUBLParty(), 'fieldName': 'headofficeparty'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find(cacnamespace + element_.get('Tag'))
            if not tagelement_:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
