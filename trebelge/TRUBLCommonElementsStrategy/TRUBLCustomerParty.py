from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLCustomerParty(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> list:
        customerparty: dict = {}
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'customerparty')
        party_ = element.find(cacnamespace + 'Party')
        strategy: TRUBLCommonElement = TRUBLParty()
        self._strategyContext.set_strategy(strategy)
        party = self._strategyContext.return_element_data(party_, cbcnamespace, cacnamespace)
        for key in party.keys():
            customerparty['party_' + key] = party.get(key)
        # ['DeliveryContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'deliverycontact')
        deliverycontact_ = element.find(cacnamespace + 'DeliveryContact')
        if deliverycontact_ is not None:
            strategy: TRUBLCommonElement = TRUBLContact()
            self._strategyContext.set_strategy(strategy)
            deliverycontact = self._strategyContext.return_element_data(deliverycontact_, cbcnamespace, cacnamespace)
            for key in deliverycontact.keys():
                customerparty['deliverycontact_' + key] = deliverycontact.get(key)

        return customerparty
