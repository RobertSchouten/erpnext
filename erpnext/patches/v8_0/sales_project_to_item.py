from __future__ import unicode_literals
import frappe

def execute():
	for parent in ["Sales Order","Sales Invoice", "Delivery Note"]:
		frappe.reload_doctype(parent+" item")
		frappe.db.sql("""update `tab{0}` as parent, `tab{0} Item` as child  set
			child.project = parent.project
			where parent.name = child.parent AND 
			ifnull(parent.project, "")!=""
		""".format(parent))