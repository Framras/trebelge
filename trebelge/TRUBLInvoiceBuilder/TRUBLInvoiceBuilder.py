import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from trebelge.TRUBLCommonElementsStrategy import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
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
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()
    _product: TRUBLInvoice = TRUBLInvoice()

    def _reset(self) -> None:
        self._product: TRUBLInvoice = TRUBLInvoice()

    def set_product(self, uuid_: str):
        self._reset()
        self._product: TRUBLInvoice = TRUBLInvoice()
        self._product.set_uuid(uuid_)

    def get_product(self) -> TRUBLInvoice:
        return self._product

    def build_ublversionid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'ublversionid': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'UBLVersionID').text
        })

    def build_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'customizationid': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'CustomizationID').text
        })

    def build_profileid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'profileid': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'ProfileID').text
        })

    def build_id(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'id': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'ID').text
        })

    def build_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'copyindicator': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'CopyIndicator').text
        })

    def build_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'issuedate': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'IssueDate').text
        })

    def build_issuetime(self, filepath: str, cbcnamespace: str) -> None:
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
        self._product.add({
            'invoicetypecode': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'InvoiceTypeCode').text
        })

    def build_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_note(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        notes_: list = ET.parse(filepath).getroot().findall('./' + cbcnamespace + 'Note')
        if notes_:
            strategy: TRUBLCommonElement = TRUBLNote()
            self._strategyContext.set_strategy(strategy)
            for note_ in notes_:
                self._product.add({
                    'note': self._strategyContext.return_element_data(note_,
                                                                      cbcnamespace,
                                                                      cacnamespace)
                })

    def build_documentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'documentcurrencycode': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'DocumentCurrencyCode').text
        })

    def build_taxcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        taxcurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'TaxCurrencyCode')
        if taxcurrencycode_:
            self._product.add({
                'taxcurrencycode': taxcurrencycode_.text
            })

    def build_pricingcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pricingcurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'PricingCurrencyCode')
        if pricingcurrencycode_:
            self._product.add({
                'pricingcurrencycode': pricingcurrencycode_.text
            })

    def build_paymentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        paymentcurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'PaymentCurrencyCode')
        if paymentcurrencycode_:
            self._product.add({
                'paymentcurrencycode': paymentcurrencycode_.text
            })

    def build_paymentalternativecurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        paymentalternativecurrencycode_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'PaymentAlternativeCurrencyCode')
        if paymentalternativecurrencycode_:
            self._product.add({
                'paymentalternativecurrencycode': paymentalternativecurrencycode_.text
            })

    def build_accountingcost(self, filepath: str, cbcnamespace: str) -> None:
        accountingcost_: Element = ET.parse(filepath).getroot().find(
            './' + cbcnamespace + 'AccountingCost')
        if accountingcost_:
            self._product.add({
                'accountingcost': accountingcost_.text
            })

    def build_linecountnumeric(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'linecountnumeric': ET.parse(filepath).getroot().find(
                './' + cbcnamespace + 'LineCountNumeric').text
        })

    def build_invoiceperiod(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        invoiceperiod_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'InvoicePeriod')
        if invoiceperiod_:
            strategy: TRUBLCommonElement = TRUBLPeriod()
            self._strategyContext.set_strategy(strategy)
            self._product.add({
                'invoiceperiod': self._strategyContext.return_element_data(invoiceperiod_,
                                                                           cbcnamespace,
                                                                           cacnamespace)
            })

    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        orderreference_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'OrderReference')
        if orderreference_:
            strategy: TRUBLCommonElement = TRUBLOrderReference()
            self._strategyContext.set_strategy(strategy)
            self._product.add({
                'orderreference': self._strategyContext.return_element_data(orderreference_,
                                                                            cbcnamespace,
                                                                            cacnamespace)
            })

    def build_billingreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_despatchdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_receiptdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_originatordocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_contractdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_additionaldocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_accountingsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_despatchsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_accountingcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_deliverycustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_buyercustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_sellersupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_taxrepresentativeparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_originatorcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_delivery(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_shipment(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_paymentmeans(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_paymentterms(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        paymentterms_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PaymentTerms')
        if paymentterms_:
            strategy: TRUBLCommonElement = TRUBLPaymentTerms()
            self._strategyContext.set_strategy(strategy)
            self._product.add({
                'paymentterms': self._strategyContext.return_element_data(paymentterms_,
                                                                          cbcnamespace,
                                                                          cacnamespace)
            })

    def build_allowancecharge(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_taxexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        taxexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'TaxExchangeRate')
        if taxexchangerate_:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            self._product.add({
                'taxexchangerate': self._strategyContext.return_element_data(taxexchangerate_,
                                                                             cbcnamespace,
                                                                             cacnamespace)
            })

    def build_pricingexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pricingexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PricingExchangeRate')
        if pricingexchangerate_:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            self._product.add({
                'pricingexchangerate': self._strategyContext.return_element_data(pricingexchangerate_,
                                                                                 cbcnamespace,
                                                                                 cacnamespace)
            })

    def build_paymentexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        paymentexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PaymentExchangeRate')
        if paymentexchangerate_:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            self._product.add({
                'paymentexchangerate': self._strategyContext.return_element_data(paymentexchangerate_,
                                                                                 cbcnamespace,
                                                                                 cacnamespace)
            })

    def build_paymentalternativeexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        paymentalternativeexchangerate_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate_:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            self._product.add({
                'paymentalternativeexchangerate': self._strategyContext.return_element_data(
                    paymentalternativeexchangerate_,
                    cbcnamespace,
                    cacnamespace)
            })

    def build_taxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        taxtotals_: list = ET.parse(filepath).getroot().findall('./' + cacnamespace + 'TaxTotal')
        taxtotal: list = []
        for taxtotal_ in taxtotals_:
            strategy: TRUBLCommonElement = TRUBLTaxTotal()
            self._strategyContext.set_strategy(strategy)
            taxtotal.append(self._strategyContext.return_element_data(taxtotal_,
                                                                      cbcnamespace,
                                                                      cacnamespace))
        self._product.add({
            'taxtotal': taxtotal
        })

    def build_withholdingtaxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        withholdingtaxtotals_: list = ET.parse(filepath).getroot().findall('./' + cacnamespace + 'WithholdingTaxTotal')
        if withholdingtaxtotals_:
            withholdingtaxtotal: list = []
            for withholdingtaxtotal_ in withholdingtaxtotals_:
                strategy: TRUBLCommonElement = TRUBLTaxTotal()
                self._strategyContext.set_strategy(strategy)
                withholdingtaxtotal.append(self._strategyContext.return_element_data(withholdingtaxtotal_,
                                                                                     cbcnamespace,
                                                                                     cacnamespace))
            self._product.add({
                'withholdingtaxtotal': withholdingtaxtotal
            })

    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        legalmonetarytotal_: Element = ET.parse(filepath).getroot().find(
            './' + cacnamespace + 'LegalMonetaryTotal')
        strategy: TRUBLCommonElement = TRUBLMonetaryTotal()
        self._strategyContext.set_strategy(strategy)
        self._product.add({
            'legalmonetarytotal': self._strategyContext.return_element_data(legalmonetarytotal_,
                                                                            cbcnamespace,
                                                                            cacnamespace)
        })

    def build_invoiceline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        invoicelines_: list = ET.parse(filepath).getroot().findall('./' + cacnamespace + 'InvoiceLine')
        invoiceline: list = []
        for invoiceline_ in invoicelines_:
            strategy: TRUBLCommonElement = TRUBLInvoiceLine()
            self._strategyContext.set_strategy(strategy)
            invoiceline.append(self._strategyContext.return_element_data(invoiceline_,
                                                                         cbcnamespace,
                                                                         cacnamespace))
        self._product.add({
            'invoiceline': invoiceline
        })

    def build_despatchline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass
