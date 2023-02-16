import frappe


def execute():
	frappe.reload_doctype("Request For Sample RFS")
	property_setter_default_name = frappe.db.exists(
		"Property Setter", 
		dict(doc_type="Request For Sample RFS",field_name="naming_series", property="default",value="PUR-RFS-.YEAR.-.####")
	)
	if property_setter_default_name:    
		frappe.db.sql(
			"""
			DELETE FROM `tabProperty Setter`
			WHERE `tabProperty Setter`.doc_type='Request For Sample RFS'
				AND `tabProperty Setter`.value='PUR-RFS-.YEAR.-.####'
				AND `tabProperty Setter`.property='default'
                AND `tabProperty Setter`.field_name='naming_series'
		"""
		)        

	property_setter_options_name = frappe.db.exists(
		"Property Setter", 
		dict(doc_type="Request For Sample RFS",field_name="naming_series", property="options",value="PUR-RFS-.YEAR.-.####")
	)
	if property_setter_options_name:    
		frappe.db.sql(
			"""
			DELETE FROM `tabProperty Setter`
			WHERE `tabProperty Setter`.doc_type='Request For Sample RFS'
				AND `tabProperty Setter`.value='PUR-RFS-.YEAR.-.####'
				AND `tabProperty Setter`.property='options'
                AND `tabProperty Setter`.field_name='naming_series'
		"""
		)         