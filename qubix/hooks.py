# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import frappe
from frappe import _
# from . import __version__ as app_version

app_name = "qubix"
app_title = "Qubix"
app_publisher = "Subramani"
app_description = "Qubix Medicare"  
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "subramani.ac@promantia.com"
app_license = "MIT"

fixtures = ["Workflow", "Workflow State", "Workflow Action Master", "Client Script", "Server Script",
            {
                "dt": "Custom Field",
                "filters": [
                    [
                        "name", "in", [
                            "Supplier-lead_time",
                            "Purchase Receipt-approver",
                            "Purchase Order-approver",
                            "Warehouse-warehouse_manager",
                            "Stock Entry-warehouse_manager",
                            "Purchase Receipt-remark",
                            "Supplier-terms_and_conditions",
                            "Supplier-tc_name",
                            "Supplier-terms",
							"Job Card Time Log-employee",
							"Quality Inspection-accepted_quantity",
							"Quality Inspection-rejected_quantity",
							"Batch-mrp",
							"Job Card-batch_no",
							"Work Order-batch_no",
                            "Job Card Time Log-pcs_completed",
                            "Stock Entry-batch"
                        ]
                    ]
                ]
            },
            {"dt": "Report",
                "filters": [
                    [
                        "name", "in",
                        [
                            "Safety Stock vs Purchase Receipt",
                            "Item vs Supplier Report"

                        ]
                    ]
                ]
             },
            {"dt": "Print Format",
                "filters": [
                    [
                        "name", "in",
                        [
                            "Qubix PO format"

                        ]
                    ]
                ]
             },
            {"dt": "Notification",
                "filters": [
                    "is_standard != 1"
                ]
             },
            {"dt": "Role",
                "filters": [
                    [
                        "name", "in", ["Production User"]
                    ]
                ]
             },
            ]
doctype_js = {
#    "Purchase Order": "qubix/doctype/purchase_order/purchase_order.js",
 #   "Purchase Receipt": "qubix/doctype/purchase_receipt/purchase_receipt.js",
  #  "Stock Entry": "qubix/doctype/stock_entry/stock_entry.js",
}

doc_events = {
    "Purchase Order": {
        "on_submit": ["qubix.qubix.doctype.purchase_order.purchase_order.on_submit"]
    }
}

scheduler_events = {
    "daily": [
        "qubix.qubix.doctype.regulator_board_documents.regulator_board_documents.validate_expiry_date",
        "qubix.qubix.api.birthday_reminder",
        "qubix.qubix.api.anniversary_reminder"
    ]
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qubix/css/qubix.css"
# app_include_js = "/assets/qubix/js/qubix.js"

# include js, css files in header of web template
# web_include_css = "/assets/qubix/css/qubix.css"
# web_include_js = "/assets/qubix/js/qubix.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qubix/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "qubix.install.before_install"
# after_install = "qubix.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qubix.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"qubix.tasks.all"
# 	],
# 	"daily": [
# 		"qubix.tasks.daily"
# 	],
# 	"hourly": [
# 		"qubix.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qubix.tasks.weekly"
# 	]
# 	"monthly": [
# 		"qubix.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "qubix.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qubix.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qubix.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
