# from __future__ import annotations
import xml.etree.ElementTree as ET

from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState


class ExchangeRate(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _mapping = dict()
    _elementTag: str = 'TaxExchangeRate'
    _invoiceTaxElementTag: str = 'TaxExchangeRate'
    _invoicePricingElementTag: str = 'PricingExchangeRate'
    _invoicePaymentElementTag: str = 'PaymentExchangeRate'
    _invoicePaymentAlternativeElementTag: str = 'PaymentAlternativeExchangeRate'
    _initiatorTag: str = ''

    def find_ebelge_status(self):
        pass

    def define_mappings(self, tag: str, initiator: AbstractXMLFileState):
        self._initiatorTag = tag
        # _mapping[tag] = (namespace, frappe_field, cardinality, start_event, has_attribs, end_event)
        if tag == self._invoiceTaxElementTag:
            # Zorunlu(1): SourceCurrencyCode
            self._mapping['SourceCurrencyCode'] = (
                'cbc', 'taxexchangerate_sourcecurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): TargetCurrencyCode
            self._mapping['TargetCurrencyCode'] = (
                'cbc', 'taxexchangerate_targetcurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): CalculationRate
            self._mapping['CalculationRate'] = (
                'cbc', 'taxexchangerate_calculationrate', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1): Date
            self._mapping['Date'] = (
                'cbc', 'taxexchangerate_date', 'Seçimli (0...1)', False, False, True, '')
            self._mapping[self._invoiceTaxElementTag] = ('cac', initiator, '', False, False, True, '')
        elif tag == self._invoicePricingElementTag:
            # Zorunlu(1): SourceCurrencyCode
            self._mapping['SourceCurrencyCode'] = (
                'cbc', 'pricingexchangerate_sourcecurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): TargetCurrencyCode
            self._mapping['TargetCurrencyCode'] = (
                'cbc', 'pricingexchangerate_targetcurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): CalculationRate
            self._mapping['CalculationRate'] = (
                'cbc', 'pricingexchangerate_calculationrate', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1): Date
            self._mapping['Date'] = (
                'cbc', 'pricingexchangerate_date', 'Seçimli (0...1)', False, False, True, '')
            self._mapping[self._invoicePricingElementTag] = ('cac', initiator, '', False, False, True, '')
        elif tag == self._invoicePaymentElementTag:
            # Zorunlu(1): SourceCurrencyCode
            self._mapping['SourceCurrencyCode'] = (
                'cbc', 'paymentexchangerate_sourcecurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): TargetCurrencyCode
            self._mapping['TargetCurrencyCode'] = (
                'cbc', 'paymentexchangerate_targetcurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): CalculationRate
            self._mapping['CalculationRate'] = (
                'cbc', 'paymentexchangerate_calculationrate', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1): Date
            self._mapping['Date'] = (
                'cbc', 'paymentexchangerate_date', 'Seçimli (0...1)', False, False, True, '')
            self._mapping[self._invoicePaymentElementTag] = ('cac', initiator, '', False, False, True, '')
        elif tag == self._invoicePaymentAlternativeElementTag:
            # Zorunlu(1): SourceCurrencyCode
            self._mapping['SourceCurrencyCode'] = (
                'cbc', 'paymentalternativeexchangerate_sourcecurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): TargetCurrencyCode
            self._mapping['TargetCurrencyCode'] = (
                'cbc', 'paymentalternativeexchangerate_targetcurrencycode', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): CalculationRate
            self._mapping['CalculationRate'] = (
                'cbc', 'paymentalternativeexchangerate_calculationrate', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1): Date
            self._mapping['Date'] = (
                'cbc', 'paymentalternativeexchangerate_date', 'Seçimli (0...1)', False, False, True, '')
            self._mapping[self._invoicePaymentAlternativeElementTag] = ('cac', initiator, '', False, False, True, '')
        elif tag == self._elementTag:
            # Zorunlu(1): SourceCurrencyCode
            self._mapping['SourceCurrencyCode'] = ('cbc', '', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): TargetCurrencyCode
            self._mapping['TargetCurrencyCode'] = ('cbc', '', 'Zorunlu(1)', False, False, True, '')
            # Zorunlu(1): CalculationRate
            self._mapping['CalculationRate'] = ('cbc', '', 'Zorunlu(1)', False, False, True, '')
            # Seçimli(0..1): Date
            self._mapping['Date'] = ('cbc', '', 'Seçimli (0...1)', False, False, True, '')
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
                                    self._mapping[key][1], element.attrib.get(key))
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
