from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext


class TRUBLTransportEquipment(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['schemeID'] = ('', '', 'Seçimli (0...1)')
        id_: Element = element.find(cbcnamespace + 'ID')
        if not id_ is not None:
            frappedoc['id'] = id_.text
            frappedoc['schemeid'] = id_.attrib.get('schemeID')
        # ['TransportEquipmentTypeCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Description'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['TransportEquipmentTypeCode', 'Description']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if not field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
