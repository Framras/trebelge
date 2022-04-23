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
        if id_ is not None:
            if id_.text is not None:
                frappedoc['id'] = id_.text.strip()
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is not None:
            if name_.text is not None:
                frappedoc['corporateregistrationschemename'] = name_.text.strip()
        # ['CorporateRegistrationTypeCode'] = ('cbc', 'corporateregistrationtypecode', 'Seçimli (0...1)')
        corporateregistrationtypecode_: Element = element.find('./' + cbcnamespace + 'CorporateRegistrationTypeCode')
        if corporateregistrationtypecode_ is not None:
            if corporateregistrationtypecode_.text is not None:
                frappedoc['corporateregistrationtypecode'] = corporateregistrationtypecode_.text.strip()
        if frappedoc == {}:
            return None
        # ['JurisdictionRegionAddress'] = ('cac', 'Address()', 'Seçimli(0..n)', 'jurisdictionregionaddress')
        jurisdictionregionaddress_: list = element.findall('./' + cacnamespace + 'JurisdictionRegionAddress')
        addresses = list()
        if len(jurisdictionregionaddress_) != 0:
            for address_ in jurisdictionregionaddress_:
                tmp = TRUBLAddress().process_element(address_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    addresses.append(tmp.name)
        if len(addresses) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            doc_append = document.append("jurisdictionregionaddress", {})
            for address in addresses:
                doc_append.addresses = address
                document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
