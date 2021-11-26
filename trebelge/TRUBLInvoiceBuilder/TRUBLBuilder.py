from abc import ABC, abstractmethod


class TRUBLBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def build_ublversionid(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['UBLVersionID'] = ('cbc', 'ublversionid', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['CustomizationID'] = ('cbc', 'customizationid', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_profileid(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['ProfileID'] = ('cbc', 'profileid', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_id(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['CopyIndicator'] = ('cbc', 'copyindicator', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_issuetime(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_invoicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['InvoiceTypeCode'] = ('cbc', 'invoicetypecode', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        """

        """
        pass

    @abstractmethod
    def build_notes(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['Note'] = ('cbc', 'notes', 'Seçimli (0...n)', 'note')
        """
        pass

    @abstractmethod
    def build_documentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['DocumentCurrencyCode'] = ('cbc', 'documentcurrencycode', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_taxcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['TaxCurrencyCode'] = ('cbc', 'taxcurrencycode', 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_pricingcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['PricingCurrencyCode'] = ('cbc', 'pricingcurrencycode', 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_paymentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['PaymentCurrencyCode'] = ('cbc', 'paymentcurrencycode', 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_paymentalternativecurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['PaymentAlternativeCurrencyCode'] = ('cbc', 'paymentalternativecurrencycode', 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_accountingcost(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['AccountingCost'] = ('cbc', 'accountingcost', 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_linecountnumeric(self, filepath: str, cbcnamespace: str) -> None:
        """
        ['LineCountNumeric'] = ('cbc', 'linecountnumeric', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_invoiceperiod(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...1)')
        """
        pass

    @abstractmethod
    def build_orderreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """

        """
        pass

    @abstractmethod
    def build_billingreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['BillingReference'] = ('cac', BillingReference(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_despatchdocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_receiptdocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_originatordocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['OriginatorDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_contractdocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_additionaldocumentreferences(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AdditionalDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', True, False, False, '')
        """
        pass

    @abstractmethod
    def build_accountingsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_despatchsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """

        """
        pass

    @abstractmethod
    def build_accountingcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_deliverycustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """

        """
        pass

    @abstractmethod
    def build_buyercustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['BuyerCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_originatorcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """

        """
        pass

    @abstractmethod
    def build_sellersupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['SellerSupplierParty'] = ('cac', SupplierParty(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_taxrepresentativeparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['TaxRepresentativeParty'] = ('cac', Party(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_deliveries(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_shipment(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """

        """
        pass

    @abstractmethod
    def build_paymentmeans(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PaymentMeans'] = ('cac', PaymentMeans(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_paymentterms(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PaymentTerms'] = ('cac', PaymentTerms(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_allowancecharges(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_taxexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_pricingexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_paymentexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_paymentalternativeexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)')
        """
        pass

    @abstractmethod
    def build_taxtotals(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)')
        """
        pass

    @abstractmethod
    def build_withholdingtaxtotals(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)')
        """
        pass

    @abstractmethod
    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_invoicelines(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)')
        """
        pass

    @abstractmethod
    def build_despatchlines(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """

        """
        pass
