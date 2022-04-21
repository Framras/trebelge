from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLItem import TRUBLItem
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
                    frappedoc[elementtag_.lower()] = field_.text.strip()
                    frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode').strip()
        # ['Note'] = ('cbc', '', 'Seçimli(0..n)')
        notes_: list = element.findall('./' + cbcnamespace + 'Note')
        notes = list()
        if len(notes_) != 0:
            for note_ in notes_:
                element_ = note_.text
                if element_ is not None and element_.strip() != '':
                    notes.append(element_.strip())
        # ['OutstandingReason'] = ('cbc', '', 'Seçimli(0..n)')
        outstandingreasons_: list = element.findall('./' + cbcnamespace + 'Description')
        outstandingreasons = list()
        if len(outstandingreasons_) != 0:
            for outstandingreason_ in outstandingreasons_:
                element_ = outstandingreason_.text
                if element_ is not None and element_.strip() != '':
                    outstandingreasons.append(element_.strip())
        # ['Shipment'] = ('cac', 'Shipment', 'Seçimli(0..n)')
        shipments_: list = element.findall('./' + cacnamespace + 'Shipment')
        shipments = list()
        if len(shipments_) != 0:
            for shipment_ in shipments_:
                tmp = TRUBLShipment().process_element(shipment_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    shipments.append(tmp.name)
        # ['DocumentReference'] = ('cac', 'DocumentReference', 'Seçimli(0..n)')
        documentreferences_: list = element.findall('./' + cacnamespace + 'DocumentReference')
        documentreferences = list()
        if len(documentreferences_) != 0:
            for documentreference_ in documentreferences_:
                tmp = TRUBLDocumentReference().process_element(documentreference_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    documentreferences.append(tmp.name)

        if len(notes) + len(outstandingreasons) + len(shipments) + len(documentreferences) == 0:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        if len(notes) != 0:
            for note in notes:
                document.append("note", dict(note=note))
                document.save()
        if len(outstandingreasons) != 0:
            for outstandingreason in outstandingreasons:
                document.append("outstandingreason", dict(note=outstandingreason))
                document.save()
        if len(shipments) != 0:
            doc_append = document.append("shipment", {})
            for shipment in shipments:
                doc_append.shipment = shipment
                document.save()
        if len(documentreferences) != 0:
            doc_append = document.append("documentreference", {})
            for documentreference in documentreferences:
                doc_append.documentreference = documentreference
                document.save()

        return document
