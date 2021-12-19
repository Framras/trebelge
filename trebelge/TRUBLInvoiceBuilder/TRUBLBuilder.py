from abc import ABC, abstractmethod


class TRUBLBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractmethod
    def set_product(self, uuid_: str) -> None:
        pass

    @abstractmethod
    def get_product(self) -> None:
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
        ['DespatchAdviceTypeCode'] = ('cbc', 'despatchadvicetypecode', 'Zorunlu (1)')
        """
        pass

    @abstractmethod
    def build_note(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['Note'] = ('cbc', 'note', 'Seçimli (0...n)', 'note')
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
        ['InvoicePeriod'] = ('cac', Period(), 'Seçimli (0...1)', 'invoiceperiod')
        """
        pass

    @abstractmethod
    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['OrderReference'] = ('cac', OrderReference(), 'Seçimli (0...1)', 'orderreference')
        """
        pass

    @abstractmethod
    def build_billingreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['BillingReference'] = ('cac', BillingReference(), 'Seçimli (0...n)', 'billingreference')
        """
        pass

    @abstractmethod
    def build_despatchdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['DespatchDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'despatchdocumentreference')
        """
        pass

    @abstractmethod
    def build_receiptdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['ReceiptDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'receiptdocumentreference')
        """
        pass

    @abstractmethod
    def build_originatordocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['OriginatorDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'originatordocumentreference')
        """
        pass

    @abstractmethod
    def build_contractdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['ContractDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'contractdocumentreference')
        """
        pass

    @abstractmethod
    def build_additionaldocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AdditionalDocumentReference'] = ('cac', DocumentReference(), 'Seçimli (0...n)', 'additionaldocumentreference')
        """
        pass

    @abstractmethod
    def build_accountingsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AccountingSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'accountingsupplierparty')
        """
        pass

    @abstractmethod
    def build_despatchsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['DespatchSupplierParty'] = ('cac', SupplierParty(), 'Zorunlu (1)', 'despatchsupplierparty')
        """
        pass

    @abstractmethod
    def build_accountingcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AccountingCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'accountingcustomerparty')
        """
        pass

    @abstractmethod
    def build_deliverycustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['DeliveryCustomerParty'] = ('cac', CustomerParty(), 'Zorunlu (1)', 'deliverycustomerparty')
        """
        pass

    @abstractmethod
    def build_buyercustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['BuyerCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'buyercustomerparty')
        """
        pass

    @abstractmethod
    def build_sellersupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['SellerSupplierParty'] = ('cac', SupplierParty(), 'Seçimli (0..1)', 'sellersupplierparty')
        """
        pass

    @abstractmethod
    def build_originatorcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['OriginatorCustomerParty'] = ('cac', CustomerParty(), 'Seçimli (0..1)', 'originatorcustomerparty')
        """
        pass

    @abstractmethod
    def build_taxrepresentativeparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['TaxRepresentativeParty'] = ('cac', Party(), 'Seçimli (0..1)', 'taxrepresentativeparty')
        """
        pass

    @abstractmethod
    def build_delivery(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['Delivery'] = ('cac', Delivery(), 'Seçimli (0...n)', 'delivery')
        """
        pass

    @abstractmethod
    def build_shipment(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['Shipment'] = ('cac', Shipment(), 'Seçimli (0...n)', 'shipment')
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
    def build_allowancecharge(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['AllowanceCharge'] = ('cac', AllowanceCharge(), 'Seçimli (0...n)', 'allowancecharge')
        """
        pass

    @abstractmethod
    def build_taxexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['TaxExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'taxexchangerate')
        """
        pass

    @abstractmethod
    def build_pricingexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PricingExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'pricingexchangerate')
        """
        pass

    @abstractmethod
    def build_paymentexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PaymentExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentexchangerate')
        """
        pass

    @abstractmethod
    def build_paymentalternativeexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['PaymentAlternativeExchangeRate'] = ('cac', ExchangeRate(), 'Seçimli (0..1)', 'paymentalternativeexchangerate')
        """
        pass

    @abstractmethod
    def build_taxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['TaxTotal'] = ('cac', TaxTotal(), 'Zorunlu (1...n)', 'taxtotal')
        """
        pass

    @abstractmethod
    def build_withholdingtaxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['WithholdingTaxTotal'] = ('cac', TaxTotal(), 'Seçimli (0...n)', 'withholdingtaxtotal')
        """
        pass

    @abstractmethod
    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['LegalMonetaryTotal'] = ('cac', MonetaryTotal(), 'Zorunlu (1)', 'legalmonetarytotal')
        """
        pass

    @abstractmethod
    def build_invoiceline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['InvoiceLine'] = ('cac', InvoiceLine(), 'Zorunlu (1...n)', 'invoiceline')
        """
        pass

    @abstractmethod
    def build_despatchline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        """
        ['DespatchLine'] = ('cac', DespatchLine(), 'Zorunlu (1...n)', 'despatchline')
        """
        pass
