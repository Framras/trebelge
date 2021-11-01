from trebelge.XMLFileTypeCoR import AbstractXMLFileTypeHandler
from trebelge.XMLFileTypeCoR.InvoiceHandler import InvoiceHandler


class XMLFileProcessManager:
    hXMLFile: AbstractXMLFileTypeHandler = InvoiceHandler()

    def __init__(self, file_path):
        self.hXMLFile.handle_request(file_path)
