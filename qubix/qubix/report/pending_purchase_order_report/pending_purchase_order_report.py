# Copyright (c) 2013, Subramani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import date
from datetime import timedelta
from datetime import datetime

def execute(filters=None):
	columns=get_columns()
	data = []
	conditions=get_conditions(filters)

	data = get_data(filters,conditions)
	chart = get_chart_data(data)
	report_summary=get_report_summary(data)
	return columns, data, None, chart, report_summary 


def get_columns():
	return [
		{
			"fieldname": "name",
			"label": _("Purchase Order"),
			"fieldtype": "Link",
			"options": "Purchase Order",
			"width": 200
		},
		{
			"fieldname": "supplier",
			"label": _("Supplier"),
			"fieldtype": "Link",
			"options": "Supplier",
			"width": 200
		},
		{
			"fieldname": "transaction_date",
			"label": _("Transaction Date"),
			"fieldtype": "Date",
			"width": 200
		},
		{
			"fieldname": "schedule_date",
			"label": _("Required By"),
			"fieldtype": "Date",
			"width": 200
		},
		{
			"fieldname": "item_code",
			"label": _("Item Code"),
			"fieldtype": "Link",
			"options": "Item",
			"width": 200
		},
		{
			"fieldname": "item_name",
			"label": _("Item Name"),
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "grand_total",
			"label": _("Total"),
			"fieldtype": "Data",
			"width": 200
		}
	]

def get_data(filters,conditions):
	query="""select po.name, po.supplier, po.transaction_date, po.schedule_date,poi.item_code,poi.item_name, po.grand_total, (DATEDIFF(po.schedule_date,'{days}'))as days_left from `tabPurchase Order` po LEFT JOIN `tabPurchase Order Item` poi ON poi.parent=po.name WHERE {conditions} AND po.status != 'Completed' AND po.status != 'Cancelled' AND po.status != 'Delivered' AND po.status != 'Closed' """.format(conditions=conditions,days=filters.get('transaction_date'))
	purchase_order_list=frappe.db.sql(query, as_dict=True)

	return purchase_order_list

def get_conditions(filters):
	conditions=""
	if filters.get('company'):
		conditions += " po.company = '{}'".format(filters.get('company'))
	if filters.get('transaction_date'):
		conditions += " AND DATEDIFF(po.schedule_date,'{}' ) <=7 ".format(filters.get('transaction_date'))
		conditions += " AND DATEDIFF(po.schedule_date,'{}') >=0 ".format(filters.get('transaction_date'))
	return conditions


def get_chart_data(data):
	labels = []
	po = []


	for order in data:
		labels.append(order.name)
		po.append(order.days_left)


	return {
		"data": {
			'labels': labels[:30],
			'datasets': [
				{
					"name": "Days Left",
					"values": po[:30]
				}
			]
		},
		"type": "bar",
		"colors": ["#fc4f51"],
		"barOptions": {
			"stacked": False
		}
	}

def get_report_summary(data):
	if not data:
		return None

	total = len([ord.name for ord in data])

	return [
		{
			"value": total,
			"indicator": "Blue",
			"label": "Total Orders",
			"datatype": "Int",
		}
	]
