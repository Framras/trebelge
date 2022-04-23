from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLResponse(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR Response'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        # ['ReferenceID'] = ('cbc', '', 'Zorunlu (1)')
        referenceid = element.find('./' + cbcnamespace + 'ReferenceID').text
        if referenceid is None:
            return None
        frappedoc: dict = dict(referenceid=referenceid)
        # ['ResponseCode'] = ('cbc', '', 'Seçimli (0...1)')
        responsecode_: Element = element.find('./' + cbcnamespace + 'ResponseCode')
        if responsecode_ is not None:
            if responsecode_.text is not None:
                frappedoc['responsecode'] = responsecode_.text
        document = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['Description'] = ('cbc', '', 'Seçimli (0...n)')
        descriptions_: list = element.findall('./' + cacnamespace + 'Description')
        if len(descriptions_) != 0:
            for description_ in descriptions_:
                element_ = description_.text
                if element_ is not None and element_.strip() != '':
                    document.append("description", dict(note=element_.strip()))
                    document.save()

        return document

    def process_elementasdict(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        pass
