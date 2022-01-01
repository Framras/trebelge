from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommunication import TRUBLCommunication


class TRUBLContact(TRUBLCommonElement):
    _frappeDoctype: str = 'UBL TR Contact'

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['Telephone'] = ('cbc', 'telephone', 'Seçimli (0...1)')
        # ['Telefax'] = ('cbc', 'telefax', 'Seçimli (0...1)')
        # ['ElectronicMail'] = ('cbc', 'electronicmail', 'Seçimli (0...1)')
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'Telephone', 'Telefax', 'ElectronicMail', 'Note']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None and field_.text is not None:
                frappedoc[elementtag_.lower()] = field_.text
        # ['Name'] = ('cbc', 'name', 'Seçimli (0...1)')
        name_: Element = element.find('./' + cbcnamespace + 'Name')
        if name_ is not None and name_.text is not None:
            frappedoc['contactname'] = name_.text
        # ['OtherCommunication'] = ('cac', 'Communication', 'Seçimli(0..n)')
        othercommunications_: list = element.findall('./' + cacnamespace + 'OtherCommunication')
        if len(othercommunications_) != 0:
            communications: list = []
            for othercommunication in othercommunications_:
                tmp = TRUBLCommunication().process_element(othercommunication,
                                                           cbcnamespace,
                                                           cacnamespace)
                if tmp is not None:
                    communications.append(tmp)
            if len(communications) != 0:
                if frappedoc != {}:
                    document = self._get_frappedoc(self._frappeDoctype, frappedoc)
                    document.othercommunication = communications
                    document.save()
                    return document
                else:
                    frappedoc['othercommunication'] = communications
                    return self._get_frappedoc(self._frappeDoctype, frappedoc)
        elif frappedoc != {}:
            return self._get_frappedoc(self._frappeDoctype, frappedoc)
        else:
            return None
