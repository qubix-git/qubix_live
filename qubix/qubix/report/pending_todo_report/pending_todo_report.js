// Copyright (c) 2016, Subramani and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Pending ToDo Report"] = {
	"filters": [
		{
		"fieldname": "due_date",
		"label": __("Date"),
		"fieldtype": "Date",
		"default": frappe.datetime.get_today(),
		"reqd": 1
		}
	]
};
