from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLLineReference import TRUBLLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLReceiptLine(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'

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
        if len(notes_) != 0:
            note: list = []
            for note_ in notes_:
                note.append(TRUBLNote().process_element(note_,
                                                        cbcnamespace,
                                                        cacnamespace))
            frappedoc['note'] = note
        # ['RejectReason'] = ('cbc', '', 'Seçimli (0...n)')
        rejectreasons_: list = element.findall('./' + cbcnamespace + 'RejectReason')
        if len(rejectreasons_) != 0:
            rejectreason: list = []
            for rejectreason_ in rejectreasons_:
                rejectreason.append(TRUBLNote().process_element(rejectreason_,
                                                                cbcnamespace,
                                                                cacnamespace))
            frappedoc['rejectreason'] = rejectreason
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        frappedoc['item'] = TRUBLItem().process_element(item_,
                                                        cbcnamespace,
                                                        cacnamespace).name
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...1)')
        orderlinereference_: Element = element.find('./' + cacnamespace + 'OrderLineReference')
        frappedoc['orderlinereference'] = TRUBLOrderLineReference().process_element(orderlinereference_,
                                                                                    cbcnamespace,
                                                                                    cacnamespace).name
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...1)')
        linereference_: Element = element.find('./' + cacnamespace + 'DespatchLineReference')
        frappedoc['linereference'] = TRUBLLineReference().process_element(linereference_,
                                                                          cbcnamespace,
                                                                          cacnamespace).name
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...n)')
        shipments_: list = element.findall('./' + cacnamespace + 'Shipment')
        if len(shipments_) != 0:
            shipments: list = []
            for shipment_ in shipments_:
                shipments.append(TRUBLShipment().process_element(shipment_,
                                                                 cbcnamespace,
                                                                 cacnamespace))
            document.shipment = shipments
            document.save()
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)')
        documentreferences_: list = element.findall('./' + cacnamespace + 'DocumentReference')
        if len(documentreferences_) != 0:
            documentreferences: list = []
            for documentreference_ in documentreferences_:
                documentreferences.append(TRUBLDocumentReference().process_element(documentreference_,
                                                                                   cbcnamespace,
                                                                                   cacnamespace))
            document.documentreference = documentreferences
            document.save()

        return document
