class incomingEfaturaReader:  # The target object of the parser
    def __init__(self):
        self.UBLVersionID = ""
        self.is_UBLVersionID_data = False
        self.CustomizationID = ""
        self.is_CustomizationID_data = False
        self.ProfileID = ""
        self.is_ProfileID_data = False
        self.ID = ""
        self.is_ID_data = False
        self.CopyIndicator = ""
        self.is_CopyIndicator_data = False
        self.UUID = ""
        self.is_UUID_data = False
        self.IssueDate = ""
        self.is_IssueDate_data = False
        self.IssueTime = ""
        self.is_IssueTime_data = False
        self.activity_count = 0
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
        self.return_data = dict()

    def start(self, tag, attrib):  # Called for each opening tag.
        if tag == "cbc:UBLVersionID":
            self.is_UBLVersionID_data = True
        elif tag == "cbc:CustomizationID":
            self.is_CustomizationID_data = True
        elif tag == "cbc:ProfileID":
            self.is_ProfileID_data = True
        elif tag == "cbc:ID":
            self.is_ID_data = True
        elif tag == "cbc:CopyIndicator":
            self.is_CopyIndicator_data = True
        elif tag == "cbc:UUID":
            self.is_UUID_data = True
        elif tag == "cbc:IssueDate":
            self.is_IssueDate_data = True
        elif tag == "cbc:IssueTime":
            self.is_IssueTime_data = True
        elif tag == "Document":
            self.activity_count = 0
            if attrib["type"] == "Invoice":
                self.is_einvoice_document = True
                self.is_edespatchadvice_document = False
            elif attrib["type"] == "DespatchAdvice":
                self.is_edespatchadvice_document = True
                self.is_einvoice_document = False

    def end(self, tag):  # Called for each closing tag.
        if tag == "cbc:UBLVersionID":
            self.is_UBLVersionID_data = False
        elif tag == "cbc:CustomizationID":
            self.is_CustomizationID_data = False
        elif tag == "cbc:ProfileID":
            self.is_ProfileID_data = False
        elif tag == "cbc:ID":
            self.is_ID_data = False
        elif tag == "cbc:CopyIndicator":
            self.is_CopyIndicator_data = False
        elif tag == "cbc:UUID":
            self.is_UUID_data = False
        elif tag == "cbc:IssueDate":
            self.is_IssueDate_data = False
        elif tag == "cbc:IssueTime":
            self.is_IssueTime_data = False
        elif tag == "CreationTime":
            self.activity_count += 1
        elif tag == "DeletionTime":
            self.activity_count -= 1
        elif tag == "Document":
            if self.activity_count > 0:
                if self.is_einvoice_document:
                    self.is_efatura_user = True
                elif self.is_edespatchadvice_document:
                    self.is_eirsaliye_user = True
        elif tag == "Documents":
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
