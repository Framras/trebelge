import frappe


class EbelgeUsers:  # The target object of the parser
    def __init__(self):
        self.tax_id = ""
        self.is_tax_data = False
        self.activity_count = 0
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
        self.party_types = ["Customer", "Supplier"]
        self.return_data = list()

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
            for party_type in self.party_types:
                if frappe.db.exists(party_type, {"tax_id": self.tax_id, "disabled": 0}):
                    parties: list = frappe.get_all(party_type, filters={"tax_id": self.tax_id, "disabled": 0},
                                                   fields={"name", "tax_id", "is_efatura_user", "is_eirsaliye_user"})
                    for party in parties:
                        if self.is_efatura_user:
                            if party.is_efatura_user != 1:
                                doc = frappe.get_doc(party_type, party.name)
                                doc.db_set("is_efatura_user", 1)
                        else:
                            if party.is_efatura_user == 1:
                                doc = frappe.get_doc(party_type, party.name)
                                doc.db_set("is_efatura_user", 0)
                        if self.is_eirsaliye_user:
                            if party.is_eirsaliye_user != 1:
                                doc = frappe.get_doc(party_type, party.name)
                                doc.db_set("is_eirsaliye_user", 1)
                        else:
                            if party.is_eirsaliye_user == 1:
                                doc = frappe.get_doc(party_type, party.name)
                                doc.db_set("is_eirsaliye_user", 0)
            self.return_data.append(self.tax_id)

            self.setup()

    def data(self, data):
        if self.is_tax_data:
            self.tax_id = data

    def close(self):  # Called when all data has been parsed.
        for party_type in self.party_types:
            for party in frappe.get_all(party_type,
                                        filters={"tax_id": ["not in", self.return_data], "disabled": 0},
                                        fields={"name", "is_efatura_user", "is_eirsaliye_user"}):
                if party.is_efatura_user == 1:
                    doc = frappe.get_doc(party_type, party.name)
                    doc.db_set("is_efatura_user", 0)
                if party.is_eirsaliye_user == 1:
                    doc = frappe.get_doc(party_type, party.name)
                    doc.db_set("is_eirsaliye_user", 0)

        return frappe.utils.now_datetime()

    def setup(self):
        self.tax_id = ""
        self.is_tax_data = False  #
        self.activity_count = 0  # use when document is of ebelge type to determine if active
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
