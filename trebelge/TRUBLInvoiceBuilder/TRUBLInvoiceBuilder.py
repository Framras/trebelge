import xml.etree.ElementTree as ET

from trebelge.TRUBLCommonElementsStrategy import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
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
            # ['StartDate'] = ('cbc', 'invoiceperiod_startdate', 'Seçimli (0...1)')
            # ['StartTime'] = ('cbc', 'invoiceperiod_starttime', 'Seçimli (0...1)')
            # ['EndDate'] = ('cbc', 'invoiceperiod_enddate', 'Seçimli (0...1)')
            # ['EndTime'] = ('cbc', 'invoiceperiod_endtime', 'Seçimli (0...1)')
            # ['DurationMeasure'] = ('cbc', 'invoiceperiod_durationmeasure', 'Seçimli (0...1)')
            # ['unitCode'] = ('', 'invoiceperiod_durationmeasure_unitcode', 'Zorunlu (1)')
            # ['Description'] = ('cbc', 'invoiceperiod_description', 'Seçimli (0...1)')
            conversion: dict = {'startdate': 'invoiceperiod_startdate',
                                'starttime': 'invoiceperiod_starttime',
                                'enddate': 'invoiceperiod_enddate',
                                'endtime': 'invoiceperiod_endtime',
                                'durationmeasure': 'invoiceperiod_durationmeasure',
                                'durationmeasure_unitcode': 'invoiceperiod_durationmeasure_unitcode',
                                'description': 'invoiceperiod_description'
                                }
            strategy: TRUBLCommonElement = TRUBLPeriod()
            self._strategyContext.set_strategy(strategy)
            period = self._strategyContext.return_element_data(invoiceperiod, cbcnamespace, cacnamespace)
            for key in period.keys():
                if period.get(key) is not None:
                    self._product.add({
                        conversion.get(key): period.get(key)
                    })

    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        invoiceorderreference = ET.parse(filepath).getroot().find(
            cacnamespace + 'OrderReference')
        if invoiceorderreference is not None:
            # ['ID'] = ('cbc', 'orderreference_id', 'Zorunlu(1)')
            # ['SalesOrderID'] = ('cbc', 'orderreference_salesorderid', 'Seçimli (0...1)')
            # ['IssueDate'] = ('cbc', 'orderreference_issuedate', 'Zorunlu(1)')
            # ['OrderTypeCode'] = ('cbc', 'orderreference_ordertypecode', 'Seçimli (0...1)')
            # ['DocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)')
            conversion: dict = {'id': 'orderreference_id',
                                'salesorderid': 'orderreference_salesorderid',
                                'issuedate': 'orderreference_issuedate',
                                'ordertypecode': 'orderreference_ordertypecode'
                                # 'documentreferences': 'orderreference_documentreferences'
                                }
            strategy: TRUBLCommonElement = TRUBLOrderReference()
            self._strategyContext.set_strategy(strategy)
            orderreference = self._strategyContext.return_element_data(invoiceorderreference, cbcnamespace,
                                                                       cacnamespace)
            for key in orderreference.keys():
                if orderreference.get(key) is not None:
                    self._product.add({
                        conversion.get(key): orderreference.get(key)
                    })

    def build_orderreferences(self) -> None:
        pass

    def build_billingreferences(self) -> None:
        pass

    def build_despatchdocumentreferences(self) -> None:
        pass

    def build_receiptdocumentreferences(self) -> None:
        pass

    def build_originatordocumentreferences(self) -> None:
        pass

    def build_contractdocumentreferences(self) -> None:
        pass

    def build_additionaldocumentreferences(self) -> None:
        pass

    def build_accountingsupplierparty(self) -> None:
        pass

    def build_despatchsupplierparty(self) -> None:
        pass

    def build_accountingcustomerparty(self) -> None:
        pass

    def build_deliverycustomerparty(self) -> None:
        pass

    def build_buyercustomerparty(self) -> None:
        pass

    def build_originatorcustomerparty(self) -> None:
        pass

    def build_sellersupplierparty(self) -> None:
        pass

    def build_taxrepresentativeparty(self) -> None:
        pass

    def build_deliveries(self) -> None:
        pass

    def build_shipment(self) -> None:
        pass

    def build_paymentmeans(self) -> None:
        pass

    def build_paymentterm(self) -> None:
        pass

    def build_allowancecharges(self) -> None:
        pass

    def build_taxexchangerate(self) -> None:
        pass

    def build_pricingexchangerate(self) -> None:
        pass

    def build_paymentexchangerate(self) -> None:
        pass

    def build_paymentalternativeexchangerate(self) -> None:
        pass

    def build_taxtotals(self) -> None:
        pass

    def build_withholdingtaxtotals(self) -> None:
        pass

    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        legalmonetarytotal = ET.parse(filepath).getroot().find(
            cacnamespace + 'LegalMonetaryTotal')
        # ['LineExtensionAmount'] = ('cbc', '', 'Zorunlu(1)')
        lineextensionamount = legalmonetarytotal.find(cbcnamespace + 'LineExtensionAmount')
        self._product.add({
            'legalmonetarytotal_lineextensionamount': lineextensionamount.text
        })
        # ['currencyID'] = ('', '', 'Zorunlu(1)')
        self._product.add({
            'legalmonetarytotal_lineextensionamount_currencyid': lineextensionamount.attrib.get(
                'currencyID')
        })
        # ['TaxExclusiveAmount'] = ('cbc', '', 'Zorunlu(1)')
        taxexclusiveamount = legalmonetarytotal.find(cbcnamespace + 'TaxExclusiveAmount')
        self._product.add({
            'legalmonetarytotal_taxexclusiveamount': taxexclusiveamount.text
        })
        # ['currencyID'] = ('', '', 'Zorunlu(1)')
        self._product.add({
            'legalmonetarytotal_taxexclusiveamount_currencyid': taxexclusiveamount.attrib.get(
                'currencyID')
        })
        # ['TaxInclusiveAmount'] = ('cbc', '', 'Zorunlu(1)')
        taxinclusiveamount = legalmonetarytotal.find(cbcnamespace + 'TaxInclusiveAmount')
        self._product.add({
            'legalmonetarytotal_taxinclusiveamount': taxinclusiveamount.text
        })
        # ['currencyID'] = ('', '', 'Zorunlu(1)')
        self._product.add({
            'legalmonetarytotal_taxinclusiveamount_currencyid': taxinclusiveamount.attrib.get(
                'currencyID')
        })
        # ['AllowanceTotalAmount'] = ('cbc', '', 'Seçimli (0...1)')
        allowancetotalamount = legalmonetarytotal.find(cbcnamespace + 'AllowanceTotalAmount')
        if allowancetotalamount is not None:
            self._product.add({
                'legalmonetarytotal_allowancetotalamount': allowancetotalamount.text
            })
            # ['currencyID'] = ('', '', 'Zorunlu(1)')
            self._product.add({
                'legalmonetarytotal_allowancetotalamount_currencyid': allowancetotalamount.attrib.get(
                    'currencyID')
            })
        # ['ChargeTotalAmount'] = ('cbc', '', 'Seçimli (0...1)')
        chargetotalamount = legalmonetarytotal.find(cbcnamespace + 'ChargeTotalAmount')
        if chargetotalamount is not None:
            self._product.add({
                'legalmonetarytotal_chargetotalamount': chargetotalamount.text
            })
            # ['currencyID'] = ('', '', 'Zorunlu(1)')
            self._product.add({
                'legalmonetarytotal_chargetotalamount_currencyid': chargetotalamount.attrib.get(
                    'currencyID')
            })
        # ['PayableRoundingAmount'] = ('cbc', '', 'Seçimli (0...1)')
        payableroundingamount = legalmonetarytotal.find(cbcnamespace + 'PayableRoundingAmount')
        if payableroundingamount is not None:
            self._product.add({
                'legalmonetarytotal_payableroundingamount': payableroundingamount.text
            })
            # ['currencyID'] = ('', '', 'Zorunlu(1)')
            self._product.add({
                'legalmonetarytotal_payableroundingamount_currencyid': payableroundingamount.attrib.get(
                    'currencyID')
            })
        # ['PayableAmount'] = ('cbc', '', 'Zorunlu(1)')
        payableamount = legalmonetarytotal.find(cbcnamespace + 'PayableAmount')
        if payableamount is not None:
            self._product.add({
                'legalmonetarytotal_payableamount': payableamount.text
            })
            # ['currencyID'] = ('', '', 'Zorunlu(1)')
            self._product.add({
                'legalmonetarytotal_payableamount_currencyid': payableamount.attrib.get(
                    'currencyID')
            })

    def build_invoicelines(self) -> None:
        pass

    def build_despatchlines(self) -> None:
        pass
