from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLCustomerParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CustomerParty'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = element.find('./' + cacnamespace + 'Party')
        tmp = TRUBLParty().process_element(party_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc: dict = dict(party=tmp.name)
        # ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
        deliverycontact_: Element = element.find('./' + cacnamespace + 'DeliveryContact')
        if deliverycontact_ is not None:
            tmp = TRUBLContact().process_element(deliverycontact_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['deliverycontact'] = tmp.name

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
