from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxSubtotal import TRUBLTaxSubtotal


class TRUBLTaxTotal(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR TaxTotal'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
        # ['currencyID'] = ('', 'taxamount_currencyid', 'Zorunlu(1)')
        taxamount_: Element = element.find(cbcnamespace + 'TaxAmount')
        frappedoc: dict = {'taxamount': taxamount_.text,
                           'taxamountcurrencyid': taxamount_.attrib.get('currencyID')}
        # ['TaxSubtotal'] = ('cac', 'taxsubtotals', 'Zorunlu(1..n)', 'taxsubtotal')
        strategy: TRUBLCommonElement = TRUBLTaxSubtotal()
        self._strategyContext.set_strategy(strategy)
        taxsubtotals: list = []
        for taxsubtotal in element.findall(cacnamespace + 'TaxSubtotal'):
            taxsubtotal_ = self._strategyContext.return_element_data(taxsubtotal,
                                                                     cbcnamespace,
                                                                     cacnamespace)
            taxsubtotals.append(taxsubtotal_)
        frappedoc['taxsubtotal'] = taxsubtotals

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
