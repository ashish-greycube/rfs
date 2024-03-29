from . import __version__ as app_version

app_name = "rfs"
app_title = "Request For Sample"
app_publisher = "GreyCube Technologies"
app_description = "Request for sample from supplier"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rfs/css/rfs.css"
# app_include_js = ["carrier_rfs_quick_entry.bundle.js"]

# include js, css files in header of web template
# web_include_css = "/assets/rfs/css/rfs.css"
# web_include_js = "/assets/rfs/js/rfs.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rfs/public/scss/website"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "rfs.utils.jinja_methods",
#	"filters": "rfs.utils.jinja_filters"
# }
jinja = {
    "methods": [
        "rfs.utils.jinja.get_qr_code"
    ],
}
# Installation
# ------------

# before_install = "rfs.install.before_install"
after_install = "rfs.install.create_connections"
after_migrate = "rfs.migrations.create_connections"
# Uninstallation
# ------------

# before_uninstall = "rfs.uninstall.before_uninstall"
# after_uninstall = "rfs.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rfs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Communication": {
        "on_update": "rfs.utils.api.after_insert_communication"
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"rfs.tasks.all"
#	],
#	"daily": [
#		"rfs.tasks.daily"
#	],
#	"hourly": [
#		"rfs.tasks.hourly"
#	],
#	"weekly": [
#		"rfs.tasks.weekly"
#	],
#	"monthly": [
#		"rfs.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "rfs.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "rfs.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "rfs.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"rfs.auth.validate"
# ]
fixtures = [
    {
        "doctype": "Email Template",
        "filters": {"name": "Supplier Initial Sourcing Request"}
    },
    {
        "doctype": "Print Format",
        "filters": {"name": "Sourcing Email PDF"}
    }
    ]