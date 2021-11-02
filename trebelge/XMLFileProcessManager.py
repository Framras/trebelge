from trebelge.XMLFileCoR import AbstractXMLFileHandler
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler
from trebelge.XMLFileTypeState.XMLFileTypeStateContext import XMLFileTypeStateContext


class XMLFileProcessManager:
    # initiate CoR pattern for xmlFile
    _hXMLFileHandler: AbstractXMLFileHandler = InvoiceHandler()
    _cXMLFileTypeStateContext = XMLFileTypeStateContext()

    def __init__(self, file_path: str):
        self._cXMLFileTypeStateContext.set_file_path(file_path)
        # initiate Context of State pattern for FileType
        self._hXMLFileHandler.handle_xml_file(self._cXMLFileTypeStateContext)
        self._cXMLFileTypeStateContext.find_record_status()
