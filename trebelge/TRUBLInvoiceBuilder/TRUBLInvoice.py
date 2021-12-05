import frappe
from frappe.model.document import Document


class TRUBLInvoice:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """
    _frappeDoctype: str = 'UBL TR Invoice'
    _invoice: Document = frappe.new_doc(_frappeDoctype)

    def set_uuid(self, uuid_: str):
        if not frappe.get_all(self._frappeDoctype, filters={'uuid': uuid_}):
            _invoice: Document = frappe.new_doc(self._frappeDoctype)
            _invoice.uuid = uuid_
        else:
            _invoice = None
        self._invoice = _invoice

    def add(self, part: dict):
        if self._invoice is not None:
            for key in part.keys():
                self._invoice.set(key, part.get(key))

    def commit_doc(self):
        self._invoice.insert()
