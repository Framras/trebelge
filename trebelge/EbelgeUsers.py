import frappe
from frappe.model.document import Document


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
                parties: list = frappe.get_all(party_type, filters={"tax_id": self.tax_id, "disabled": 0},
                                               fields={"name"})
                if len(parties) != 0:
                    for party in parties:
                        doc: Document = frappe.get_doc(party_type, party.name)
                        save_doc = False
                        if self.is_efatura_user:
                            if doc.is_efatura_user != 1:
                                doc.is_efatura_user = 1
                                save_doc = True
                        else:
                            if doc.is_efatura_user == 1:
                                doc.is_efatura_user = 0
                                save_doc = True
                        if self.is_eirsaliye_user:
                            if doc.is_eirsaliye_user != 1:
                                doc.is_eirsaliye_user = 1
                                save_doc = True
                        else:
                            if doc.is_eirsaliye_user == 1:
                                doc.is_eirsaliye_user = 0
                                save_doc = True
                        if save_doc:
                            doc.save()
            self.return_data.append(self.tax_id)

            self.setup()

    def data(self, data):
        if self.is_tax_data:
            self.tax_id = data

    def close(self):  # Called when all data has been parsed.
        for party_type in self.party_types:
            for party in frappe.get_all(party_type,
                                        filters={"tax_id": ["not in", self.return_data], "disabled": 0},
                                        fields={"name"}):
                doc: Document = frappe.get_doc(party_type, party.name)
                save_doc = False
                if doc.is_efatura_user == 1:
                    doc.is_efatura_user = 0
                    save_doc = True
                if doc.is_eirsaliye_user == 1:
                    doc.is_eirsaliye_user = 0
                    save_doc = True
                if save_doc:
                    doc.save()

        return frappe.utils.now_datetime()

    def setup(self):
        self.tax_id = ""
        self.is_tax_data = False  #
        self.activity_count = 0  # use when document is of ebelge type to determine if active
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
