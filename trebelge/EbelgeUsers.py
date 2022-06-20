class EbelgeUsers:  # The target object of the parser
    def __init__(self):
        self.tax_id = ""
        self.is_tax_data = False
        self.activity_count = 0
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
        self.return_data = dict()

    def start(self, tag, attrib):  # Called for each opening tag.
        if tag == "Identifier":
            self.is_tax_data = True
        elif tag == "Document":
            self.activity_count = 0
            if attrib["type"] == "Invoice":
                self.is_einvoice_document = True
                self.is_edespatchadvice_document = False
            elif attrib["type"] == "DespatchAdvice":
                self.is_edespatchadvice_document = True
                self.is_einvoice_document = False

    def end(self, tag):  # Called for each closing tag.
        if tag == "Identifier":
            self.is_tax_data = False
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
        if self.is_tax_data:
            self.tax_id = data

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
