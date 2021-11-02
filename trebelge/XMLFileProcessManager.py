from trebelge.XMLFileCoR import AbstractXMLFileHandler
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler
from trebelge.XMLFileTypeState.XMLFileTypeStateContext import XMLFileTypeStateContext


class XMLFileProcessManager:
    # initiate CoR pattern for xmlFile
    _hXMLFileHandler: AbstractXMLFileHandler = InvoiceHandler()
    # initiate Context of State pattern
    _cXMLFileTypeStateContext = XMLFileTypeStateContext()

    def __init__(self, file_path: str):
        # initiate Context of State pattern for FileType
        self._cXMLFileTypeStateContext.set_file_path(file_path)
        # handle file by CoR to determine State
        self._hXMLFileHandler.handle_xml_file(self._cXMLFileTypeStateContext)
        # check on State if file is previously processed and recorded
        self._cXMLFileTypeStateContext.find_record_status()
