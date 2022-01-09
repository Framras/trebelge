from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLFinancialInstitution import TRUBLFinancialInstitution


class TRUBLBranch(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR Branch'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Name'] = ('cbc', 'branchname', 'Seçimli(0..1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is not None and name_.text is not None:
            frappedoc['branchname'] = name_.text
        # ['FinancialInstitution'] = ('cac', 'FinancialInstitution()', 'Seçimli(0..1)', 'financialinstitution')
        financialinstitution_: Element = element.find('./' + cacnamespace + 'FinancialInstitution')
        if financialinstitution_ is not None:
            tmp = TRUBLFinancialInstitution().process_element(financialinstitution_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['financialinstitution'] = tmp.name
        if frappedoc == {}:
            return None
        return self._get_frappedoc(self._frappeDoctype, frappedoc)
