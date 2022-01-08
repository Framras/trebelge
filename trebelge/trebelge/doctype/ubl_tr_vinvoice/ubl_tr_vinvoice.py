# Copyright (c) 2022, Framras AS-Izmir and contributors
# For license information, please see license.txt

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import frappe
# import frappe
from frappe.model.document import Document


class UBLTRVInvoice(Document):
    _eBelgeSettingsDoctype: str = 'UBL TR Namespace Specifications'
    _eBelgeTag: str = 'Invoice'

    def db_insert(self):
        pass

    def load_from_db(self):
        pass

    def db_update(self):
        pass

    def get_list(self, args):
        # for all *.xml files
        for xmlFile in frappe.get_all('File', filters={"file_name": ["like", "%.xml"], "is_folder": 0},
                                      fields={"file_url"}):
            # retrieve file path of xmlFile
            filePath: str = frappe.get_site_path() + xmlFile.get('file_url')
            for namespace in frappe.get_all(
                    self._eBelgeSettingsDoctype, filters={"disabled": 0, "ebelge_type": self._eBelgeTag},
                    fields={"namespace_specification"}):
                if ET.parse(filePath).getroot().tag == namespace.get('namespace_specification') + self._eBelgeTag:
                    _namespaces = dict([node for _, node in ET.iterparse(self.filepath, events=['start-ns'])])
                    self._cac_ns = str('{' + _namespaces.get('cac') + '}')
                    self._cbc_ns = str('{' + _namespaces.get('cbc') + '}')
                    root_: Element = ET.parse(self.filepath).getroot()
                    uuid_ = root_.find('./' + self._cbc_ns + 'UUID').text
                    return uuid_
