class incomingEfaturaReader():  # The target object of the parser

    def __init__(self, namespaces):
        self.namespaces = namespaces
        self.UBLVersionID = ""  # Zorunlu (1)
        self.is_UBLVersionID_data = False
        self.CustomizationID = ""  # Zorunlu (1)
        self.is_CustomizationID_data = False
        self.ProfileID = ""  # Zorunlu (1)
        self.is_ProfileID_data = False
        self.ID = ""  # Zorunlu (1)
        self.is_ID_data = False
        self.CopyIndicator = ""  # Zorunlu (1)
        self.is_CopyIndicator_data = False
        self.UUID = ""  # Zorunlu (1)
        self.is_UUID_data = False
        self.IssueDate = ""  # Zorunlu (1)
        self.is_IssueDate_data = False
        self.IssueTime = ""  # Seçimli (0...1)
        self.is_IssueTime_data = False
        self.InvoiceTypeCode = ""  # Zorunlu (1)
        self.is_InvoiceTypeCode_data = False
        self.Notes = list()  # Seçimli (0...n)
        self.is_Note_data = False
        self.DocumentCurrencyCode = ""  # Zorunlu (1)
        self.is_DocumentCurrencyCode_data = False
        self.TaxCurrencyCode = ""  # Seçimli (0...1)
        self.is_TaxCurrencyCode_data = False
        self.PricingCurrencyCode = ""  # Seçimli (0...1)
        self.is_PricingCurrencyCode_data = False
        self.LineCountNumeric = ""
        self.is_LineCountNumeric_data = False
        self.return_data = dict()

    def start(self, tag, attrib):  # Called for each opening tag.
        print(self.namespaces)
        if tag == '{' + self.namespaces.get('cbc') + '}UBLVersionID':
            self.is_UBLVersionID_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}CustomizationID':
            self.is_CustomizationID_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}ProfileID':
            self.is_ProfileID_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}ID':
            self.is_ID_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}CopyIndicator':
            self.is_CopyIndicator_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}UUID':
            self.is_UUID_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}IssueDate':
            self.is_IssueDate_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}IssueTime':
            self.is_IssueTime_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}InvoiceTypeCode':
            self.is_InvoiceTypeCode_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}Note':
            self.is_Note_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}DocumentCurrencyCode':
            self.is_DocumentCurrencyCode_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}TaxCurrencyCode':
            self.is_TaxCurrencyCode_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}PricingCurrencyCode':
            self.is_PricingCurrencyCode_data = True
        elif tag == '{' + self.namespaces.get('cbc') + '}LineCountNumeric':
            self.is_LineCountNumeric_data = True

    def end(self, tag):  # Called for each closing tag.
        if tag == '{' + self.namespaces.get('cbc') + '}UBLVersionID':
            self.is_UBLVersionID_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}CustomizationID':
            self.is_CustomizationID_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}ProfileID':
            self.is_ProfileID_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}ID':
            self.is_ID_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}CopyIndicator':
            self.is_CopyIndicator_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}UUID':
            self.is_UUID_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}IssueDate':
            self.is_IssueDate_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}IssueTime':
            self.is_IssueTime_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}InvoiceTypeCode':
            self.is_InvoiceTypeCode_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}Note':
            self.is_Note_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}DocumentCurrencyCode':
            self.is_DocumentCurrencyCode_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}TaxCurrencyCode':
            self.is_TaxCurrencyCode_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}PricingCurrencyCode':
            self.is_PricingCurrencyCode_data = False
        elif tag == '{' + self.namespaces.get('cbc') + '}LineCountNumeric':
            self.is_LineCountNumeric_data = False
        elif tag == "Invoice":
            self.return_data[self.tax_id] = dict(
                [("is_efatura_user", self.is_efatura_user), ("is_eirsaliye_user", self.is_eirsaliye_user)])
            self.setup()

    def data(self, data):
        if self.is_UBLVersionID_data:
            self.UBLVersionID = data
        elif self.is_CustomizationID_data:
            self.CustomizationID = data
        elif self.is_ProfileID_data:
            self.ProfileID = data
        elif self.is_ID_data:
            self.ID = data
        elif self.is_CopyIndicator_data:
            self.CopyIndicator = data
        elif self.is_UUID_data:
            self.UUID = data
        elif self.is_IssueDate_data:
            self.IssueDate = data
        elif self.is_IssueTime_data:
            self.IssueTime = data
        elif self.is_InvoiceTypeCode_data:
            self.InvoiceTypeCode = data
        elif self.is_Note_data:
            self.Notes.append(data)
        elif self.is_DocumentCurrencyCode_data:
            self.DocumentCurrencyCode = data
        elif self.is_TaxCurrencyCode_data:
            self.TaxCurrencyCode = data
        elif self.is_PricingCurrencyCode_data:
            self.PricingCurrencyCode = data
        elif self.is_LineCountNumeric_data:
            self.LineCountNumeric = data

    def close(self):  # Called when all data has been parsed.
        return self.return_data

    def setup(self):
        self.tax_id = ""
        self.is_tax_data = False  #
        self.activity_count = 0  # use when document is of ebelge type to determine if active
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
