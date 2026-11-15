class EbelgeUsers:  # The target object of the parser
    """SAX-style target for ``xml.etree.ElementTree.XMLParser``.

    Streams the GIB registered-users list (``newUserPkList.xml``) and records,
    per tax id, whether the party is an active e-Fatura and/or e-Irsaliye
    user. The parser itself builds no tree, so memory stays flat no matter
    how large the file grows -- provided the caller also streams the file
    in chunks (see ``trebelge.api.get_ebelge_users``) instead of reading it
    whole.

    Only the users the caller actually needs are kept: pass the tax ids of
    your own Customers/Suppliers as ``wanted`` and every other user is
    parsed and discarded. The list holds every registered user in Turkey
    (well over a million), while a company has at most a few thousand
    parties, so keeping all of them in ``return_data`` was the other half
    of the memory blow-up. ``wanted=None`` keeps the old behaviour
    (store every user) for callers that really need the full list.
    """

    def __init__(self, wanted=None):
        self.wanted = wanted
        self.tax_id = ""
        self._tax_id_parts = []
        self.is_tax_data = False
        self.activity_count = 0
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
        self.return_data: dict[str, dict[str, bool]] = {}

    @staticmethod
    def _local(tag):
        # Tolerate namespaced documents: "{uri}Identifier" -> "Identifier".
        # Plain tags pass through unchanged.
        return tag.rsplit("}", 1)[-1] if "}" in tag else tag

    def start(self, tag, attrib):  # Called for each opening tag.
        tag = self._local(tag)
        if tag == "Identifier":
            self.is_tax_data = True
            self._tax_id_parts = []
        elif tag == "Document":
            self.activity_count = 0
            if attrib["type"] == "Invoice":
                self.is_einvoice_document = True
                self.is_edespatchadvice_document = False
            elif attrib["type"] == "DespatchAdvice":
                self.is_edespatchadvice_document = True
                self.is_einvoice_document = False

    def end(self, tag):  # Called for each closing tag.
        tag = self._local(tag)
        if tag == "Identifier":
            # Character data may arrive in several pieces (expat splits text
            # at chunk boundaries), so join the collected parts.
            self.tax_id = "".join(self._tax_id_parts).strip()
            self._tax_id_parts = []
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
            if self.wanted is None or self.tax_id in self.wanted:
                self.return_data[self.tax_id] = {
                    "is_efatura_user": self.is_efatura_user,
                    "is_eirsaliye_user": self.is_eirsaliye_user,
                }
            self.setup()

    def data(self, data):
        if self.is_tax_data:
            self._tax_id_parts.append(data)

    def close(self):  # Called when all data has been parsed.
        return self.return_data

    def setup(self):
        self.tax_id = ""
        self._tax_id_parts = []
        self.is_tax_data = False  #
        self.activity_count = 0  # use when document is of ebelge type to determine if active
        self.is_einvoice_document = False
        self.is_edespatchadvice_document = False
        self.is_efatura_user = False
        self.is_eirsaliye_user = False
