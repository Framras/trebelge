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
        # ['UBLVersionID'] = ('cbc', 'ublversionid', 'Zorunlu (1)')
        pass

    @abstractmethod
    def build_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        # ['CustomizationID'] = ('cbc', 'customizationid', 'Zorunlu (1)')
        pass

    @abstractmethod
    def build_profileid(self, filepath: str, cbcnamespace: str) -> None:
        # ['ProfileID'] = ('cbc', 'profileid', 'Zorunlu (1)')
        pass

    @abstractmethod
    def build_id(self, filepath: str, cbcnamespace: str) -> None:
        # ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        pass

    @abstractmethod
    def build_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        # ['CopyIndicator'] = ('cbc', 'copyindicator', 'Zorunlu (1)')
        pass

    @abstractmethod
    def build_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        # ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu (1)')
        pass

    @abstractmethod
    def build_issuetime(self, filepath: str, cbcnamespace: str) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        pass

    @abstractmethod
    def build_invoicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        # ['InvoiceTypeCode'] = ('cbc', 'invoicetypecode', 'Zorunlu (1)')
        pass

    @abstractmethod
    def build_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_notes(self, filepath: str, cbcnamespace: str) -> None:
        # ['Note'] = ('cbc', 'notes', 'Seçimli (0...n)', 'note')
        pass

    @abstractmethod
    def build_documentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_taxcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_pricingcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentalternativecurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_accountingcost(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_linecountnumeric(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_invoiceperiod(self) -> None:
        pass

    @abstractmethod
    def build_orderreference(self) -> None:
        pass

    @abstractmethod
    def build_orderreferences(self) -> None:
        pass

    @abstractmethod
    def build_billingreferences(self) -> None:
        pass

    @abstractmethod
    def build_despatchdocumentreferences(self) -> None:
        pass

    @abstractmethod
    def build_receiptdocumentreferences(self) -> None:
        pass

    @abstractmethod
    def build_originatordocumentreferences(self) -> None:
        pass

    @abstractmethod
    def build_contractdocumentreferences(self) -> None:
        pass

    @abstractmethod
    def build_additionaldocumentreferences(self) -> None:
        pass

    @abstractmethod
    def build_accountingsupplierparty(self) -> None:
        pass

    @abstractmethod
    def build_despatchsupplierparty(self) -> None:
        pass

    @abstractmethod
    def build_accountingcustomerparty(self) -> None:
        pass

    @abstractmethod
    def build_deliverycustomerparty(self) -> None:
        pass

    @abstractmethod
    def build_buyercustomerparty(self) -> None:
        pass

    @abstractmethod
    def build_originatorcustomerparty(self) -> None:
        pass

    @abstractmethod
    def build_sellersupplierparty(self) -> None:
        pass

    @abstractmethod
    def build_taxrepresentativeparty(self) -> None:
        pass

    @abstractmethod
    def build_deliveries(self) -> None:
        pass

    @abstractmethod
    def build_shipment(self) -> None:
        pass

    @abstractmethod
    def build_paymentmeans(self) -> None:
        pass

    @abstractmethod
    def build_paymentterm(self) -> None:
        pass

    @abstractmethod
    def build_allowancecharges(self) -> None:
        pass

    @abstractmethod
    def build_taxexchangerate(self) -> None:
        pass

    @abstractmethod
    def build_pricingexchangerate(self) -> None:
        pass

    @abstractmethod
    def build_paymentexchangerate(self) -> None:
        pass

    @abstractmethod
    def build_paymentalternativeexchangerate(self) -> None:
        pass

    @abstractmethod
    def build_taxtotals(self) -> None:
        pass

    @abstractmethod
    def build_withholdingtaxtotals(self) -> None:
        pass

    @abstractmethod
    def build_legalmonetarytotal(self) -> None:
        pass

    @abstractmethod
    def build_invoicelines(self) -> None:
        pass

    @abstractmethod
    def build_despatchlines(self) -> None:
        pass
