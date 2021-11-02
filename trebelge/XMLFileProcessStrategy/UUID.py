import xml.etree.ElementTree as ET

from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy


class UUID(XMLFileProcessStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """

    def return_xml_file_data(self):
        context = XMLFileProcessContext(CBCNamespace())
        namespaces = context.return_file_data(file_path)
        return ET.parse(file_path).getroot().find(cbc_namespace + 'UUID').text
