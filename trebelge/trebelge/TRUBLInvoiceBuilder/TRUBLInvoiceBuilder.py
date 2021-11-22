from trebelge.trebelge.TRUBLInvoiceBuilder.TRUBLBuilder import TRUBLBuilder


class TRUBLInvoiceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def produce_part_ublversionid(self) -> None:
        pass

    def produce_part_customizationid(self) -> None:
        pass

    def produce_part_profileid(self) -> None:
        pass

    def produce_part_id(self) -> None:
        pass

    def produce_part_copyindicator(self) -> None:
        pass

    def produce_part_uuid(self) -> None:
        pass

    def produce_part_issuedate(self) -> None:
        pass

    def produce_part_issuetime(self) -> None:
        pass

    def produce_part_invoicetypecode(self) -> None:
        pass

    def produce_part_despatchadvicetypecode(self) -> None:
        pass

    def produce_part_notes(self) -> None:
        pass

    def produce_part_documentcurrencycode(self) -> None:
        pass

    def produce_part_taxcurrencycode(self) -> None:
        pass

    def produce_part_pricingcurrencycode(self) -> None:
        pass

    def produce_part_paymentcurrencycode(self) -> None:
        pass

    def produce_part_paymentalternativecurrencycode(self) -> None:
        pass

    def produce_part_accountingcost(self) -> None:
        pass

    def produce_part_linecountnumeric(self) -> None:
        pass

    def produce_part_invoiceperiod(self) -> None:
        pass

    def produce_part_orderreference(self) -> None:
        pass

    def produce_part_orderreferences(self) -> None:
        pass

    def produce_part_billingreferences(self) -> None:
        pass

    def produce_part_despatchdocumentreferences(self) -> None:
        pass

    def produce_part_receiptdocumentreferences(self) -> None:
        pass

    def produce_part_originatordocumentreferences(self) -> None:
        pass

    def produce_part_contractdocumentreferences(self) -> None:
        pass

    def produce_part_additionaldocumentreferences(self) -> None:
        pass

    def produce_part_accountingsupplierparty(self) -> None:
        pass

    def produce_part_despatchsupplierparty(self) -> None:
        pass

    def produce_part_accountingcustomerparty(self) -> None:
        pass

    def produce_part_deliverycustomerparty(self) -> None:
        pass

    def produce_part_buyercustomerparty(self) -> None:
        pass

    def produce_part_originatorcustomerparty(self) -> None:
        pass

    def produce_part_sellersupplierparty(self) -> None:
        pass

    def produce_part_taxrepresentativeparty(self) -> None:
        pass

    def produce_part_deliveries(self) -> None:
        pass

    def produce_part_shipment(self) -> None:
        pass

    def produce_part_paymentmeans(self) -> None:
        pass

    def produce_part_paymentterm(self) -> None:
        pass

    def produce_part_allowancecharges(self) -> None:
        pass

    def produce_part_taxexchangerate(self) -> None:
        pass

    def produce_part_pricingexchangerate(self) -> None:
        pass

    def produce_part_paymentexchangerate(self) -> None:
        pass

    def produce_part_paymentalternativeexchangerate(self) -> None:
        pass

    def produce_part_taxtotals(self) -> None:
        pass

    def produce_part_withholdingtaxtotals(self) -> None:
        pass

    def produce_part_legalmonetarytotal(self) -> None:
        pass

    def produce_part_invoicelines(self) -> None:
        pass

    def produce_part_despatchlines(self) -> None:
        pass

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
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
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")
