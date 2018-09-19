# -*- coding: utf-8 -*-
# Copyright (c) 2018, DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProductSampling(Document):
	pass
@frappe.whitelist()
def make_coa(purpose):
	je_doc = frappe.new_doc('COA')
	je_doc.product_sampling_no = purpose

	doc_asli = frappe.get_doc("Product Sampling", purpose)

	je_doc.date_of_inspecton = doc_asli.date		
	return je_doc.as_dict() 

@frappe.whitelist()
def make_rfp(purpose):
	je_doc = frappe.new_doc('RFP')
	je_doc.product_sampling_no = purpose
	doc_asli = frappe.get_doc("Product Sampling", purpose)

	je_doc.document_date = doc_asli.date
	return je_doc.as_dict()