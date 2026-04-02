# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import date
from frappe.desk.doctype.notification_log.notification_log import  enqueue_create_notification
from frappe.utils import today

def birthday_reminder(doc,method):
    employees_born_today=frappe.db.sql("""SELECT employee_name FROM `tabEmployee` WHERE DAY(date_of_birth) = DAY('{today}') AND MONTH(date_of_birth) = MONTH('{today}') AND `status` = 'Active'""".format(today=today()), as_dict=1)
    user_list=frappe.db.sql("""SELECT email FROM `tabUser` where enabled=1 """, as_dict=1)
    create_system_notification(employees_born_today,user_list)

def anniversary_reminder(doc, method):
    emps_joined_today = {}
    query = """SELECT employee_name, date_of_joining FROM `tabEmployee` WHERE DAY(date_of_joining) = DAY('{today}') AND MONTH(date_of_joining) = MONTH('{today}') AND `status` = 'Active'""".format(today=today())
    employees_joined_today = frappe.db.sql(query, as_dict=1)
    for emp in employees_joined_today:
        emp['anniversary_date'] = date.today().year - emp['date_of_joining'].year
        emps_joined_today[emp['employee_name']] = emp
    get_all_emps = """SELECT email FROM `tabUser` WHERE enabled=1"""
    user_list = frappe.db.sql(get_all_emps, as_dict=1)
    users = ''
    for user in user_list:
        users+=user.email +', '
    users = users[:-2]
    send_anniversary_notification(emps_joined_today, users)

@frappe.whitelist()
def new_joinee(employee_name):
    get_all_emps = """SELECT email FROM `tabUser` WHERE enabled=1"""
    user_list = frappe.db.sql(get_all_emps, as_dict=1)
    users = ''
    for user in user_list:
        users+=user.email + ', '
    users = users[:-2]

    subject = f"{employee_name} joined Qubix."
    message = f"Welcoming {employee_name} to Qubix."
    notification_doc = {
            'type': 'Alert',
            'subject': subject,
            'email_content': message
        }
    enqueue_create_notification(users, notification_doc)

def send_anniversary_notification(employees_list, users):
    num = ''
    for employee in employees_list:
        subject = f"Today is {employee.employee_name}'s Work Anniversary."
        if employee.anniversary_date == 1:
            num = f'{employee.anniversary_date}st'
        elif employee.anniversary_date == 2:
            num = f'{employee.anniversary_date}nd'
        elif employee.anniversary_date == 3:
            num = f'{employee.anniversary_date}rd'
        else:
            num = f'{employee.anniversary_date}th'

        message = f"Happy {num} Work Anniversary {employee.employee_name}." 
        notification_doc = {
            'type': 'Alert',
            'subject': subject,
            'email_content': message
        }
        enqueue_create_notification(users, notification_doc)

def create_system_notification(employees_born_today, user_list):
    users=''
    for user in user_list:
        users+=user.email +', '
    users = users[:-2]
    for employee in employees_born_today:
        subject = f"Today is { employee.employee_name}'s Birthday"
        message=f"Happy Birthday {employee.employee_name}"

        notification_doc = {
            'type': 'Alert',
            'subject': subject,
            'email_content': message
        }
        enqueue_create_notification(users, notification_doc)