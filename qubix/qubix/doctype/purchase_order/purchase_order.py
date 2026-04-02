# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, nowdate, getdate
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname

from erpnext.controllers.selling_controller import SellingController


class StockEntry(Document):
    pass

def on_submit(doc,method):
    doc.db_set('approver',frappe.session.user)
