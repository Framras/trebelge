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
        frappedoc: dict = {'id': element.find('./' + cbcnamespace + 'ID').text}
        # ['OrderLineReference'] = ('cac', 'OrderLineReference', 'Zorunlu(1)')
        orderlinereference_: Element = element.find('./' + cacnamespace + 'OrderLineReference')
        frappedoc['orderlinereference'] = [TRUBLOrderLineReference.process_element(orderlinereference_,
                                                                                   cbcnamespace,
                                                                                   cacnamespace)]
        # ['Item'] = ('cac', 'Item', 'Zorunlu(1)')
        item_: Element = element.find('./' + cacnamespace + 'Item')
        frappedoc['item'] = [TRUBLItem.process_element(item_,
                                                       cbcnamespace,
                                                       cacnamespace)]
        # ['DeliveredQuantity'] = ('cbc', '', 'Seçimli (0...1)')
        # ['OutstandingQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        # ['OversupplyQuantity'] = ('cbc', '', 'Seçimli(0..1)')
        cbcsecimli01: list = ['DeliveredQuantity', 'OutstandingQuantity', 'OversupplyQuantity']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                frappedoc[elementtag_.lower()] = field_.text
                frappedoc[elementtag_.lower() + 'unitcode'] = field_.attrib.get('unitCode')
        # ['Note'] = ('cbc', '', 'Seçimli(0..n)')
        notes_: list = element.findall('./' + cbcnamespace + 'Note')
        if notes_:
            note: list = []
            for note_ in notes_:
                note.append(TRUBLNote.process_element(note_,
                                                      cbcnamespace,
                                                      cacnamespace))
            frappedoc['note'] = note
        # ['OutstandingReason'] = ('cbc', '', 'Seçimli(0..n)')
        outstandingreasons_: list = element.findall('./' + cbcnamespace + 'Description')
        if outstandingreasons_:
            outstandingreason: list = []
            for outstandingreason_ in outstandingreasons_:
                outstandingreason.append(TRUBLNote.process_element(outstandingreason_,
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
                for tagelement in tagelements_:
                    tagelements.append(element_.get('strategy').process_element(tagelement,
                                                                                cbcnamespace,
                                                                                cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
