import xml.etree.ElementTree as ET

from trebelge.TRUBLInvoiceBuilder.TRUBLBuilder import TRUBLBuilder


class TRUBLDirector:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """
    _builder: TRUBLBuilder = None
    _file_path: str = ''
    _namespaces = dict()
    _default_namespace: str = ''
    _cac_namespace: str = ''
    _cbc_namespace: str = ''
    _uuid: str = ''

    def set_file_path(self, file_path: str):
        self._file_path = file_path
        self._set_namespaces()

    def _set_namespaces(self):
        # read all namespaces
        self._namespaces = dict([node for _, node in ET.iterparse(self._file_path, events=['start-ns'])])
        self._set_default_namespace()
        self._set_cac_namespace()
        self._set_cbc_namespace()
        self._set_uuid()

    def _get_namespaces(self):
        # return all namespaces
        return self._namespaces

    def _set_default_namespace(self):
        self._default_namespace = '{' + self._get_namespaces().get('') + '}'

    def _get_default_namespace(self):
        return self._default_namespace

    def _set_cac_namespace(self):
        self._cac_namespace = '{' + self._get_namespaces().get('cac') + '}'

    def _set_cbc_namespace(self):
        self._cbc_namespace = '{' + self._get_namespaces().get('cbc') + '}'

    def _set_uuid(self):
        self._uuid = ET.parse(self._file_path).getroot().find(self._cbc_namespace + 'UUID').text

    def get_uuid(self):
        return self._uuid

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

    def build_tr_ubl_invoice(self) -> None:
        self.builder.build_ublversionid(self._file_path, self._cbc_namespace)
        self.builder.build_customizationid(self._file_path, self._cbc_namespace)
        self.builder.build_profileid(self._file_path, self._cbc_namespace)
        self.builder.build_id(self._file_path, self._cbc_namespace)
        self.builder.build_copyindicator(self._file_path, self._cbc_namespace)
        self.builder.build_issuedate(self._file_path, self._cbc_namespace)
        self.builder.build_issuetime(self._file_path, self._cbc_namespace)
        self.builder.build_invoicetypecode(self._file_path, self._cbc_namespace)
        self.builder.build_note(self._file_path, self._cbc_namespace,
                                self._cac_namespace)
        self.builder.build_documentcurrencycode(self._file_path, self._cbc_namespace)
        self.builder.build_taxcurrencycode(self._file_path, self._cbc_namespace)
        self.builder.build_pricingcurrencycode(self._file_path, self._cbc_namespace)
        self.builder.build_paymentcurrencycode(self._file_path, self._cbc_namespace)
        self.builder.build_paymentalternativecurrencycode(self._file_path, self._cbc_namespace)
        self.builder.build_accountingcost(self._file_path, self._cbc_namespace)
        self.builder.build_linecountnumeric(self._file_path, self._cbc_namespace)
        self.builder.build_invoiceperiod(self._file_path, self._cbc_namespace,
                                         self._cac_namespace)
        self.builder.build_orderreference(self._file_path, self._cbc_namespace,
                                          self._cac_namespace)
        self.builder.build_billingreference(self._file_path, self._cbc_namespace,
                                            self._cac_namespace)
        self.builder.build_despatchdocumentreference(self._file_path, self._cbc_namespace,
                                                     self._cac_namespace)
        self.builder.build_receiptdocumentreference(self._file_path, self._cbc_namespace,
                                                    self._cac_namespace)
        self.builder.build_originatordocumentreference(self._file_path, self._cbc_namespace,
                                                       self._cac_namespace)
        self.builder.build_contractdocumentreference(self._file_path, self._cbc_namespace,
                                                     self._cac_namespace)
        self.builder.build_additionaldocumentreference(self._file_path, self._cbc_namespace,
                                                       self._cac_namespace)
        self.builder.build_accountingsupplierparty(self._file_path, self._cbc_namespace,
                                                   self._cac_namespace)
        self.builder.build_accountingcustomerparty(self._file_path, self._cbc_namespace,
                                                   self._cac_namespace)
        self.builder.build_buyercustomerparty(self._file_path, self._cbc_namespace,
                                              self._cac_namespace)
        self.builder.build_sellersupplierparty(self._file_path, self._cbc_namespace,
                                               self._cac_namespace)
        self.builder.build_taxrepresentativeparty(self._file_path, self._cbc_namespace,
                                                  self._cac_namespace)
        self.builder.build_delivery(self._file_path, self._cbc_namespace,
                                    self._cac_namespace)
        self.builder.build_paymentmeans(self._file_path, self._cbc_namespace,
                                        self._cac_namespace)
        self.builder.build_paymentterms(self._file_path, self._cbc_namespace,
                                        self._cac_namespace)
        self.builder.build_allowancecharge(self._file_path, self._cbc_namespace,
                                           self._cac_namespace)
        self.builder.build_taxexchangerate(self._file_path, self._cbc_namespace,
                                           self._cac_namespace)
        self.builder.build_pricingexchangerate(self._file_path, self._cbc_namespace,
                                               self._cac_namespace)
        self.builder.build_paymentexchangerate(self._file_path, self._cbc_namespace,
                                               self._cac_namespace)
        self.builder.build_paymentalternativeexchangerate(self._file_path, self._cbc_namespace,
                                                          self._cac_namespace)
        self.builder.build_taxtotal(self._file_path, self._cbc_namespace,
                                    self._cac_namespace)
        self.builder.build_withholdingtaxtotal(self._file_path, self._cbc_namespace,
                                               self._cac_namespace)
        self.builder.build_legalmonetarytotal(self._file_path, self._cbc_namespace,
                                              self._cac_namespace)
        self.builder.build_invoiceline(self._file_path, self._cbc_namespace,
                                       self._cac_namespace)

    def build_tr_ubl_despatchadvice(self) -> None:
        self.builder.build_ublversionid(self._file_path, self._cbc_namespace)
        self.builder.build_customizationid(self._file_path, self._cbc_namespace)
        self.builder.build_profileid(self._file_path, self._cbc_namespace)
        self.builder.build_id(self._file_path, self._cbc_namespace)
        self.builder.build_copyindicator(self._file_path, self._cbc_namespace)
        self.builder.build_issuedate(self._file_path, self._cbc_namespace)
        self.builder.build_issuetime(self._file_path, self._cbc_namespace)
        self.builder.build_despatchadvicetypecode(self._file_path, self._cbc_namespace)
        self.builder.build_note(self._file_path, self._cbc_namespace)
        self.builder.build_linecountnumeric(self._file_path, self._cbc_namespace)
        self.builder.build_orderreference(self._file_path, self._cbc_namespace,
                                          self._cac_namespace)
        self.builder.build_additionaldocumentreference(self._file_path, self._cbc_namespace,
                                                       self._cac_namespace)
        self.builder.build_despatchsupplierparty(self._file_path, self._cbc_namespace,
                                                 self._cac_namespace)
        self.builder.build_deliverycustomerparty(self._file_path, self._cbc_namespace,
                                                 self._cac_namespace)
        self.builder.build_buyercustomerparty(self._file_path, self._cbc_namespace,
                                              self._cac_namespace)
        self.builder.build_sellersupplierparty(self._file_path, self._cbc_namespace,
                                               self._cac_namespace)
        self.builder.build_originatorcustomerparty(self._file_path, self._cbc_namespace,
                                                   self._cac_namespace)
        self.builder.build_shipment(self._file_path, self._cbc_namespace,
                                    self._cac_namespace)
        self.builder.build_despatchline(self._file_path, self._cbc_namespace,
                                        self._cac_namespace)
