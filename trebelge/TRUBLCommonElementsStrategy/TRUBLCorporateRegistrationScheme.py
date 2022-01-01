from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLAddress import TRUBLAddress
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLCorporateRegistrationScheme(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CorporateRegistrationScheme'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None and id_.text is not None:
            frappedoc['id'] = id_.text
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is not None and name_.text is not None:
            frappedoc['corporateregistrationschemename'] = name_.text
        # ['CorporateRegistrationTypeCode'] = ('cbc', 'corporateregistrationtypecode', 'Seçimli (0...1)')
        corporateregistrationtypecode_: Element = element.find('./' + cbcnamespace + 'CorporateRegistrationTypeCode')
        if corporateregistrationtypecode_ is not None and corporateregistrationtypecode_.text is not None:
            frappedoc['corporateregistrationtypecode'] = corporateregistrationtypecode_.text
        # ['JurisdictionRegionAddress'] = ('cac', 'Address()', 'Seçimli(0..n)', 'jurisdictionregionaddress')
        jurisdictionregionaddress_: list = element.findall('./' + cacnamespace + 'JurisdictionRegionAddress')
        if len(jurisdictionregionaddress_) != 0:
            addresses: list = []
            for address_ in jurisdictionregionaddress_:
                tmp = TRUBLAddress().process_element(address_,
                                                     cbcnamespace,
                                                     cacnamespace)
                if tmp is not None:
                    addresses.append(tmp)
            if len(addresses) != 0:
                if frappedoc != {}:
                    document = self._get_frappedoc(self._frappeDoctype, frappedoc)
                    document.jurisdictionregionaddress = addresses
                    document.save()
                    return document
                else:
                    frappedoc['jurisdictionregionaddress'] = addresses
                    return self._get_frappedoc(self._frappeDoctype, frappedoc)
            else:
                return self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            if frappedoc != {}:
                return None
            else:
                return self._get_frappedoc(self._frappeDoctype, frappedoc)
