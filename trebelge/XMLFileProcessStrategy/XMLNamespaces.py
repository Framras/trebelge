import xml.etree.ElementTree as ET

from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategyContext import XMLFileProcessStrategyContext


class XMLNamespaces(XMLFileProcessStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """

    def return_xml_file_data(self, context: XMLFileProcessStrategyContext):
        file_path = context.get_file_path()
        # return all namespaces
        return dict([node for _, node in ET.iterparse(file_path, events=['start-ns'])])
