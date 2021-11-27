from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement


class TRUBLDeliveryTerms(TRUBLCommonElement):
    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> dict:
        """
        ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        ['SpecialTerms'] = ('cbc', 'specialterms', 'Seçimli (0...1)')
        ['Amount'] = ('cbc', 'amount', 'Seçimli (0...1)')
        ['currencyID'] = ('', 'amount_currencyid', 'Zorunlu(1)')
        """
        deliveryterms: dict = {}
        id_ = element.find(cbcnamespace + 'ID')
        if id_ is not None:
            deliveryterms[id_.tag.lower()] = id_.text
        specialterms_ = element.find(cbcnamespace + 'SpecialTerms')
        if specialterms_ is not None:
            deliveryterms[specialterms_.tag.lower()] = specialterms_.text
        amount_ = element.find(cbcnamespace + 'Amount')
        if amount_ is not None:
            deliveryterms['amount'] = amount_.text
            deliveryterms['amount_currencyid'] = amount_.attrib.get('currencyID')

        return deliveryterms
