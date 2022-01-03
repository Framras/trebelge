from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPrice(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Price'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # self._mapping['PriceAmount'] = ('cbc', '', 'Zorunlu(1)')
        priceamount = element.find('./' + cbcnamespace + 'PriceAmount')
        if priceamount.text is not None:
            return None
        return self._get_frappedoc(self._frappeDoctype, dict(priceamount=priceamount.text,
                                                             priceamountcurrencyid=priceamount.attrib.get('currencyID')
                                                             ))
