from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeCoR import AbstractXMLFileTypeHandler
from trebelge.XMLFileTypeCoR.InvoiceHandler import InvoiceHandler


class XMLFileProcessManager:
    cXMLFileTypeContext = XMLFileTypeContext()
    hXMLFileTypeHandler: AbstractXMLFileTypeHandler = InvoiceHandler()

    def __init__(self, file_path: str):
        self.hXMLFileTypeHandler.handle_request(file_path)
