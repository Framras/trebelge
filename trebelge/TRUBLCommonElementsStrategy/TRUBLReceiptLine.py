from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLReceiptLine(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', '', 'Zorunlu (1)')
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text}
        # ['RejectReasonCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ReceivedDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaintCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaint'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RejectReasonCode', 'ReceivedDate', 'TimingComplaintCode', 'TimingComplaint']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['ReceivedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ShortQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RejectedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        cbcqtysecimli01: list = ['ReceivedQuantity', 'ShortQuantity', 'RejectedQuantity', 'OversupplyQuantity']
        for elementtag_ in cbcqtysecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
                frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Note'] = ('cbc', '', 'Seçimli (0...n)')
        notes_: list = element.findall('./' + cbcnamespace + 'Note')
        if notes_ is not None:
            note: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for note_ in notes_:
                note.append(self._strategyContext.return_element_data(note_,
                                                                      cbcnamespace,
                                                                      cacnamespace))
            frappedoc['note'] = note
        # ['RejectReason'] = ('cbc', '', 'Seçimli (0...n)')
        rejectreasons_: list = element.findall('./' + cbcnamespace + 'RejectReason')
        if rejectreasons_ is not None:
            rejectreason: list = []
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for rejectreason_ in rejectreasons_:
                rejectreason.append(self._strategyContext.return_element_data(rejectreason_,
                                                                              cbcnamespace,
                                                                              cacnamespace))
            frappedoc['rejectreason'] = rejectreason
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        strategy: TRUBLCommonElement = TRUBLItem()
        self._strategyContext.set_strategy(strategy)
        frappedoc['item'] = [self._strategyContext.return_element_data(item_,
                                                                       cbcnamespace,
                                                                       cacnamespace)]
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...1)')
        orderlinereference_: Element = element.find('./' + cacnamespace + 'OrderLineReference')
        strategy: TRUBLCommonElement = TRUBLOrderLineReference()
        self._strategyContext.set_strategy(strategy)
        frappedoc['orderlinereference'] = [self._strategyContext.return_element_data(orderlinereference_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace)]
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...1)')
        linereference_: Element = element.find('./' + cacnamespace + 'DespatchLineReference')
        strategy: TRUBLCommonElement = TRUBLLineReference()
        self._strategyContext.set_strategy(strategy)
        frappedoc['linereference'] = [self._strategyContext.return_element_data(linereference_,
                                                                                cbcnamespace,
                                                                                cacnamespace)]
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)')
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...n)')
        cacsecimli0n: list = \
            [{'Tag': 'Shipment', 'strategy': TRUBLShipment(), 'fieldName': 'shipment'},
             {'Tag': 'DocumentReference', 'strategy': TRUBLDocumentReference(), 'fieldName': 'documentreference'}
             ]
        for element_ in cacsecimli0n:
            tagelements_: list = element.findall('./' + cacnamespace + element_.get('Tag'))
            if tagelements_ is not None:
                tagelements: list = []
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                for tagelement in tagelements_:
                    tagelements.append(self._strategyContext.return_element_data(tagelement,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
