from trebelge.XMLFileTypeCoR import IXMLFileTypeHandler
import XMLFileProcessStateManager


class XMLFileProcessManager():
    self.xmlpsm = XMLFileProcessStateManager
    self.hInvoice = IXMLFileTypeHandler

    def __init__(self, filepath):
        self.xmlpsm = XMLFileProcessStateManager()

        # create ConcreteHandler instances
        self.hInvoice =
