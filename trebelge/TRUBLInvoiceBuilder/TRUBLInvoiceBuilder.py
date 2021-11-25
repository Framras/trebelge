import xml.etree.ElementTree as ET

from trebelge.TRUBLCommonElementsStrategy import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLExchangeRate import TRUBLExchangeRate
from trebelge.TRUBLCommonElementsStrategy.TRUBLMonetaryTotal import TRUBLMonetaryTotal
from trebelge.TRUBLCommonElementsStrategy.TRUBLOrderReference import TRUBLOrderReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLPeriod import TRUBLPeriod
from trebelge.TRUBLInvoiceBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.TRUBLInvoiceBuilder.TRUBLInvoice import TRUBLInvoice


class TRUBLInvoiceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def __init__(self, uuid_: str) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self._set_product(uuid_)

    def _reset(self) -> None:
        self._product = None

    def _set_product(self, uuid_: str):
        self._product = TRUBLInvoice(uuid_)

    @property
    def product(self) -> TRUBLInvoice:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self._reset()
        return product

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

    def build_notes(self, filepath: str, cbcnamespace: str) -> None:
        if ET.parse(filepath).getroot().find(
                cbcnamespace + 'Note') is not None:
            notes: list = []
            for note in ET.parse(filepath).getroot().findall(cbcnamespace + 'Note'):
                notes.append({'note': note.text})
            self._product.add({
                'notes': notes
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
            mapping: dict = {'startdate': 'invoiceperiod_startdate',
                             'starttime': 'invoiceperiod_starttime',
                             'enddate': 'invoiceperiod_enddate',
                             'endtime': 'invoiceperiod_endtime',
                             'durationmeasure': 'invoiceperiod_durationmeasure',
                             'durationmeasure_unitcode': 'invoiceperiod_durationmeasure_unitcode',
                             'description': 'invoiceperiod_description'
                             }
            strategy: TRUBLCommonElement = TRUBLPeriod()
            self._strategyContext.set_strategy(strategy)
            period_ = self._strategyContext.return_element_data(invoiceperiod, cbcnamespace, cacnamespace)
            for key in period_.keys():
                if period_.get(key) is not None:
                    self._product.add({mapping.get(key): period_.get(key)
                                       })

    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        orderreference = ET.parse(filepath).getroot().find(
            cacnamespace + 'OrderReference')
        if orderreference is not None:
            # ['DocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)')
            mapping: dict = {'id': 'orderreference_id',
                             'salesorderid': 'orderreference_salesorderid',
                             'issuedate': 'orderreference_issuedate',
                             'ordertypecode': 'orderreference_ordertypecode'
                             # 'documentreferences': 'orderreference_documentreferences'
                             }
            strategy: TRUBLCommonElement = TRUBLOrderReference()
            self._strategyContext.set_strategy(strategy)
            orderreference_ = self._strategyContext.return_element_data(orderreference, cbcnamespace,
                                                                        cacnamespace)
            for key in orderreference_.keys():
                if orderreference_.get(key) is not None:
                    self._product.add({
                        mapping.get(key): orderreference_.get(key)
                    })

    def build_orderreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_billingreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_despatchdocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_receiptdocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_originatordocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_contractdocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_additionaldocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
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

    def build_originatorcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_sellersupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_taxrepresentativeparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_deliveries(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_shipment(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_paymentmeans(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_paymentterm(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_allowancecharges(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_taxexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        taxexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'TaxExchangeRate')
        if taxexchangerate is not None:
            mapping: dict = {'sourcecurrencycode': 'taxexchangerate_sourcecurrencycode',
                             'targetcurrencycode': 'taxexchangerate_targetcurrencycode',
                             'calculationrate': 'taxexchangerate_calculationrate',
                             'date': 'taxexchangerate_date'
                             }
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(taxexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        mapping.get(key): exchangerate_.get(key)
                    })

    def build_pricingexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pricingexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'PricingExchangeRate')
        if pricingexchangerate is not None:
            mapping: dict = {'sourcecurrencycode': 'pricingexchangerate_sourcecurrencycode',
                             'targetcurrencycode': 'pricingexchangerate_targetcurrencycode',
                             'calculationrate': 'pricingexchangerate_calculationrate',
                             'date': 'pricingexchangerate_date'
                             }
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(pricingexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        mapping.get(key): exchangerate_.get(key)
                    })

    def build_paymentexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        paymentexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'PaymentExchangeRate')
        if paymentexchangerate is not None:
            mapping: dict = {'sourcecurrencycode': 'paymentexchangerate_sourcecurrencycode',
                             'targetcurrencycode': 'paymentexchangerate_targetcurrencycode',
                             'calculationrate': 'paymentexchangerate_calculationrate',
                             'date': 'paymentexchangerate_date'
                             }
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(paymentexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        mapping.get(key): exchangerate_.get(key)
                    })

    def build_paymentalternativeexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        paymentalternativeexchangerate = ET.parse(filepath).getroot().find(
            cacnamespace + 'PaymentAlternativeExchangeRate')
        if paymentalternativeexchangerate is not None:
            mapping: dict = {'sourcecurrencycode': 'paymentalternativeexchangerate_sourcecurrencycode',
                             'targetcurrencycode': 'paymentalternativeexchangerate_targetcurrencycode',
                             'calculationrate': 'paymentalternativeexchangerate_calculationrate',
                             'date': 'paymentalternativeexchangerate_date'
                             }
            strategy: TRUBLCommonElement = TRUBLExchangeRate()
            self._strategyContext.set_strategy(strategy)
            exchangerate_ = self._strategyContext.return_element_data(paymentalternativeexchangerate, cbcnamespace,
                                                                      cacnamespace)
            for key in exchangerate_.keys():
                if exchangerate_.get(key) is not None:
                    self._product.add({
                        mapping.get(key): exchangerate_.get(key)
                    })

    def build_taxtotals(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_withholdingtaxtotals(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        legalmonetarytotal = ET.parse(filepath).getroot().find(
            cacnamespace + 'LegalMonetaryTotal')
        mapping: dict = {'lineextensionamount': 'legalmonetarytotal_lineextensionamount',
                         'lineextensionamount_currencyid': 'legalmonetarytotal_lineextensionamount_currencyid',
                         'taxexclusiveamount': 'legalmonetarytotal_taxexclusiveamount',
                         'taxexclusiveamount_currencyid': 'legalmonetarytotal_taxexclusiveamount_currencyid',
                         'taxinclusiveamount': 'legalmonetarytotal_taxinclusiveamount',
                         'taxinclusiveamount_currencyid': 'legalmonetarytotal_taxinclusiveamount_currencyid',
                         'allowancetotalamount': 'legalmonetarytotal_allowancetotalamount',
                         'allowancetotalamount_currencyid': 'legalmonetarytotal_allowancetotalamount_currencyid',
                         'chargetotalamount': 'legalmonetarytotal_chargetotalamount',
                         'chargetotalamount_currencyid': 'legalmonetarytotal_chargetotalamount_currencyid',
                         'payableroundingamount': 'legalmonetarytotal_payableroundingamount',
                         'payableroundingamount_currencyid': 'legalmonetarytotal_payableroundingamount_currencyid',
                         'payableamount': 'legalmonetarytotal_payableamount',
                         'payableamount_currencyid': 'legalmonetarytotal_payableamount_currencyid'
                         }
        strategy: TRUBLCommonElement = TRUBLMonetaryTotal()
        self._strategyContext.set_strategy(strategy)
        monetarytotal_ = self._strategyContext.return_element_data(legalmonetarytotal, cbcnamespace,
                                                                   cacnamespace)
        for key in monetarytotal_.keys():
            if monetarytotal_.get(key) is not None:
                self._product.add({
                    mapping.get(key): monetarytotal_.get(key)
                })

    def build_invoicelines(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    def build_despatchlines(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass
