// Copyright (c) 2021, Framras AS-Izmir and contributors
// For license information, please see license.txt

frappe.ui.form.on('UBL TR Process Files', {
	// refresh: function(frm) {
	check_xml_files: function(frm){
        frappe.call({
            method: "trebelge.api.check_all_xml_files",
            args:{
            },
            callback: function(r){
                frm.set_value("last_run", r.message);
                frm.save();
            }
        })
	}
	// }
});
