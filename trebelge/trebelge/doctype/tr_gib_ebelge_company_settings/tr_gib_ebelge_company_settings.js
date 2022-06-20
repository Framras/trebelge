// Copyright (c) 2019, Framras AS-Izmir and contributors
// For license information, please see license.txt

frappe.ui.form.on('TR GIB eBelge Company Settings', {
	initiate_ebelge_parties: function(frm){
        frappe.call({
            method: "trebelge.api.check_all_ebelge_parties",
            args:{
            },
            callback: function(r){
                frm.set_value("last_run", r.message);
                frm.save();
            }
        });
	};
	refill_user_table: function(frm){
        frappe.call({
            method: "trebelge.api.refill_ebelge_users",
            args:{
            },
            callback: function(r){
                frm.set_value("last_run", r.message);
                frm.save();
            }
        });
	}
});
