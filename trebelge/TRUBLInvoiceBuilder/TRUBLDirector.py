from apps.trebelge.trebelge.TRUBLInvoiceBuilder import TRUBLBuilder


class TRUBLDirector:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self, builder) -> None:
        self._builder: TRUBLBuilder = builder

    @property
    def builder(self) -> TRUBLBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: TRUBLBuilder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def make_tr_ubl_invoice(self) -> None:
        self.builder.build_ublversionid(self)
        self.builder.build_customizationid(self)
        self.builder.build_profileid(self)
        self.builder.build_id(self)
        self.builder.build_copyindicator(self)
        self.builder.build_issuedate(self)
        self.builder.build_issuetime(self)
        self.builder.build_invoicetypecode(self)
        self.builder.build_note(self)
        self.builder.build_documentcurrencycode(self)
        self.builder.build_taxcurrencycode(self)
        self.builder.build_pricingcurrencycode(self)
        self.builder.build_paymentcurrencycode(self)
        self.builder.build_paymentalternativecurrencycode(self)
        self.builder.build_accountingcost(self)
        self.builder.build_linecountnumeric(self)
        self.builder.build_invoiceperiod(self)
        self.builder.build_orderreference(self)
        self.builder.build_billingreference(self)
        self.builder.build_despatchdocumentreference(self)
        self.builder.build_receiptdocumentreference(self)
        self.builder.build_originatordocumentreference(self)
        self.builder.build_contractdocumentreference(self)
        self.builder.build_additionaldocumentreference(self)
        self.builder.build_accountingsupplierparty(self)
        self.builder.build_accountingcustomerparty(self)
        self.builder.build_buyercustomerparty(self)
        self.builder.build_sellersupplierparty(self)
        self.builder.build_taxrepresentativeparty(self)
        self.builder.build_delivery(self)
        self.builder.build_paymentmeans(self)
        self.builder.build_paymentterms(self)
        self.builder.build_allowancecharge(self)
        self.builder.build_taxexchangerate(self)
        self.builder.build_pricingexchangerate(self)
        self.builder.build_paymentexchangerate(self)
        self.builder.build_paymentalternativeexchangerate(self)
        self.builder.build_taxtotal(self)
        self.builder.build_withholdingtaxtotal(self)
        self.builder.build_legalmonetarytotal(self)
        self.builder.build_invoiceline(self)

    def make_tr_ubl_despatchadvice(self) -> None:
        self.builder.build_ublversionid(self)
        self.builder.build_customizationid(self)
        self.builder.build_profileid(self)
        self.builder.build_id(self)
        self.builder.build_copyindicator(self)
        self.builder.build_issuedate(self)
        self.builder.build_issuetime(self)
        self.builder.build_despatchadvicetypecode(self)
        self.builder.build_note(self)
        self.builder.build_linecountnumeric(self)
        self.builder.build_orderreference(self)
        self.builder.build_additionaldocumentreference(self)
        self.builder.build_despatchsupplierparty(self)
        self.builder.build_deliverycustomerparty(self)
        self.builder.build_buyercustomerparty(self)
        self.builder.build_sellersupplierparty(self)
        self.builder.build_originatorcustomerparty(self)
        self.builder.build_shipment(self)
        self.builder.build_despatchline(self)
