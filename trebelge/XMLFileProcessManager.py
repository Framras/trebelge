from trebelge.XMLFileCoR import AbstractXMLFileHandler
from trebelge.XMLFileCoR.InvoiceHandler import InvoiceHandler
from trebelge.XMLFileTypeState.XMLFileTypeContext import XMLFileTypeContext


class XMLFileProcessManager:
    # initiate CoR pattern for xmlFile
    _hXMLFileHandler: AbstractXMLFileHandler = InvoiceHandler()
    _cXMLFileTypeContext = XMLFileTypeContext(None, '')

    def __init__(self, file_path: str):
        self._cXMLFileTypeContext.set_file_path(file_path)
        # initiate Context of State pattern for FileType
        self._hXMLFileHandler.handle_xml_file(file_path, self._cXMLFileTypeContext)
        if self._cXMLFileTypeContext.find_record_status():
