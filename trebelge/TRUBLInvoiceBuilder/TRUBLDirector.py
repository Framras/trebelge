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

    def _get_file_path(self):
        return self._file_path

    def _set_namespaces(self):
        # read all namespaces
        self._namespaces = dict([node for _, node in ET.iterparse(self._get_file_path(), events=['start-ns'])])
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

    def _get_cac_namespace(self):
        return self._cac_namespace

    def _set_cbc_namespace(self):
        self._cbc_namespace = '{' + self._get_namespaces().get('cbc') + '}'

    def _get_cbc_namespace(self):
        return self._cbc_namespace

    def _set_uuid(self):
        self._uuid = ET.parse(self._get_file_path()).getroot().find(self._get_cbc_namespace() + 'UUID').text

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
        self.builder.build_ublversionid(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_customizationid(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_profileid(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_id(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_copyindicator(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_issuedate(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_issuetime(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_invoicetypecode(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_note(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_documentcurrencycode(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_taxcurrencycode(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_pricingcurrencycode(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_paymentcurrencycode(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_paymentalternativecurrencycode(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_accountingcost(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_linecountnumeric(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_invoiceperiod(self._get_file_path(), self._get_cbc_namespace(), self._get_cac_namespace())
        self.builder.build_orderreference(self._get_file_path(), self._get_cbc_namespace(), self._get_cac_namespace())
        self.builder.build_legalmonetarytotal(self._get_file_path(), self._get_cbc_namespace(),
                                              self._get_cac_namespace())

    def build_tr_ubl_despatchadvice(self) -> None:
        self.builder.build_ublversionid(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_customizationid(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_profileid(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_id(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_copyindicator(self._get_file_path(), self._get_cbc_namespace())
        self.builder.build_issuedate(self._get_file_path(), self._get_cbc_namespace())
