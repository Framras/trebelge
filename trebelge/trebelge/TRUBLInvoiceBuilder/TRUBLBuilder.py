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
    def produce_part_ublversionid(self, filepath: str, cbcnamespace: str) -> None:
        # ['UBLVersionID'] = ('cbc', 'ublversionid', 'Zorunlu (1)')
        pass

    @abstractmethod
    def produce_part_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        # ['CustomizationID'] = ('cbc', 'customizationid', 'Zorunlu (1)')
        pass

    @abstractmethod
    def produce_part_profileid(self, filepath: str, cbcnamespace: str) -> None:
        # ['ProfileID'] = ('cbc', 'profileid', 'Zorunlu (1)')
        pass

    @abstractmethod
    def produce_part_id(self, filepath: str, cbcnamespace: str) -> None:
        # ['ID'] = ('cbc', 'id', 'Zorunlu (1)')
        pass

    @abstractmethod
    def produce_part_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        # ['CopyIndicator'] = ('cbc', 'copyindicator', 'Zorunlu (1)')
        pass

    @abstractmethod
    def produce_part_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        # ['IssueDate'] = ('cbc', 'issuedate', 'Zorunlu (1)')
        pass

    @abstractmethod
    def produce_part_issuetime(self, filepath: str, cbcnamespace: str) -> None:
        # ['IssueTime'] = ('cbc', 'issuetime', 'Seçimli (0...1)')
        pass

    @abstractmethod
    def produce_part_invoicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_notes(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_documentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_taxcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_pricingcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_paymentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_paymentalternativecurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_accountingcost(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_linecountnumeric(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def produce_part_invoiceperiod(self) -> None:
        pass

    @abstractmethod
    def produce_part_orderreference(self) -> None:
        pass

    @abstractmethod
    def produce_part_orderreferences(self) -> None:
        pass

    @abstractmethod
    def produce_part_billingreferences(self) -> None:
        pass

    @abstractmethod
    def produce_part_despatchdocumentreferences(self) -> None:
        pass

    @abstractmethod
    def produce_part_receiptdocumentreferences(self) -> None:
        pass

    @abstractmethod
    def produce_part_originatordocumentreferences(self) -> None:
        pass

    @abstractmethod
    def produce_part_contractdocumentreferences(self) -> None:
        pass

    @abstractmethod
    def produce_part_additionaldocumentreferences(self) -> None:
        pass

    @abstractmethod
    def produce_part_accountingsupplierparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_despatchsupplierparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_accountingcustomerparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_deliverycustomerparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_buyercustomerparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_originatorcustomerparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_sellersupplierparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_taxrepresentativeparty(self) -> None:
        pass

    @abstractmethod
    def produce_part_deliveries(self) -> None:
        pass

    @abstractmethod
    def produce_part_shipment(self) -> None:
        pass

    @abstractmethod
    def produce_part_paymentmeans(self) -> None:
        pass

    @abstractmethod
    def produce_part_paymentterm(self) -> None:
        pass

    @abstractmethod
    def produce_part_allowancecharges(self) -> None:
        pass

    @abstractmethod
    def produce_part_taxexchangerate(self) -> None:
        pass

    @abstractmethod
    def produce_part_pricingexchangerate(self) -> None:
        pass

    @abstractmethod
    def produce_part_paymentexchangerate(self) -> None:
        pass

    @abstractmethod
    def produce_part_paymentalternativeexchangerate(self) -> None:
        pass

    @abstractmethod
    def produce_part_taxtotals(self) -> None:
        pass

    @abstractmethod
    def produce_part_withholdingtaxtotals(self) -> None:
        pass

    @abstractmethod
    def produce_part_legalmonetarytotal(self) -> None:
        pass

    @abstractmethod
    def produce_part_invoicelines(self) -> None:
        pass

    @abstractmethod
    def produce_part_despatchlines(self) -> None:
        pass
