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
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_.text is None:
            return None
        frappedoc: dict = {'id': id_.text}
        # ['RejectReasonCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ReceivedDate'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaintCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['TimingComplaint'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['RejectReasonCode', 'ReceivedDate', 'TimingComplaintCode', 'TimingComplaint']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['ReceivedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['ShortQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['RejectedQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        cbcqtysecimli01: list = ['ReceivedQuantity', 'ShortQuantity', 'RejectedQuantity', 'OversupplyQuantity']
        for elementtag_ in cbcqtysecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
                    frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Note'] = ('cbc', '', 'Seçimli (0...n)')
        notes_: list = element.findall('./' + cbcnamespace + 'Note')
        if len(notes_) != 0:
            note = list()
            for note_ in notes_:
                tmp = TRUBLNote().process_element(note_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    note.append(tmp)
            if len(note) != 0:
                frappedoc['note'] = note
        # ['RejectReason'] = ('cbc', '', 'Seçimli (0...n)')
        rejectreasons_: list = element.findall('./' + cbcnamespace + 'RejectReason')
        if len(rejectreasons_) != 0:
            rejectreason = list()
            for rejectreason_ in rejectreasons_:
                tmp = TRUBLNote().process_element(rejectreason_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    rejectreason.append(tmp)
            if len(rejectreason) != 0:
                frappedoc['rejectreason'] = rejectreason
        # ['Item'] = ('cac', 'Item', 'Zorunlu (1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        tmp = TRUBLItem().process_element(item_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc['item'] = tmp.name
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Seçimli (0...1)')
        orderlinereference_: Element = element.find('./' + cacnamespace + 'OrderLineReference')
        tmp = TRUBLOrderLineReference().process_element(orderlinereference_, cbcnamespace, cacnamespace)
        if tmp is not None:
            frappedoc['orderlinereference'] = tmp.name
        # ['DespatchLineReference'] = ('cac', 'LineReference', 'Seçimli (0...1)')
        linereference_: Element = element.find('./' + cacnamespace + 'DespatchLineReference')
        tmp = TRUBLLineReference().process_element(linereference_, cbcnamespace, cacnamespace)
        if tmp is not None:
            frappedoc['linereference'] = tmp.name
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli (0...n)')
        shipments = list()
        shipments_: list = element.findall('./' + cacnamespace + 'Shipment')
        if len(shipments_) != 0:
            for shipment_ in shipments_:
                tmp = TRUBLShipment().process_element(shipment_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    shipments.append(tmp)
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)')
        documentreferences = list()
        documentreferences_: list = element.findall('./' + cacnamespace + 'DocumentReference')
        if len(documentreferences_) != 0:
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    documentreferences.append(tmp)
        if len(shipments) + len(documentreferences) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
            if len(shipments) != 0:
                document.shipment = shipments
            if len(documentreferences) != 0:
                document.documentreference = documentreferences
            document.save()

        return document
