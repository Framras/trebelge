from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLFinancialInstitution(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR FinancialInstitution'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Name'] = ('cbc', 'name', 'Seçimli(0..1)', 'financialinstitution')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is None or name_.text.strip() == '':
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(financialinstitution=name_.text))

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
