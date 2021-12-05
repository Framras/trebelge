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
    _invoice = frappe.new_doc(_frappeDoctype)

    def set_uuid(self, uuid_: str):
        if not frappe.get_all(self._frappeDoctype, filters={'uuid': uuid_}):
            self._invoice = frappe.new_doc(self._frappeDoctype)
            self._invoice.uuid = uuid_
        else:
            self._invoice = None

    def add(self, part) -> None:
        if self._invoice is not None:
            self._invoice.

    def commit_doc(self):
        self._invoice.insert()
