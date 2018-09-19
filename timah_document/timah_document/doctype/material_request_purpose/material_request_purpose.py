# -*- coding: utf-8 -*-
# Copyright (c) 2018, DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MaterialRequestPurpose(Document):
	pass

@frappe.whitelist()
def make_material_request(purpose):
	je_doc = frappe.new_doc('Material Request')
	je_doc.purpose = purpose
	return je_doc.as_dict() 