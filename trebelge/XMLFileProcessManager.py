from trebelge.XMLFileTypeCoR import AbstractXMLFileTypeHandler
import XMLFileProcessStateManager


class XMLFileProcessManager():
    self.xmlpsm = XMLFileProcessStateManager
    self.hInvoice = IXMLFileTypeHandler

    def __init__(self, filepath):
        self.xmlpsm = XMLFileProcessStateManager()

        # create ConcreteHandler instances
        self.hInvoice =
