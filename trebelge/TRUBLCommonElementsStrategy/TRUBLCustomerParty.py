from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLCustomerParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR CustomerParty'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = element.find('./' + cacnamespace + 'Party')
        strategy: TRUBLCommonElement = TRUBLParty()
        self._strategyContext.set_strategy(strategy)
        frappedoc['party'] = self._strategyContext.return_element_data(party_,
                                                                       cbcnamespace,
                                                                       cacnamespace)
        # ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
        deliverycontact_: Element = element.find('./' + cacnamespace + 'DeliveryContact')
        if deliverycontact_ is not None:
            strategy: TRUBLCommonElement = TRUBLContact()
            self._strategyContext.set_strategy(strategy)
            frappedoc['deliverycontact'] = self._strategyContext.return_element_data(deliverycontact_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
