from abc import ABC, abstractmethod
from typing import Any


class TRUBLBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> Any:
        pass

    @abstractmethod
    def build_ublversionid(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_profileid(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_id(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_issuetime(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_invoicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    @abstractmethod
    def build_note(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
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
    def build_invoiceperiod(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_orderreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_billingreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_despatchdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_receiptdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_originatordocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_contractdocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_additionaldocumentreference(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_accountingsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_despatchsupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_accountingcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_deliverycustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_buyercustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_sellersupplierparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_originatorcustomerparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_taxrepresentativeparty(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_delivery(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_shipment(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentmeans(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentterms(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_allowancecharge(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_taxexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_pricingexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentalternativeexchangerate(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_taxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_withholdingtaxtotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_legalmonetarytotal(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_invoiceline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_despatchline(self, filepath: str, cbcnamespace: str, cacnamespace: str) -> None:
        pass
