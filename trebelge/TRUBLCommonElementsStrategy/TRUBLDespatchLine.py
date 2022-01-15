from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderLineReference import TRUBLOrderLineReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLShipment import TRUBLShipment


class TRUBLDespatchLine(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR DespatchLine'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ID'] = ('cbc', 'id', 'Zorunlu(1)')
        id_ = element.find('./' + cbcnamespace + 'ID').text
        if id_ is None:
            return None
        frappedoc: dict = {'id': id_}
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Zorunlu(1)')
        orderlinereference_: Element = element.find('./' + cacnamespace + 'OrderLineReference')
        tmp = TRUBLOrderLineReference().process_element(orderlinereference_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc['orderlinereference'] = tmp.name
        # ['Item'] = ('cac', 'Item', 'Zorunlu(1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        tmp = TRUBLItem().process_element(item_, cbcnamespace, cacnamespace)
        if tmp is None:
            return None
        frappedoc['item'] = tmp.name
        # ['DeliveredQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OutstandingQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['DeliveredQuantity', 'OutstandingQuantity', 'OversupplyQuantity']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
                    frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Note'] = ('cbc', '', 'Seçimli(0..n)')
        notes = list()
        notes_: list = element.findall('./' + cbcnamespace + 'Note')
        if len(notes_) != 0:
            for note_ in notes_:
                tmp = TRUBLNote().process_element(note_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    notes.append(tmp)
            if len(notes) != 0:
                frappedoc['note'] = notes
        # ['OutstandingReason'] = ('cbc', '', 'Seçimli(0..n)')
        outstandingreasons = list()
        outstandingreasons_: list = element.findall('./' + cbcnamespace + 'Description')
        if len(outstandingreasons_) != 0:
            for outstandingreason_ in outstandingreasons_:
                tmp = TRUBLNote().process_element(outstandingreason_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    outstandingreasons.append(tmp)
            if len(outstandingreasons) != 0:
                frappedoc['outstandingreason'] = outstandingreasons
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli(0..n)')
        shipments = list()
        shipments_: list = element.findall('./' + cacnamespace + 'Shipment')
        if len(shipments_) != 0:
            for shipment_ in shipments_:
                tmp = TRUBLShipment().process_element(shipment_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    shipments.append(tmp)
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli(0..n)')
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
