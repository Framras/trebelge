from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategy import XMLFileProcessStrategy
from trebelge.XMLFileProcessStrategy.XMLFileProcessStrategyContext import XMLFileProcessStrategyContext
from trebelge.XMLFileProcessStrategy.XMLNamespaces import XMLNamespaces


class CACNamespace(XMLFileProcessStrategy):
    """
    Concrete Strategies implement the algorithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context.
    """

    def return_xml_file_data(self, context: XMLFileProcessStrategyContext):
        file_path = context.get_file_path()
        xmlnamespaces_context = XMLFileProcessStrategyContext()
        xmlnamespaces_context.set_file_path(file_path)
        xmlnamespaces_context.set_strategy(XMLNamespaces())
        namespaces = xmlnamespaces_context.return_file_data()
        cbc_namespace: str = '{' + namespaces.get('cac') + '}'
        return cbc_namespace
