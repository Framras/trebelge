from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLTransportEquipment(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportEquipment'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', '', 'Seçimli (0...1)')
        # ['schemeID'] = ('', '', 'Seçimli (0...1)')
        id_: Element = element.find('./' + cbcnamespace + 'ID')
        if id_ is not None:
            if id_.text is not None:
                frappedoc['id'] = id_.text
                frappedoc['schemeid'] = id_.attrib.get('schemeID')
        # ['TransportEquipmentTypeCode'] = ('cbc', '', 'Seçimli (0...1)')
        # ['Description'] = ('cbc', '', 'Seçimli (0...1)')
        cbcsecimli01: list = ['TransportEquipmentTypeCode', 'Description']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        if frappedoc == {}:
            return None

        return self._get_frappedoc(self._frappeDoctype, frappedoc)

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
