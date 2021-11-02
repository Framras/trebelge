import xml.etree.ElementTree as ET

from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategyContext import XMLFileProcessStrategyContext
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy
from trebelge.XMLFileProcessStrategy.XMLNamespaces import XMLNamespaces


class CBCNamespace(XMLFileProcessStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """

    def return_xml_file_data(self):
        context = XMLFileProcessStrategyContext(XMLNamespaces())
        cbc_namespace = context.return_file_data(file_path)
        return ET.parse(file_path).getroot().find(cbc_namespace + 'UUID').text
