"""Developer Assignment Module
Copyright (c) 2024, Rijal Tanjung  and contributors. 
For license information, please see license.txt
"""

import frappe
from frappe.model.document import Document
from developer.constants import DOCTYPE_DEVELOPER


class DeveloperAssignment(Document):
    """Developer Assignment controller

    Args:
        Document (_type_): Frappe document
    """

    def validate(self):
        """Controller hook method. Called right before save"""
        self.developer_name = frappe.get_cached_value(
            DOCTYPE_DEVELOPER, self.developer, "developer_name"
        )
