import xml.etree.ElementTree as ET

from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy


class XMLNamespaces(XMLFileProcessStrategy):
    def return_xml_file_data(self, file_path: str):
        return dict([node for _, node in ET.iterparse(file_path, events=['start-ns'])])
