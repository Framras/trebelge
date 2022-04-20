from abc import ABC, abstractmethod
from typing import Any


class TRUBLBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def build_issuetime(self) -> None:
        pass

    @abstractmethod
    def build_note(self) -> None:
        pass

    @abstractmethod
    def build_invoiceperiod(self) -> None:
        pass

    @abstractmethod
    def build_orderreference(self) -> None:
        pass

    @abstractmethod
    def build_billingreference(self) -> None:
        pass

    @abstractmethod
    def build_despatchdocumentreference(self) -> None:
        pass

    @abstractmethod
    def build_receiptdocumentreference(self) -> None:
        pass

    @abstractmethod
    def build_originatordocumentreference(self) -> None:
        pass

    @abstractmethod
    def build_contractdocumentreference(self) -> None:
        pass

    @abstractmethod
    def build_additionaldocumentreference(self) -> None:
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
    def build_sellersupplierparty(self) -> None:
        pass

    @abstractmethod
    def build_originatorcustomerparty(self) -> None:
        pass

    @abstractmethod
    def build_taxrepresentativeparty(self) -> None:
        pass

    @abstractmethod
    def build_delivery(self) -> None:
        pass

    @abstractmethod
    def build_shipment(self) -> None:
        pass

    @abstractmethod
    def build_paymentmeans(self) -> None:
        pass

    @abstractmethod
    def build_paymentterms(self) -> None:
        pass

    @abstractmethod
    def build_allowancecharge(self) -> None:
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
    def build_taxtotal(self) -> None:
        pass

    @abstractmethod
    def build_withholdingtaxtotal(self) -> None:
        pass

    @abstractmethod
    def build_legalmonetarytotal(self) -> None:
        pass

    @abstractmethod
    def build_invoiceline(self) -> None:
        pass

    @abstractmethod
    def build_despatchline(self) -> None:
        pass

    @abstractmethod
    def build_receiptline(self) -> None:
        pass

    @abstractmethod
    def build_creditnoteline(self) -> None:
        pass

    @abstractmethod
    def build_senderparty(self) -> None:
        pass

    @abstractmethod
    def build_receiverparty(self) -> None:
        pass

    @abstractmethod
    def build_documentresponse(self) -> None:
        pass

    @abstractmethod
    def get_document(self) -> Any:
        pass
