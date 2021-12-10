from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLFinancialInstitution(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        # ['Name'] = ('cbc', 'name', 'Seçimli(0..1)')
        financialInstitution: dict = {}
        name_ = element.find(cbcnamespace + 'Name')
        if name_ is not None:
            financialInstitution['financialinstitutionname'] = name_.text

        return financialInstitution
