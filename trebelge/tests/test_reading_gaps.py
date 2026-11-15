# Copyright (c) 2026, Framras AS-Izmir and Contributors
# See license.txt

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
from frappe.tests import IntegrationTestCase
from frappe.utils import flt, getdate

from trebelge.TRUBLBuilder.TRUBLDirector import TRUBLDirector
from trebelge.TRUBLBuilder.TRUBLInvoiceBuilder import TRUBLInvoiceBuilder


INVOICE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
 xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
 xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.1</cbc:UBLVersionID>
  <cbc:CustomizationID>TR1.2</cbc:CustomizationID>
  <cbc:ProfileID>TEMELFATURA</cbc:ProfileID>
  <cbc:ID>ABC2026000000001</cbc:ID>
  <cbc:CopyIndicator>false</cbc:CopyIndicator>
  <cbc:UUID>11111111-1111-1111-1111-111111111111</cbc:UUID>
  <cbc:IssueDate>2026-11-15</cbc:IssueDate>
  <cbc:InvoiceTypeCode>SATIS</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>TRY</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification><cbc:ID schemeID="VKN">1111111111</cbc:ID></cac:PartyIdentification>
      <cac:PartyName><cbc:Name>Satici A.S.</cbc:Name></cac:PartyName>
      <cac:PostalAddress>
        <cbc:CitySubdivisionName>Konak</cbc:CitySubdivisionName>
        <cbc:CityName>Izmir</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>TR</cbc:IdentificationCode>
          <cbc:Name>Turkiye</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification><cbc:ID schemeID="VKN">2222222222</cbc:ID></cac:PartyIdentification>
      <cac:PartyName><cbc:Name>Alici A.S.</cbc:Name></cac:PartyName>
      <cac:PostalAddress>
        <cbc:CitySubdivisionName>Kadikoy</cbc:CitySubdivisionName>
        <cbc:CityName>Istanbul</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>TR</cbc:IdentificationCode>
          <cbc:Name>Turkiye</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode>10</cbc:PaymentMeansCode>
    <cbc:PaymentID>REF-99</cbc:PaymentID>
  </cac:PaymentMeans>
  <cac:PrepaidPayment>
    <cbc:ID>AVANS-1</cbc:ID>
    <cbc:PaidAmount currencyID="TRY">25.50</cbc:PaidAmount>
    <cbc:ReceivedDate>2026-01-15</cbc:ReceivedDate>
  </cac:PrepaidPayment>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="TRY">0.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="TRY">0.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="TRY">0.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="TRY">0.00</cbc:PayableAmount>
    <cbc:PrepaidAmount currencyID="TRY">25.50</cbc:PrepaidAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="C62">1</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="TRY">0.00</cbc:LineExtensionAmount>
    <cbc:FreeOfChargeIndicator>true</cbc:FreeOfChargeIndicator>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Satir iskontosu</cbc:AllowanceChargeReason>
      <cbc:Amount currencyID="TRY">1.00</cbc:Amount>
    </cac:AllowanceCharge>
    <cac:Item>
      <cbc:Name>Bedelsiz kalem</cbc:Name>
      <cac:StandardItemIdentification>
        <cbc:ID>8690000000001</cbc:ID>
      </cac:StandardItemIdentification>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="TRY">10.00</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="C62">1</cbc:BaseQuantity>
      <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReason>Birim fiyat iskontosu</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="TRY">2.00</cbc:Amount>
      </cac:AllowanceCharge>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
"""


class TestReadingGaps(IntegrationTestCase):
    def setUp(self):
        self._ensure("UBL TR CurrencyCode", {"currencycode": "TRY", "currencyname": "Turk Lirasi"})
        self._ensure("UBL TR PartyIdentification Scheme", {"schemeid": "VKN", "description": "VKN"})
        self._ensure(
            "UBL TR Unitcodes",
            {"unitcode": "C62", "unitcodename": "Adet", "description": "UNECE Rec.20 one", "type": "UNECE Rec.20"},
        )
        self._ensure("UBL TR Paymentmeanscode", {"paymentmeanscode": "10"})

    def _ensure(self, doctype: str, values: dict) -> None:
        name = values.get("currencycode") or values.get("schemeid") or values.get("unitcode") or values.get(
            "paymentmeanscode"
        )
        if not frappe.db.exists(doctype, name):
            frappe.get_doc({"doctype": doctype, **values}).insert(ignore_permissions=True)

    def test_invoice_read_stores_seven_gaps(self):
        root: Element = ET.fromstring(INVOICE_XML)
        ns = {"cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"}
        cbc_ns = "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}"
        cac_ns = "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}"
        uuid_ = root.find("cbc:UUID", ns).text
        builder = TRUBLInvoiceBuilder(root, cac_ns, cbc_ns, uuid_)
        TRUBLDirector(builder).make_tr_ubl_invoice()
        builder.get_document()

        invoice = frappe.get_doc("UBL TR Invoice", uuid_)
        self.assertEqual(flt(invoice.prepaidamount), flt("25.50"))
        self.assertEqual(invoice.prepaidamountcurrencyid, "TRY")
        self.assertEqual(len(invoice.prepaidpayment), 1)
        prepaid = invoice.prepaidpayment[0]
        self.assertEqual(prepaid.id, "AVANS-1")
        self.assertEqual(flt(prepaid.paidamount), flt("25.50"))
        self.assertEqual(prepaid.paidamountcurrencyid, "TRY")
        self.assertEqual(getdate(prepaid.receiveddate), getdate("2026-01-15"))

        self.assertEqual(len(invoice.paymentmeans), 1)
        payment = frappe.get_doc("UBL TR PaymentMeans", invoice.paymentmeans[0].paymentmeans)
        self.assertEqual(payment.paymentid, "REF-99")
        self.assertEqual(payment.paymentmeanscode, "10")

        line = frappe.get_doc("UBL TR InvoiceLine", invoice.invoicelinesummary[0].invoiceline)
        self.assertEqual(line.freeofchargeindicator, 1)
        self.assertEqual(flt(line.basequantity), flt("1"))
        self.assertEqual(line.basequantityunitcode, "C62")

        item = frappe.get_doc("UBL TR Item", line.item)
        identification = frappe.get_doc("UBL TR ItemIdentification", item.standarditemid)
        self.assertEqual(identification.id, "8690000000001")

        self.assertEqual(len(line.priceallowancecharge), 1)
        self.assertEqual(len(line.allowancecharge), 1)
        price_allowance = frappe.get_doc(
            "UBL TR AllowanceCharge", line.priceallowancecharge[0].allowancecharge
        )
        line_allowance = frappe.get_doc("UBL TR AllowanceCharge", line.allowancecharge[0].allowancecharge)
        self.assertEqual(price_allowance.allowancechargereason, "Birim fiyat iskontosu")
        self.assertEqual(line_allowance.allowancechargereason, "Satir iskontosu")
        self.assertNotEqual(price_allowance.name, line_allowance.name)
        self.assertEqual(flt(price_allowance.amount), flt("2.00"))
        self.assertEqual(flt(line_allowance.amount), flt("1.00"))
