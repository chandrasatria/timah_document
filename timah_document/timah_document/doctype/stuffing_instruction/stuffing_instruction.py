# -*- coding: utf-8 -*-
# Copyright (c) 2018, DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StuffingInstruction(Document):
	pass
@frappe.whitelist()
def make_delivery_note(purpose):
	je_doc = frappe.new_doc('Delivery Note')
	je_doc.stuffing_instruction = purpose
	doc_awal = frappe.get_doc("Stuffing Instruction", purpose)
	je_doc.customer = doc_awal.customer_name

	return je_doc.as_dict() 