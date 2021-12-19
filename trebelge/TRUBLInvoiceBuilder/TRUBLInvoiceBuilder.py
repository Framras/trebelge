import xml.etree.ElementTree as ET

from trebelge.TRUBLCommonElementsStrategy import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
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
                cbcnamespace + 'UBLVersionID').text
        })

    def build_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'customizationid': ET.parse(filepath).getroot().find(
                cbcnamespace + 'CustomizationID').text
        })

    def build_profileid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'profileid': ET.parse(filepath).getroot().find(
                cbcnamespace + 'ProfileID').text
        })

    def build_id(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'id': ET.parse(filepath).getroot().find(
                cbcnamespace + 'ID').text
        })

    def build_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'copyindicator': ET.parse(filepath).getroot().find(
                cbcnamespace + 'CopyIndicator').text
        })

    def build_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'issuedate': ET.parse(filepath).getroot().find(
                cbcnamespace + 'IssueDate').text
        })

    def build_issuetime(self, filepath: str, cbcnamespace: str) -> None:
        issuetime = ET.parse(filepath).getroot().find(
            cbcnamespace + 'IssueTime')
        if issuetime is not None:
            self._product.add({
                'issuetime': issuetime.text
            })

    def build_invoicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'invoicetypecode': ET.parse(filepath).getroot().find(
                cbcnamespace + 'InvoiceTypeCode').text
        })

    def build_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_note(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        notes_ = ET.parse(filepath).getroot().findall(cbcnamespace + 'Note')
        if notes_ is not None:
            notes: list = []
            for note in notes_:
                strategy: TRUBLCommonElement = TRUBLNote()
                self._strategyContext.set_strategy(strategy)
                notes.append(self._strategyContext.return_element_data(
                    note,
                    cbcnamespace,
                    cacnamespace))
            self._product.add({
                'note': [notes]
            })

    def build_documentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'documentcurrencycode': ET.parse(filepath).getroot().find(
                cbcnamespace + 'DocumentCurrencyCode').text
        })

    def build_taxcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        taxcurrencycode = ET.parse(filepath).getroot().find(
            cbcnamespace + 'TaxCurrencyCode')
        if taxcurrencycode is not None:
            self._product.add({
                'taxcurrencycode': taxcurrencycode.text
            })

    def build_pricingcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pricingcurrencycode = ET.parse(filepath).getroot().find(
            cbcnamespace + 'PricingCurrencyCode')
        if pricingcurrencycode is not None:
            self._product.add({
                'pricingcurrencycode': pricingcurrencycode.text
            })

    def build_paymentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        paymentcurrencycode = ET.parse(filepath).getroot().find(
            cbcnamespace + 'PaymentCurrencyCode')
        if paymentcurrencycode is not None:
            self._product.add({
                'paymentcurrencycode': paymentcurrencycode.text
            })

    def build_paymentalternativecurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        paymentalternativecurrencycode = ET.parse(filepath).getroot().find(
            cbcnamespace + 'PaymentAlternativeCurrencyCode')
        if paymentalternativecurrencycode is not None:
            self._product.add({
                'paymentalternativecurrencycode': paymentalternativecurrencycode.text
            })

    def build_accountingcost(self, filepath: str, cbcnamespace: str) -> None:
        accountingcost = ET.parse(filepath).getroot().find(
            cbcnamespace + 'AccountingCost')
        if accountingcost is not None:
            self._product.add({
                'accountingcost': accountingcost.text
            })

    def build_linecountnumeric(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'linecountnumeric': ET.parse(filepath).getroot().find(
                cbcnamespace + 'LineCountNumeric').text
        })

    def build_invoiceperiod(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        invoiceperiod = ET.parse(filepath).getroot().find(
            cacnamespace + 'InvoicePeriod')
        if invoiceperiod is not None:
            strategy: TRUBLCommonElement = TRUBLPeriod()
            self._strategyContext.set_strategy(strategy)
            period_ = self._strategyContext.return_element_data(invoiceperiod, cbcnamespace, cacnamespace)
            for key in period_.keys():
                if period_.get(key) is not None:
                    self._product.add({
                        'invoiceperiod_' + key: period_.get(key)
                    })

    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        orderreference = ET.parse(filepath).getroot().find(
            cacnamespace + 'OrderReference')
        if orderreference is not None:
            # ['DocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)')
            # 'documentreferences': 'orderreference_documentreferences'
            strategy: TRUBLCommonElement = TRUBLOrderReference()
            self._strategyContext.set_strategy(strategy)
            orderreference_ = self._strategyContext.return_element_data(orderreference, cbcnamespace,
                                                                        cacnamespace)
            for key in orderreference_.keys():
                if orderreference_.get(key) is not None:
                    self._product.add({
                        'orderreference_' + key: orderreference_.get(key)
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
        paymentterms = ET.parse(filepath).getroot().find(
            cacnamespace + 'PaymentTerms')
        if paymentterms is not None:
            strategy: TRUBLCommonElement = TRUBLPaymentTerms()
            self._strategyContext.set_strategy(strategy)
            paymentterm_ = self._strategyContext.return_element_data(paymentterms, cbcnamespace,
                                                                     cacnamespace)
            for key in paymentterm_.keys():
                if paymentterm_.get(key) is not None:
                    self._product.add({
                        'paymentterms_' + key: paymentterm_.get(key)
                    })

    def build_allowancecharge(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_taxexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        taxexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'TaxExchangeRate')
        if taxexchangerate is not None:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(taxexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        'taxexchangerate_' + key: exchangerate_.get(key)
                    })

    def build_pricingexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pricingexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'PricingExchangeRate')
        if pricingexchangerate is not None:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(pricingexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        'pricingexchangerate_' + key: exchangerate_.get(key)
                    })

    def build_paymentexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        paymentexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'PaymentExchangeRate')
        if paymentexchangerate is not None:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(paymentexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        'paymentexchangerate_' + key: exchangerate_.get(key)
                    })

    def build_paymentalternativeexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        paymentalternativeexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate is not None:
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(paymentalternativeexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        'paymentalternativeexchangerate_' + key: exchangerate_.get(key)
                    })

    def build_taxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        taxtotals: list = []
        for taxtotal in ET.parse(filepath).getroot().findall(cacnamespace + 'TaxTotal'):
            strategy: TRUBLCommonElement = TRUBLTaxTotal()
            self._strategyContext.set_strategy(strategy)
            taxtotal_ = self._strategyContext.return_element_data(taxtotal, cbcnamespace,
                                                                  cacnamespace)
            taxtotals.append(taxtotal_)
        self._product.add({
            'taxtotals': taxtotals
        })

    def build_withholdingtaxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        withholdingtaxtotals = ET.parse(filepath).getroot().findall(cacnamespace + 'WithholdingTaxTotal')
        if withholdingtaxtotals is not None:
            withholdingtaxtotals_: list = []
            for withholdingtaxtotal in withholdingtaxtotals:
                strategy: TRUBLCommonElement = TRUBLTaxTotal()
                self._strategyContext.set_strategy(strategy)
                taxtotal_ = self._strategyContext.return_element_data(withholdingtaxtotal, cbcnamespace,
                                                                      cacnamespace)
                withholdingtaxtotals_.append(taxtotal_)
            self._product.add({
                'withholdingtaxtotals': withholdingtaxtotals_
            })

    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        legalmonetarytotal = ET.parse(filepath).getroot().find(
            cacnamespace + 'LegalMonetaryTotal')
        strategy: TRUBLCommonElement = TRUBLMonetaryTotal()
        self._strategyContext.set_strategy(strategy)
        monetarytotal_ = self._strategyContext.return_element_data(legalmonetarytotal, cbcnamespace,
                                                                   cacnamespace)
        for key in monetarytotal_.keys():
            if monetarytotal_.get(key) is not None:
                self._product.add({
                    'legalmonetarytotal_' + key: monetarytotal_.get(key)
                })

    def build_invoiceline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_despatchline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass
