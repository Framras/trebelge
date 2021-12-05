import frappe


class TRUBLInvoice:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """
    _frappeDoctype: str = 'UBL TR Invoice'
    _invoice = None

    def __init__(self, uuid_: str):
        product: dict = {"doctype": self._frappeDoctype, "uuid": uuid_}
        if not frappe.get_all(self._frappeDoctype, filters=product):
            self._invoice = frappe.new_doc(self._frappeDoctype)
        else:
            self._invoice = None

    def add(self, part) -> None:
        if self._invoice[0] is not None:
            self._invoice.as_dict.append = part

    def commit_doc(self):
        self._invoice.insert()
