from xml.etree.ElementTree import Element

import frappe
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxSubtotal import TRUBLTaxSubtotal


class TRUBLTaxTotal(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()
    _frappeDoctype: str = 'TR UBL Tax Total'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        """
        ['TaxAmount'] = ('cbc', 'taxamount', 'Zorunlu(1)')
        ['currencyID'] = ('', 'taxamount_currencyid', 'Zorunlu(1)')
        ['TaxSubtotal'] = ('cac', 'taxsubtotals', 'Zorunlu(1..n)', 'taxsubtotal')
        """
        taxamount_ = element.find(cbcnamespace + 'TaxAmount')
        taxTotal: dict = {'doctype': self._frappeDoctype,
                          'taxamount': taxamount_.text,
                          'taxamount_currencyid': taxamount_.attrib.get('currencyID')}
        strategy: TRUBLCommonElement = TRUBLTaxSubtotal()
        self._strategyContext.set_strategy(strategy)
        taxsubtotals: list = []
        for taxsubtotal in element.findall(cacnamespace + 'TaxSubtotal'):
            taxsubtotal_ = self._strategyContext.return_element_data(taxsubtotal, cbcnamespace,
                                                                     cacnamespace)
            taxsubtotals.append(taxsubtotal_)
        taxTotal['taxsubtotals'] = taxsubtotals
        newTaxTotal = frappe.get_doc(taxTotal)
        newTaxTotal.db_insert()

        return newTaxTotal.get_value('name')
