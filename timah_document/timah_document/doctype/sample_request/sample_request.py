# -*- coding: utf-8 -*-
# Copyright (c) 2018, DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SampleRequest(Document):
	pass

@frappe.whitelist()
def check_actual_qty_item_warehouse(dokumen_name):
	actual_qty = frappe.db.sql("""SELECT actual_qty FROM `tabBin` WHERE warehouse LIKE "%Gudang Lab%" AND item_code = "Timah A" """.format(dokumen_name))
	return actual_qty
