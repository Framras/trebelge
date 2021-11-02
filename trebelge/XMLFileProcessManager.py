from trebelge.XMLFileTypeState import XMLFileTypeContext
from trebelge.XMLFileTypeCoR import AbstractXMLFileTypeHandler
from trebelge.XMLFileTypeCoR.InvoiceHandler import InvoiceHandler


class XMLFileProcessManager:
    # initiate Context of State pattern for FileType
    cXMLFileTypeContext = XMLFileTypeContext()
    # initiate CoR pattern for xmlFile
    hXMLFileTypeHandler: AbstractXMLFileTypeHandler = InvoiceHandler()

    def __init__(self, file_path: str):
        self.hXMLFileTypeHandler.handle_xml_file_type(file_path, self.cXMLFileTypeContext)
