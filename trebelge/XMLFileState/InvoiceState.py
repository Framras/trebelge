# from __future__ import annotations

import frappe
from trebelge.XMLFileState.AbstractXMLFileState import AbstractXMLFileState
from trebelge.XMLFileState.NewInvoiceState import NewInvoiceState


class InvoiceState(AbstractXMLFileState):
    """
    State methods
    Backreference to the Context object, associated with the State.
    """
    _frappeDoctype: str = 'TR GIB eFatura Gelen'

    def find_ebelge_status(self):
        if not frappe.db.exists({"doctype": self._frappeDoctype,
                                 "uuid": self.get_context().get_uuid()}):
            self.get_context().set_state(NewInvoiceState())

    "ublversionid"
    "profileid"

    "customizationid"
    "copyindicator"

    "id"
    "issuedate"
    "issuetime"

    "uuid"
    "invoicetypecode"

    "note"

    "documentcurrencycode"
    "taxcurrencycode"
    "pricingcurrencycode"
    "paymentcurrencycode"
    "paymentalternativecurrencycode"

    "accountingcost"
    "linecountnumeric"

    "invoiceperiod_startdate"
    "invoiceperiod_starttime"
    "invoiceperiod_durationmeasure"

    "invoiceperiod_enddate"
    "invoiceperiod_endtime"
    "invoiceperiod_durationmeasure_unitcode"
    "invoiceperiod_description"

    "orderreference_id"
    "orderreference_salesorderid"

    "orderreference_issuedate"
    "orderreference_ordertypecode"
    "orderreference_documentreference"

    "billingreference"
    "despatchdocumentreference"
    "receiptdocumentreference"
    "originatordocumentreference"
    "contractdocumentreference"
    "additionaldocumentreference"
    "signature"

    "accountingsupplierparty_websiteuri"
    "accountingsupplierparty_partyidentification_schemeid"
    "accountingsupplierparty_partyidentificationid"
    "accountingsupplierparty_partyname"

    "accountingsupplierparty_industryclassificationcode"
    "accountingsupplierparty_endpointid"
    "accountingsupplierparty_postaladdress_id"
    "accountingsupplierparty_postaladdress_postbox"
    "accountingsupplierparty_postaladdress_room"
    "accountingsupplierparty_postaladdress_streetname"
    "accountingsupplierparty_postaladdress_blockname"
    "accountingsupplierparty_postaladdress_buildingname"
    "accountingsupplierparty_postaladdress_buildingnumber"
    "accountingsupplierparty_postaladdress_citysubdivisionname"
    "accountingsupplierparty_postaladdress_cityname"
    "accountingsupplierparty_postaladdress_postalzone"
    "accountingsupplierparty_postaladdress_region"
    "accountingsupplierparty_postaladdress_district"
    "accountingsupplierparty_postaladdress_country"
    "accountingcustomerparty"
    "buyercustomerparty"
    "sellersupplierparty"
    "taxrepresentativeparty"

    "taxexchangerate_sourcecurrencycode"
    "taxexchangerate_date"
    "column_break_vergi_doviz_kuru"
    "taxexchangerate_targetcurrencycode"
    "taxexchangerate_calculationrate"

    "pricingexchangerate_sourcecurrencycode"
    "pricingexchangerate_date"
    "column_break_fiyatlandirma_doviz_kuru"
    "pricingexchangerate_targetcurrencycode"
    "pricingexchangerate_calculationrate"

    "paymentexchangerate_sourcecurrencycode"
    "paymentexchangerate_date"
    "column_break_odeme_doviz_kuru"
    "paymentexchangerate_targetcurrencycode"
    "paymentexchangerate_calculationrate"

    "paymentalternativeexchangerate_sourcecurrencycode"
    "paymentalternativeexchangerate_date"
    "column_break_alternatif_odeme_doviz_kuru"
    "paymentalternativeexchangerate_targetcurrencycode"
    "paymentalternativeexchangerate_calculationrate"
