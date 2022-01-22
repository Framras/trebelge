from trebelge.TRUBLBuilder import TRUBLBuilder


class TRUBLDirector:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self, builder) -> None:
        self._builder = builder

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
        self.builder.reset()
        self.builder.build_issuetime()
        self.builder.build_note()
        self.builder.build_invoiceperiod()
        self.builder.build_orderreference()
        self.builder.build_billingreference()
        self.builder.build_despatchdocumentreference()
        self.builder.build_receiptdocumentreference()
        self.builder.build_originatordocumentreference()
        self.builder.build_contractdocumentreference()
        self.builder.build_additionaldocumentreference()
        self.builder.build_accountingsupplierparty()
        self.builder.build_accountingcustomerparty()
        self.builder.build_buyercustomerparty()
        self.builder.build_sellersupplierparty()
        self.builder.build_taxrepresentativeparty()
        self.builder.build_delivery()
        self.builder.build_paymentmeans()
        self.builder.build_paymentterms()
        self.builder.build_allowancecharge()
        self.builder.build_taxexchangerate()
        self.builder.build_pricingexchangerate()
        self.builder.build_paymentexchangerate()
        self.builder.build_paymentalternativeexchangerate()
        self.builder.build_taxtotal()
        self.builder.build_withholdingtaxtotal()
        self.builder.build_legalmonetarytotal()
        self.builder.build_invoiceline()

    def make_tr_ubl_despatchadvice(self) -> None:
        self.builder.reset()
        self.builder.build_issuetime()
        self.builder.build_note()
        self.builder.build_orderreference()
        self.builder.build_additionaldocumentreference()
        self.builder.build_despatchsupplierparty()
        self.builder.build_deliverycustomerparty()
        self.builder.build_buyercustomerparty()
        self.builder.build_sellersupplierparty()
        self.builder.build_originatorcustomerparty()
        self.builder.build_shipment()
        self.builder.build_despatchline()

    def make_tr_ubl_applicationresponse(self) -> None:
        self.builder.reset()
        self.builder.build_issuetime()
        self.builder.build_note()
        self.builder.build_senderparty()
        self.builder.build_receiverparty()
        self.builder.build_documentresponse()
