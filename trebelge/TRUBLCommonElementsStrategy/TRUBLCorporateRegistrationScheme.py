from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLCorporateRegistrationScheme(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        # ['CorporateRegistrationTypeCode'] = ('cbc', 'corporateregistrationtypecode', 'Seçimli (0...1)')
        # ['JurisdictionRegionAddress'] = ('cac', 'Address()', 'Seçimli(0..n)', 'jurisdictionregionaddresses')
        frappedoc: dict = {}
        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            frappedoc[('CorporateRegistrationScheme' + 'ID').lower()] = id_.text
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc[('CorporateRegistrationScheme' + 'Name').lower()] = name_.text
        corporateregistrationtypecode_ = element.find(cbcnamespace + 'CorporateRegistrationTypeCode')
        if corporateregistrationtypecode_ is not None:
            frappedoc[
                corporateregistrationtypecode_.tag.lower()] = corporateregistrationtypecode_.text
        jurisdictionregionaddress_ = element.find(cacnamespace + 'JurisdictionRegionAddress')
        if jurisdictionregionaddress_ is not None:
            strategy: TRUBLCommonElement = TRUBLAddress()
            self._strategyContext.set_strategy(strategy)
            addresses = self._strategyContext.return_element_data(jurisdictionregionaddress_, cbcnamespace,
                                                                  cacnamespace)
            addresses_: list = []
            for address in addresses:
                addresses_.append(address)
            frappedoc['jurisdictionregionaddresses'] = addresses_

        return self.get_frappedoc(self._frappeDoctype, frappedoc)
