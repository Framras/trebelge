from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLDespatchLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DespatchLine'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text}
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Zorunlu(1)')
        orderlinereference_: Element = element.find('./' + cacnamespace + 'OrderLineReference')
        strategy: TRUBLCommonElement = TRUBLOrderLineReference()
        self._strategyContext.set_strategy(strategy)
        frappedoc['orderlinereference'] = [self._strategyContext.return_element_data(orderlinereference_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)]
        # ['Item'] = ('cac', 'Item', 'Zorunlu(1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        strategy: TRUBLCommonElement = TRUBLItem()
        self._strategyContext.set_strategy(strategy)
        frappedoc['item'] = [self._strategyContext.return_element_data(item_,
                                                                       cbcnamespace,
                                                                       cacnamespace)]
        # ['DeliveredQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OutstandingQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['DeliveredQuantity', 'OutstandingQuantity', 'OversupplyQuantity']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_:
                frappedoc[field_.tag.lower()] = field_.text
                frappedoc[field_.tag.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Note'] = ('cbc', '', 'Seçimli(0..n)')
        notes_: list = element.findall('./' + cbcnamespace + 'Note')
        if notes_:
            note: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for note_ in notes_:
                note.append(self._strategyContext.return_element_data(note_,
                                                                      cbcnamespace,
                                                                      cacnamespace))
            frappedoc['note'] = note
        # ['OutstandingReason'] = ('cbc', '', 'Seçimli(0..n)')
        outstandingreasons_: list = element.findall('./' + cbcnamespace + 'Description')
        if outstandingreasons_:
            outstandingreason: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for outstandingreason_ in outstandingreasons_:
                outstandingreason.append(self._strategyContext.return_element_data(outstandingreason_,
                                                                                   cbcnamespace,
                                                                                   cacnamespace))
            frappedoc['outstandingreason'] = outstandingreason
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli(0..n)')
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli(0..n)')
        cacsecimli0n: list = \
            [{'Tag': 'Shipment', 'strategy': TRUBLShipment(), 'fieldName': 'shipment'},
             {'Tag': 'DocumentReference', 'strategy': TRUBLDocumentReference(), 'fieldName': 'documentreference'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall('./' + cacnamespace + element_.get('Tag'))
            if tagelements_:
                tagelements: list = []
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                for tagelement in tagelements_:
                    tagelements.append(self._strategyContext.return_element_data(tagelement,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
