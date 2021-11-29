from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLSupplierParty(TRUBLCommonElement):
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        supplierparty: dict = {}
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_ = element.find(cacnamespace + 'Party')
        strategy: TRUBLCommonElement = TRUBLParty()
        self._strategyContext.set_strategy(strategy)
        party = self._strategyContext.return_element_data(party_, cbcnamespace, cacnamespace)
        for key in party.keys():
            supplierparty['party_' + key] = party.get(key)
        # ['DespatchContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'despatchcontact')
        despatchcontact_ = element.find(cacnamespace + 'DespatchContact')
        if despatchcontact_ is not None:
            strategy: TRUBLCommonElement = TRUBLContact()
            self._strategyContext.set_strategy(strategy)
            despatchcontact = self._strategyContext.return_element_data(despatchcontact_, cbcnamespace, cacnamespace)
            for key in despatchcontact.keys():
                supplierparty['despatchcontact_' + key] = despatchcontact.get(key)

        return supplierparty
