"""GİB / UBL-TR code lists.

Read path: unknown codes are logged and parsing continues.
Production path: ``validate_for_production`` throws and the document is not produced.
There is no XML producer in trebelge yet; call this before one is added.
"""

from __future__ import annotations

import json
import os

import frappe
from frappe import _

# kind -> (DocType, filter field or None when the document name is the code)
_DOCTYPES: dict[str, tuple[str, str | None]] = {
    "ProfileID": ("UBL TR ProfileID", None),
    "InvoiceTypeCode": ("UBL TR InvoiceTypeCode", None),
    "PaymentMeansCode": ("UBL TR Paymentmeanscode", None),
    "TaxExemptionReasonCode": ("UBL TR TaxExemptionReasonCode", None),
    "WithholdingTaxCode": ("UBL TR Withholdingtaxcode", "code"),
    "UnitCode": ("UBL TR Unitcodes", None),
}


def is_known(kind: str, code: str | None) -> bool:
    if code is None or kind not in _DOCTYPES:
        return False
    code = str(code).strip()
    if code == "":
        return False
    doctype, field = _DOCTYPES[kind]
    if not frappe.db.exists("DocType", doctype):
        return False
    if field:
        return bool(frappe.db.exists(doctype, {field: code}))
    return bool(frappe.db.exists(doctype, code))


def warn_on_read(kind: str, code: str | None) -> None:
    """Log an unknown code. Never raises, so the parser keeps going."""
    if code is None or str(code).strip() == "":
        return
    logger = frappe.logger("trebelge")
    try:
        known = is_known(kind, code)
    except Exception:
        logger.warning("Kod listesi kontrol edilemedi (%s %s); okuma devam ediyor", kind, code)
        return
    if not known:
        logger.warning("Bilinmeyen %s kodu: %s. Okuma devam ediyor.", kind, str(code).strip())


def validate_for_production(kind: str, code: str | None) -> None:
    """Reject an unknown code on the production path. The document must not be produced."""
    if kind not in _DOCTYPES:
        frappe.throw(_("{0} kod listesi tanımsız, belge üretilmedi").format(kind))
    if code is None or str(code).strip() == "":
        frappe.throw(_("{0} kodu boş, belge üretilmedi").format(kind))
    if not is_known(kind, code):
        frappe.throw(_("{0} kodu listede yok, belge üretilmedi: {1}").format(kind, str(code).strip()))


def load_code_lists() -> None:
    """Insert fixture rows that are not already stored. Does not update or delete."""
    folder = frappe.get_app_path("trebelge", "fixtures")
    if not folder or not os.path.isdir(folder):
        return
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(folder, fname)
        with open(path, encoding="utf-8") as handle:
            rows = json.load(handle)
        if isinstance(rows, dict):
            rows = [rows]
        for row in rows:
            doctype = row.get("doctype")
            name = row.get("name")
            if not doctype or not name or not frappe.db.exists("DocType", doctype):
                continue
            if frappe.db.exists(doctype, name):
                continue
            frappe.get_doc(row).insert(ignore_permissions=True)
