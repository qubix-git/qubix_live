# Copyright (c) 2013, Subramani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

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
			"label": _("ToDo"),
			"fieldtype": "Link",
			"options": "ToDo",
			"width": 200
		},
		{
			"fieldname": "date",
			"label": _("Due Date"),
			"fieldtype": "Date",
			"width": 200
		},
		{
			"fieldname": "priority",
			"label": _("Priority"),
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "owner",
			"label": _("Owner"),
			"options": "Data",
			"width": 200
		},
		{
			"fieldname": "reference_type",
			"label": _("Reference Type"),
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "reference_name",
			"label": _("Reference Name"),
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "assigned_by",
			"label": _("Assigned By"),
			"fieldtype": "Data",
			"width": 200
		}
	]

def get_data(filters,conditions):
	query="""select t.name,t.date, t.priority, t.owner, t.reference_type, t.reference_name, t.assigned_by,(DATEDIFF(t.date,'{days}'))as days_left from `tabToDo` t WHERE {conditions} AND t.status = 'Open' """.format(conditions=conditions,days=filters.get('due_date'))
	todo_list=frappe.db.sql(query, as_dict=True)

	return todo_list

def get_conditions(filters):
	conditions=""
	if filters.get('due_date'):
		conditions += " DATEDIFF(t.date,'{}')<= 7 ".format(filters.get('due_date'))
		conditions += " AND DATEDIFF(t.date,'{}')>= 0 ".format(filters.get('due_date'))
	return conditions

def get_chart_data(data):
	labels = []
	todo = []


	for lists in data:
		labels.append(lists.name)
		todo.append(lists.days_left)


	return {
		"data": {
			'labels': labels[:30],
			'datasets': [
				{
					"name": "Days Left",
					"values": todo[:30]
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
			"label": "Total ToDo's",
			"datatype": "Int",
		}
	]
