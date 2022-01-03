from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLBranch import TRUBLBranch
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLFinancialAccount(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR FinancialAccount'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        id_ = element.find('./' + cbcnamespace + 'ID').text
        if id_ is None:
            return None
        frappedoc: dict = {'id': id_}
        # ['CurrencyCode'] = ('cbc', 'currencycode', 'Seçimli (0...1)')
        # ['PaymentNote'] = ('cbc', 'paymentnote', 'Seçimli (0...1)')
        cbcsecimli01: list = ['CurrencyCode', 'PaymentNote']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['FinancialInstitutionBranch'] = ('cac', 'Branch()', 'Seçimli (0...1)', 'financialinstitutionbranch')
        financialinstitutionbranch_: Element = element.find('./' + cacnamespace + 'FinancialInstitutionBranch')
        if financialinstitutionbranch_ is not None:
            tmp = TRUBLBranch().process_element(financialinstitutionbranch_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['financialinstitutionbranch'] = tmp.name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
