import xml.etree.ElementTree as ET

from trebelge.XMLFileProcessStrategy.CBCNamespace import CBCNamespace
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategyContext import XMLFileProcessStrategyContext


class UUID(XMLFileProcessStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """

    def return_xml_file_data(self, context: XMLFileProcessStrategyContext):
        file_path = context.get_file_path()
        uuid_context = XMLFileProcessStrategyContext()
        uuid_context.set_strategy(CBCNamespace())
        uuid_context.set_file_path(file_path)
        cbc_namespace = uuid_context.return_file_data()
        return ET.parse(file_path).getroot().find(cbc_namespace + 'UUID').text
