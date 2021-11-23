import xml.etree.ElementTree as ET

from trebelge.trebelge.TRUBLInvoiceBuilder.TRUBLBuilder import TRUBLBuilder
from trebelge.trebelge.TRUBLInvoiceBuilder.TRUBLInvoice import TRUBLInvoice


class TRUBLInvoiceBuilder(TRUBLBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self, uuid_: str) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self._set_product(uuid_)

    def _reset(self) -> None:
        self._product = None

    def _set_product(self, uuid_: str):
        self._product = TRUBLInvoice(uuid_)

    @property
    def product(self) -> TRUBLInvoice:
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
        self._reset()
        return product

    def build_ublversionid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'ublversionid': ET.parse(filepath).getroot().find(
                cbcnamespace + 'UBLVersionID').text
        })

    def build_customizationid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'customizationid': ET.parse(filepath).getroot().find(
                cbcnamespace + 'CustomizationID').text
        })

    def build_profileid(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'profileid': ET.parse(filepath).getroot().find(
                cbcnamespace + 'ProfileID').text
        })

    def build_id(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'id': ET.parse(filepath).getroot().find(
                cbcnamespace + 'ID').text
        })

    def build_copyindicator(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'copyindicator': ET.parse(filepath).getroot().find(
                cbcnamespace + 'CopyIndicator').text
        })

    def build_issuedate(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'issuedate': ET.parse(filepath).getroot().find(
                cbcnamespace + 'IssueDate').text
        })

    def build_issuetime(self, filepath: str, cbcnamespace: str) -> None:
        issuetime = ET.parse(filepath).getroot().find(
            cbcnamespace + 'IssueTime').text
        if issuetime is not None:
            self._product.add({
                'issuetime': issuetime
            })

    def build_invoicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        self._product.add({
            'invoicetypecode': ET.parse(filepath).getroot().find(
                cbcnamespace + 'InvoiceTypeCode').text
        })

    def build_despatchadvicetypecode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_notes(self, filepath: str, cbcnamespace: str) -> None:
        invoice.as_dict(
            {
                'ublversionid': ET.parse(self.get_context().get_file_path()).getroot().find(
                    self.get_context().get_cbc_namespace() + 'UBLVersionID').text,
                'customizationid': ET.parse(self.get_context().get_file_path()).getroot().find(
                    self.get_context().get_cbc_namespace() + 'CustomizationID').text,
                'qualifications': [
                    {'title': 'Frontend Architect', 'year': '2017'},
                    {'title': 'DevOps Engineer', 'year': '2016'},
                ]
            }
        )

    def build_documentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_taxcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_pricingcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_paymentcurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_paymentalternativecurrencycode(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_accountingcost(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_linecountnumeric(self, filepath: str, cbcnamespace: str) -> None:
        pass

    def build_invoiceperiod(self) -> None:
        pass

    def build_orderreference(self) -> None:
        pass

    def build_orderreferences(self) -> None:
        pass

    def build_billingreferences(self) -> None:
        pass

    def build_despatchdocumentreferences(self) -> None:
        pass

    def build_receiptdocumentreferences(self) -> None:
        pass

    def build_originatordocumentreferences(self) -> None:
        pass

    def build_contractdocumentreferences(self) -> None:
        pass

    def build_additionaldocumentreferences(self) -> None:
        pass

    def build_accountingsupplierparty(self) -> None:
        pass

    def build_despatchsupplierparty(self) -> None:
        pass

    def build_accountingcustomerparty(self) -> None:
        pass

    def build_deliverycustomerparty(self) -> None:
        pass

    def build_buyercustomerparty(self) -> None:
        pass

    def build_originatorcustomerparty(self) -> None:
        pass

    def build_sellersupplierparty(self) -> None:
        pass

    def build_taxrepresentativeparty(self) -> None:
        pass

    def build_deliveries(self) -> None:
        pass

    def build_shipment(self) -> None:
        pass

    def build_paymentmeans(self) -> None:
        pass

    def build_paymentterm(self) -> None:
        pass

    def build_allowancecharges(self) -> None:
        pass

    def build_taxexchangerate(self) -> None:
        pass

    def build_pricingexchangerate(self) -> None:
        pass

    def build_paymentexchangerate(self) -> None:
        pass

    def build_paymentalternativeexchangerate(self) -> None:
        pass

    def build_taxtotals(self) -> None:
        pass

    def build_withholdingtaxtotals(self) -> None:
        pass

    def build_legalmonetarytotal(self) -> None:
        pass

    def build_invoicelines(self) -> None:
        pass

    def build_despatchlines(self) -> None:
        pass
