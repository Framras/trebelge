# from __future__ import annotations
import xml.etree.ElementTree as ET

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState
from trebelge.XMLFileState.TaxSubtotal import TaxSubtotal


class TaxTotal(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _mapping = dict()
    _elementTag: str = 'TaxTotal'
    _withholdingElementTag: str = 'WithholdingTaxTotal'
    _initiatorTag: str = ''

    def find_ebelge_status(self):
        pass

    def define_mappings(self, tag: str, initiator: AbstractXMLFileState):
        self._initiatorTag = tag
        if tag == self._elementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Zorunlu(1): TaxAmount
            self._mapping['TaxAmount'] = ('cbc', 'taxtotal_taxamount', 'Zorunlu(1)', True, True, True, '')
            # attrib currencyID for tags endswith('Amount')
            self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False, '')
            # Zorunlu(1..n): TaxSubtotal:TaxSubtotal
            self._mapping['TaxSubtotal'] = ('cac', TaxSubtotal(), 'Zorunlu(1..n)', True, False, False, '')
            self._mapping[self._elementTag] = ('cac', initiator, '', False, False, True, '')
        elif tag == self._withholdingElementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Zorunlu(1): TaxAmount
            self._mapping['TaxAmount'] = ('cbc', 'withholdingtaxtotal_taxamount', 'Zorunlu(1)', True, True, True, '')
            # attrib currencyID for tags endswith('Amount')
            self._mapping['currencyID'] = (
                '', '', 'Zorunlu(1)', False, False, False, '')
            # Zorunlu(1..n): TaxSubtotal:TaxSubtotal
            self._mapping['TaxSubtotal'] = ('cac', TaxSubtotal(), 'Zorunlu(1..n)', True, False, False, '')
            self._mapping[self._withholdingElementTag] = ('cac', initiator, '', False, False, True, '')
        elif tag == self._elementTag:
            # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
            # Zorunlu(1): TaxAmount
            self._mapping['TaxAmount'] = ('cbc', '', 'Zorunlu(1)', True, True, True, '')
            # attrib currencyID for tags endswith('Amount')
            self._mapping['currencyID'] = ('', '', 'Zorunlu(1)', False, False, False, '')
            # Zorunlu(1..n): TaxSubtotal:TaxSubtotal
            self._mapping['TaxSubtotal'] = ('cac', TaxSubtotal(), 'Zorunlu(1..n)', True, False, False, '')
            self._mapping[self._elementTag] = ('cac', initiator, '', False, False, True, '')

    def read_element_by_action(self, event: str, element: ET.Element):
        tag: str = ''
        if element.tag.startswith(self.get_context().get_cac_namespace()):
            tag = element.tag[len(self.get_context().get_cac_namespace()):]
        elif element.tag.startswith(self.get_context().get_cbc_namespace()):
            tag = element.tag[len(self.get_context().get_cbc_namespace()):]
        if self._mapping[tag] is not None:
            if event == 'start' and self._mapping[tag][3]:
                if element.tag.startswith(self.get_context().get_cbc_namespace()):
                    if self._mapping[tag][4]:
                        for key in element.attrib.keys():
                            if self._mapping[key] is not None:
                                self.get_context().set_new_frappe_doc(
                                    self._mapping[tag][1] + '_' + key.lower(), element.attrib.get(key))
                    else:
                        pass
                elif element.tag.startswith(self.get_context().get_cac_namespace()):
                    if self._mapping[tag][2] in ['Zorunlu (1)', 'Seçimli (0..1)']:
                        self.get_context().set_state = self._mapping[tag][1]
                        self.get_context().define_mappings(self._initiatorTag, self)
                        self.get_context().read_element_by_action(event, element)
                    elif self._mapping[tag][2] in ['Seçimli (0...n)']:
                        pass
            elif event == 'end' and self._mapping[tag][5]:
                if element.tag.startswith(self.get_context().get_cbc_namespace()):
                    if self._mapping[tag][2] in ['Zorunlu (1)', 'Seçimli (0..1)']:
                        self.get_context().set_new_frappe_doc(
                            self._mapping[tag][1], element.text)
                    elif self._mapping[tag][2] in ['Seçimli (0...n)']:
                        if self.get_context().get_new_frappe_doc(self)[self._mapping[tag][1]] is None:
                            self.get_context().set_new_frappe_doc(
                                self._mapping[tag][1], {self._mapping[tag][6]: element.text})
                        else:
                            self.get_context().append_new_frappe_doc_field(
                                self._mapping[tag][1], {self._mapping[tag][6]: element.text})
                elif element.tag.startswith(self.get_context().get_cac_namespace()):
                    self.get_context().set_state = self._mapping[tag][1]
