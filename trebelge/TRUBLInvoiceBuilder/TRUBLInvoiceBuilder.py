import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
from trebelge.TRUBLCommonElementsStrategy.TRUBLInvoiceLine import TRUBLInvoiceLine
from trebelge.TRUBLCommonElementsStrategy.TRUBLMonetaryTotal import TRUBLMonetaryTotal
from trebelge.TRUBLCommonElementsStrategy.TRUBLNote import TRUBLNote
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLPaymentTerms import TRUBLPaymentTerms
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLCommonElementsStrategy.TRUBLTaxTotal import TRUBLTaxTotal
from trebelge.TRUBLInvoiceBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLInvoiceBuilder.TRUBLInvoice import TRUBLInvoice


class TRUBLInvoiceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self._product = None
        self.reset()

    def reset(self) -> None:
        self._product = TRUBLInvoice()

    @property
    def product(self) -> TRUBLInvoice:
        product = self._product
        self.reset()
        return product

    def build_ublversionid(self, filepath: str, cbcnamespace: str) -> None:
        # ['UBLVersionID'] = ('cbc', 'ublversionid', 'Zorunlu (1)')
        self._product.add({
            'ublversionid': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'UBLVersionID').text
        })

    def build_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        # ['CustomizationID'] = ('cbc', 'customizationid', 'Zorunlu (1)')
        self._product.add({
            'customizationid': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'CustomizationID').text
        })

    def build_profileid(self, filepath: str, cbcnamespace: str) -> None:
        # ['ProfileID'] = ('cbc', 'profileid', 'Zorunlu (1)')
        self._product.add({
            'profileid': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'ProfileID').text
        })

    def build_id(self, filepath: str, cbcnamespace: str) -> None:
        # ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        self._product.add({
            'id': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'ID').text
        })

    def build_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        # ['CopyIndicator'] = ('cbc', 'copyindicator', 'Zorunlu (1)')
        self._product.add({
            'copyindicator': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'CopyIndicator').text
        })

    def build_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        # ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu (1)')
        self._product.add({
            'issuedate': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'IssueDate').text
        })

    def build_issuetime(self, filepath: str, cbcnamespace: str) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        issuetime_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'IssueTime')
        if issuetime_:
            self._product.add({
                'issuetime': issuetime_.text
            })
        else:
            self._product.add({
                'issuetime': ''
            })

    def build_invoicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        # ['InvoiceTypeCode'] = ('cbc', 'invoicetypecode', 'Zorunlu (1)')
        self._product.add({
            'invoicetypecode': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'InvoiceTypeCode').text
        })

    def build_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_note(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['Note'] = ('cbc', 'note', 'Seçimli (0...n)', 'note')
        notes_: list = ET.parse(filepath).getroot().findall('./' + cbcnamespace + 'Note')
        if notes_:
            note: list = []
            for note_ in notes_:
                note.append(TRUBLNote().process_element(note_,
                                                        cbcnamespace,
                                                        cacnamespace).name
                            )
            self._product.add({
                'note': note
            })

    def build_documentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        # ['DocumentCurrencyCode'] = ('cbc', 'documentcurrencycode', 'Zorunlu (1)')
        self._product.add({
            'documentcurrencycode': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'DocumentCurrencyCode').text
        })

    def build_taxcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        # ['TaxCurrencyCode'] = ('cbc', 'taxcurrencycode', 'Seçimli (0...1)')
        taxcurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'TaxCurrencyCode')
        if taxcurrencycode_:
            self._product.add({
                'taxcurrencycode': taxcurrencycode_.text
            })

    def build_pricingcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        # ['PricingCurrencyCode'] = ('cbc', 'pricingcurrencycode', 'Seçimli (0...1)')
        pricingcurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'PricingCurrencyCode')
        if pricingcurrencycode_:
            self._product.add({
                'pricingcurrencycode': pricingcurrencycode_.text
            })

    def build_paymentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        # ['PaymentCurrencyCode'] = ('cbc', 'paymentcurrencycode', 'Seçimli (0...1)')
        paymentcurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'PaymentCurrencyCode')
        if paymentcurrencycode_:
            self._product.add({
                'paymentcurrencycode': paymentcurrencycode_.text
            })

    def build_paymentalternativecurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        # ['PaymentAlternativeCurrencyCode'] = ('cbc', 'paymentalternativecurrencycode', 'Seçimli (0...1)')
        paymentalternativecurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'PaymentAlternativeCurrencyCode')
        if paymentalternativecurrencycode_:
            self._product.add({
                'paymentalternativecurrencycode': paymentalternativecurrencycode_.text
            })

    def build_accountingcost(self, filepath: str, cbcnamespace: str) -> None:
        # ['AccountingCost'] = ('cbc', 'accountingcost', 'Seçimli (0...1)')
        accountingcost_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'AccountingCost')
        if accountingcost_:
            self._product.add({
                'accountingcost': accountingcost_.text
            })

    def build_linecountnumeric(self, filepath: str, cbcnamespace: str) -> None:
        # ['LineCountNumeric'] = ('cbc', 'linecountnumeric', 'Zorunlu (1)')
        self._product.add({
            'linecountnumeric': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'LineCountNumeric').text
        })

    def build_invoiceperiod(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)', 'invoiceperiod')
        invoiceperiod_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'InvoicePeriod')
        if invoiceperiod_:
            self._product.add({
                'invoiceperiod': TRUBLPeriod.process_element(invoiceperiod_,
                                                             cbcnamespace,
                                                             cacnamespace)
            })

    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...1)', 'orderreference')
        orderreference_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'OrderReference')
        if orderreference_:
            self._product.add({
                'orderreference': TRUBLOrderReference.process_element(orderreference_,
                                                                      cbcnamespace,
                                                                      cacnamespace)
            })

    def build_billingreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['BillingReference'] = ('cac', BillingReference(), 'Seçimli (0...n)', 'billingreference')
        pass

    def build_despatchdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'despatchdocumentreference')
        pass

    def build_receiptdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'receiptdocumentreference')
        pass

    def build_originatordocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['OriginatorDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'originatordocumentreference')
        pass

    def build_contractdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'contractdocumentreference')
        pass

    def build_additionaldocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['AdditionalDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)',
        # 'additionaldocumentreference')
        pass

    def build_accountingsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        pass

    def build_despatchsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        pass

    def build_accountingcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        pass

    def build_deliverycustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['DeliveryCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'deliverycustomerparty')
        pass

    def build_buyercustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['BuyerCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'buyercustomerparty')
        pass

    def build_sellersupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['SellerSupplierParty'] = ('cac', SupplierParty(), 'Seçimli (0..1)', 'sellersupplierparty')
        pass

    def build_originatorcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['OriginatorCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'originatorcustomerparty')
        pass

    def build_taxrepresentativeparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['TaxRepresentativeParty'] = ('cac', Party(), 'Seçimli (0..1)', 'taxrepresentativeparty')
        pass

    def build_delivery(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)', 'delivery')
        pass

    def build_shipment(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['Shipment'] = ('cac', Shipment(), 'Seçimli (0...n)', 'shipment')
        pass

    def build_paymentmeans(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)')
        pass

    def build_paymentterms(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['PaymentTerms'] = ('cac', PaymentTerms(), 'Seçimli (0..1)')
        paymentterms_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PaymentTerms')
        if paymentterms_:
            self._product.add({
                'paymentterms': TRUBLPaymentTerms.process_element(paymentterms_,
                                                                  cbcnamespace,
                                                                  cacnamespace)
            })

    def build_allowancecharge(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)', 'allowancecharge')
        pass

    def build_taxexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'taxexchangerate')
        taxexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'TaxExchangeRate')
        if taxexchangerate_:
            self._product.add({
                'taxexchangerate': TRUBLExchangeRate.process_element(taxexchangerate_,
                                                                     cbcnamespace,
                                                                     cacnamespace)
            })

    def build_pricingexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'pricingexchangerate')
        pricingexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PricingExchangeRate')
        if pricingexchangerate_:
            self._product.add({
                'pricingexchangerate': TRUBLExchangeRate.process_element(pricingexchangerate_,
                                                                         cbcnamespace,
                                                                         cacnamespace)
            })

    def build_paymentexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentexchangerate')
        paymentexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PaymentExchangeRate')
        if paymentexchangerate_:
            self._product.add({
                'paymentexchangerate': TRUBLExchangeRate.process_element(paymentexchangerate_,
                                                                         cbcnamespace,
                                                                         cacnamespace)
            })

    def build_paymentalternativeexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)',
        # 'paymentalternativeexchangerate')
        paymentalternativeexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate_:
            self._product.add({
                'paymentalternativeexchangerate': TRUBLExchangeRate.process_element(
                    paymentalternativeexchangerate_,
                    cbcnamespace,
                    cacnamespace)
            })

    def build_taxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)', 'taxtotal')
        taxtotals_: list = ET.parse(filepath).getroot().findall('./' + cacnamespace + 'TaxTotal')
        taxtotal: list = []
        for taxtotal_ in taxtotals_:
            taxtotal.append(TRUBLTaxTotal.process_element(taxtotal_,
                                                          cbcnamespace,
                                                          cacnamespace))
        self._product.add({
            'taxtotal': taxtotal
        })

    def build_withholdingtaxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'withholdingtaxtotal')
        withholdingtaxtotals_: list = ET.parse(filepath).getroot().findall('./' + cacnamespace + 'WithholdingTaxTotal')
        if withholdingtaxtotals_:
            withholdingtaxtotal: list = []
            for withholdingtaxtotal_ in withholdingtaxtotals_:
                withholdingtaxtotal.append(TRUBLTaxTotal.process_element(withholdingtaxtotal_,
                                                                         cbcnamespace,
                                                                         cacnamespace))
            self._product.add({
                'withholdingtaxtotal': withholdingtaxtotal
            })

    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        legalmonetarytotal_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'LegalMonetaryTotal')
        self._product.add({
            'legalmonetarytotal': TRUBLMonetaryTotal.process_element(legalmonetarytotal_,
                                                                     cbcnamespace,
                                                                     cacnamespace)
        })

    def build_invoiceline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)', 'invoiceline')
        invoicelines_: list = ET.parse(filepath).getroot().findall('./' + cacnamespace + 'InvoiceLine')
        invoiceline: list = []
        for invoiceline_ in invoicelines_:
            invoiceline.append(TRUBLInvoiceLine.process_element(invoiceline_,
                                                                cbcnamespace,
                                                                cacnamespace))
        self._product.add({
            'invoiceline': invoiceline
        })

    def build_despatchline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        # ['DespatchLine'] = ('cac', DespatchLine(), 'Zorunlu (1...n)', 'despatchline')
        pass
