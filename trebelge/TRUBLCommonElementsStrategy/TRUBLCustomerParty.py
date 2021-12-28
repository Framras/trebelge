from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLCustomerParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CustomerParty'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = element.find('./' + cacnamespace + 'Party')
        frappedoc['party'] = TRUBLParty.process_element(party_,
                                                        cbcnamespace,
                                                        cacnamespace)
        # ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
        deliverycontact_: Element = element.find('./' + cacnamespace + 'DeliveryContact')
        if deliverycontact_ is not None:
            frappedoc['deliverycontact'] = TRUBLContact.process_element(deliverycontact_,
                                                                        cbcnamespace,
                                                                        cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
