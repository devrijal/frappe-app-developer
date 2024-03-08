"""Developer app desktop configuration"""

from typing import List
from frappe import _


def get_data() -> List[dict]:
    """Get data for frappe app

    Returns:
            list: _description_
    """
    return [
        {
            "module_name": "Developer Management System",
            "color": "grey",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("Developer Management System"),
        }
    ]
