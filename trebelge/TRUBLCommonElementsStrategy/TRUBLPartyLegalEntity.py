from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCorporateRegistrationScheme import TRUBLCorporateRegistrationScheme


class TRUBLPartyLegalEntity(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR PartyLegalEntity'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty
        frappedoc: dict = {}
        # ['RegistrationName'] = ('cbc', 'registrationname', 'Seçimli (0...1)')
        # ['CompanyID'] = ('cbc', 'companyid', 'Seçimli (0...1)')
        # ['RegistrationDate'] = ('cbc', 'registrationdate', 'Seçimli (0...1)')
        # ['SolePrioprietorshipIndicator'] = ('cbc', 'soleprioprietorshipindicator', 'Seçimli (0...1)')
        # ['FullyPaidSharesIndicator'] = ('cbc', 'fullypaidsharesindicator', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RegistrationName', 'CompanyID', 'RegistrationDate', 'SolePrioprietorshipIndicator',
                              'FullyPaidSharesIndicator']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['CorporateStockAmount'] = ('cbc', 'corporatestockamount', 'Seçimli (0...1)')
        corporatestockamount_: Element = element.find('./' + cbcnamespace + 'CorporateStockAmount')
        if corporatestockamount_ is not None:
            if corporatestockamount_.text is not None:
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
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_ is not None:
                tmp = element_.get('strategy').process_element(tagelement_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    frappedoc[element_.get('fieldName')] = tmp.name
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)
