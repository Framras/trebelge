# Copyright (c) 2026, Framras AS-Izmir and Contributors
# See license.txt

from unittest.mock import patch

import frappe
from frappe.tests import IntegrationTestCase

from trebelge.codelists import validate_for_production, warn_on_read


class TestCodeLists(IntegrationTestCase):
    def test_read_warns_and_production_throws(self):
        with patch.object(frappe.logger("trebelge"), "warning") as warned:
            warn_on_read("ProfileID", "BU_KOD_YOK")
            self.assertTrue(warned.called)
            warned.reset_mock()
            warn_on_read("ProfileID", "TEMELFATURA")
            self.assertFalse(warned.called)

        validate_for_production("ProfileID", "TEMELFATURA")
        validate_for_production("UnitCode", "C62")
        with self.assertRaises(frappe.ValidationError):
            validate_for_production("ProfileID", "BU_KOD_YOK")
        with self.assertRaises(frappe.ValidationError):
            validate_for_production("InvoiceTypeCode", "")
