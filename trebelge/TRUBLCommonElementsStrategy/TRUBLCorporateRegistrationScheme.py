from xml.etree.ElementTree import Element

from apps.frappe.frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLCorporateRegistrationScheme(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CorporateRegistrationScheme'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        id_: Element = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            frappedoc['id'] = id_.text
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            frappedoc['corporateregistrationschemename'] = name_.text
        # ['CorporateRegistrationTypeCode'] = ('cbc', 'corporateregistrationtypecode', 'Seçimli (0...1)')
        corporateregistrationtypecode_: Element = element.find(cbcnamespace + 'CorporateRegistrationTypeCode')
        if corporateregistrationtypecode_ is not None:
            frappedoc['corporateregistrationtypecode'] = corporateregistrationtypecode_.text
        # ['JurisdictionRegionAddress'] = ('cac', 'Address()', 'Seçimli(0..n)', 'jurisdictionregionaddress')
        jurisdictionregionaddress_: list = element.findall(cacnamespace + 'JurisdictionRegionAddress')
        if jurisdictionregionaddress_ is not None:
            addresses: list = []
            strategy: TRUBLCommonElement = TRUBLAddress()
            self._strategyContext.set_strategy(strategy)
            for address_ in jurisdictionregionaddress_:
                addresses.append(self._strategyContext.return_element_data(address_,
                                                                           cbcnamespace,
                                                                           cacnamespace))
            frappedoc['jurisdictionregionaddress'] = addresses

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
