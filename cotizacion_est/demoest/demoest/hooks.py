# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "demoest"
app_title = "Demoest"
app_publisher = "Daniel"
app_description = "Demo app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "desp002@gmail.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/demoest/css/demoest.css"
# app_include_js = "/assets/demoest/js/demoest.js"

# include js, css files in header of web template
# web_include_css = "/assets/demoest/css/demoest.css"
# web_include_js = "/assets/demoest/js/demoest.js"

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

# Installation
# ------------

# before_install = "demoest.install.before_install"
# after_install = "demoest.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "demoest.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"demoest.tasks.all"
# 	],
# 	"daily": [
# 		"demoest.tasks.daily"
# 	],
# 	"hourly": [
# 		"demoest.tasks.hourly"
# 	],
# 	"weekly": [
# 		"demoest.tasks.weekly"
# 	]
# 	"monthly": [
# 		"demoest.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "demoest.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "demoest.event.get_events"
# }

