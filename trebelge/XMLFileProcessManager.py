from trebelge.XMLFileTypeCoR import AbstractXMLFileTypeHandler
from trebelge.XMLFileTypeCoR.InvoiceHandler import InvoiceHandler


class XMLFileProcessManager:
    hXMLFile: AbstractXMLFileTypeHandler = InvoiceHandler()

    def __init__(self, filepath):
        self.hXMLFile.handle_request(filepath)
