from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLContact import TRUBLContact
from trebelge.TRUBLCommonElementsStrategy.TRUBLParty import TRUBLParty


class TRUBLSupplierParty(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR SupplierParty'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['Party'] = ('cac', 'Party()', 'Zorunlu(1)', 'party')
        party_: Element = element.find(cacnamespace + 'Party')
        strategy: TRUBLCommonElement = TRUBLParty()
        self._strategyContext.set_strategy(strategy)
        frappedoc['party'] = self._strategyContext.return_element_data(party_,
                                                                       cbcnamespace,
                                                                       cacnamespace)
        # ['DespatchContact'] = ('cac', 'Contact()', 'Seçimli(0..1)', 'despatchcontact')
        despatchcontact_: Element = element.find(cacnamespace + 'DespatchContact')
        if despatchcontact_:
            strategy: TRUBLCommonElement = TRUBLContact()
            self._strategyContext.set_strategy(strategy)
            frappedoc['despatchcontact'] = self._strategyContext.return_element_data(despatchcontact_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
