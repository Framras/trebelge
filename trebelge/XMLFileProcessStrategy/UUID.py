import xml.etree.ElementTree as ET

from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy


class UUID(XMLFileProcessStrategy):
    def return_xml_file_data(self, file_path: str):
        return ET.parse(file_path).getroot().find(cbc_namespace + 'UUID').text
