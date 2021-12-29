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
    def build_ublversionid(self) -> None:
        pass

    @abstractmethod
    def build_customizationid(self) -> None:
        pass

    @abstractmethod
    def build_profileid(self) -> None:
        pass

    @abstractmethod
    def build_id(self) -> None:
        pass

    @abstractmethod
    def build_copyindicator(self) -> None:
        pass

    @abstractmethod
    def build_issuedate(self) -> None:
        pass

    @abstractmethod
    def build_issuetime(self) -> None:
        pass

    @abstractmethod
    def build_invoicetypecode(self) -> None:
        pass

    @abstractmethod
    def build_despatchadvicetypecode(self) -> None:
        pass

    @abstractmethod
    def build_note(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_documentcurrencycode(self) -> None:
        pass

    @abstractmethod
    def build_taxcurrencycode(self) -> None:
        pass

    @abstractmethod
    def build_pricingcurrencycode(self) -> None:
        pass

    @abstractmethod
    def build_paymentcurrencycode(self) -> None:
        pass

    @abstractmethod
    def build_paymentalternativecurrencycode(self) -> None:
        pass

    @abstractmethod
    def build_accountingcost(self) -> None:
        pass

    @abstractmethod
    def build_linecountnumeric(self) -> None:
        pass

    @abstractmethod
    def build_invoiceperiod(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_orderreference(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_billingreference(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_despatchdocumentreference(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_receiptdocumentreference(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_originatordocumentreference(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_contractdocumentreference(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_additionaldocumentreference(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_accountingsupplierparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_despatchsupplierparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_accountingcustomerparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_deliverycustomerparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_buyercustomerparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_sellersupplierparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_originatorcustomerparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_taxrepresentativeparty(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_delivery(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_shipment(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentmeans(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentterms(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_allowancecharge(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_taxexchangerate(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_pricingexchangerate(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentexchangerate(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_paymentalternativeexchangerate(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_taxtotal(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_withholdingtaxtotal(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_legalmonetarytotal(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_invoiceline(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass

    @abstractmethod
    def build_despatchline(self, cbcnamespace: str, cacnamespace: str) -> None:
        pass
