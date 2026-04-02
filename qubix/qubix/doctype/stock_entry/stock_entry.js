frappe.ui.form.on('Stock Entry', {
	before_save(frm) {    
        frappe.db.get_value("Warehouse",frm.doc.to_warehouse,"warehouse_manager",(a)=>{
            frm.set_value("warehouse_manager",a.warehouse_manager)
        });
	}
})