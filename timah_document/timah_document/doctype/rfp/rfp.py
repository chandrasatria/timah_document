# -*- coding: utf-8 -*-
# Copyright (c) 2018, DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RFP(Document):
	pass

@frappe.whitelist()
def check_production_order(purpose):
	cek_product = frappe.db.sql(""" SELECT rfp FROM `tabProduction Order` WHERE rfp = "{}" """.format(purpose))

	if cek_product:
		return "found"
	else:	
		return "not found"


@frappe.whitelist()
def make_production_order(purpose):
	je_doc = frappe.new_doc('Production Order')
	je_doc.rfp = purpose
	return je_doc.as_dict()