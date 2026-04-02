// Copyright (c) 2016, Subramani and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Pending Purchase Order Report"] = {
	"filters": [
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		{
		"fieldname": "transaction_date",
		"label": __("Date"),
		"fieldtype": "Date",
		"default": frappe.datetime.get_today(),
		"reqd": 1
		}
	]
};
