# -*- coding: utf-8 -*-
# Copyright (c) 2021, Subramani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import date
from frappe import _
from six import string_types
from frappe.utils import date_diff
from frappe.core.doctype.communication.email import make

class RegulatorBoardDocuments(Document):
	pass


def validate_expiry_date():
	docName=frappe.get_all("Regulator Board Documents")
	for values in docName:
		docList=frappe.db.get_list("Regulator Board Documents",filters={'name':values.name},fields={'*'})
		for row in docList:
				documentList=frappe.db.get_list("Regulator Board Documents Details",filters={'parenttype':'Regulator Board Documents','parent':row.name},fields={'*'})
				for val in documentList:
					new_date=str(date.today())
					expire_date=date_diff(val.expiry_date,new_date)
					if expire_date==15 and val.is_active==1:
						user=row.user
						message="Regulator Board Document "+val.document_name+" will be expired in 15 days."
						if user:
							make(
									subject = row.name,
									recipients = user,
									communication_medium = "Email",
									content = message,
									send_email = True
							)
			
