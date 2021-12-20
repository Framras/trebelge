from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLPrice(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Price'

    def process_element(self, element: Element, cbcnamespace: str, **kwargs) -> Document:
        # self._mapping['PriceAmount'] = ('cbc', '', 'Zorunlu(1)')
        # self._mapping['currencyID'] = ('', '', 'Zorunlu(1)')
        priceamount = element.find(cbcnamespace + 'PriceAmount')
        frappedoc: dict = {'priceamount': priceamount.text,
                           'priceamountcurrencyid': priceamount.attrib.get('currencyID')
                           }

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
