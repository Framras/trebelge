import xml.etree.ElementTree as ET

from trebelge.XMLFileProcessStrategy import XMLFileProcessStrategyContext
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy


class XMLNamespaces(XMLFileProcessStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """

    def return_xml_file_data(self, context: XMLFileProcessStrategyContext):
        return dict([node for _, node in ET.iterparse(file_path, events=['start-ns'])])
