"""Developer weekly report module"""

# Copyright (c) 2024, Rijal Tanjung  and contributors
# For license information, please see license.txt

import frappe
from pypika import functions as fn
from developer.constants import (
    DOCTYPE_DEVELOPER,
    DOCTYPE_DEVELOPER_ASSIGNMENT,
    FIELDTYPE_DATA,
    FIELDTYPE_DATE,
    FIELDTYPE_TEXT,
)
from developer.developer_management_system.report.utils import get_column


def execute(filters=None):
    """Frappe report entry point method.

    Args:
        filters (dict, optional): Dictionary filters. Defaults to None.

    Returns:
        list:
    """
    columns, data = get_columns(), get_data(filters)
    return columns, data


def get_columns():
    """Get report columns

    Returns:
        list: List of columns
    """
    columns = []

    columns.append(get_column("Date", "assignment_date", FIELDTYPE_DATE))
    columns.append(get_column("Date", "assignment_day", FIELDTYPE_DATA))
    # columns.append(
    #     get_column("Developer", "developer", FIELDTYPE_LINK, DOCTYPE_DEVELOPER)
    # )
    columns.append(
        get_column("Developer Name", "developer_name", FIELDTYPE_DATA, width=200)
    )
    columns.append(get_column("Task", "task", FIELDTYPE_TEXT, width=400))
    columns.append(get_column("Obstacle", "obstacle", FIELDTYPE_TEXT, width=400))

    return columns


def get_data(filters):
    """Get report data

    Args:
        filters (dict): Report filter map

    Returns:
        list: List of data
    """
    developer = frappe.qb.DocType(DOCTYPE_DEVELOPER)

    developer_assignment = frappe.qb.DocType(DOCTYPE_DEVELOPER_ASSIGNMENT)

    query = (
        frappe.qb.from_(developer)
        .left_join(developer_assignment)
        .on(developer_assignment.developer == developer.name)
        .select(
            developer_assignment.assignment_date,
            developer_assignment.developer_name,
            developer_assignment.task,
            developer_assignment.obstacle,
            fn.ToChar(developer_assignment.assignment_date, "Day", "assignment_day"),
        )
    )

    query = apply_filters(query, filters)

    data = query.run(as_dict=1)

    return data


def apply_filters(query, filters: dict):
    """A method to apply user's filters
    Args:
        query (_type_):
        filters (dict):

    Returns:
        _type_: query
    """
    developer_assignment = frappe.qb.DocType(DOCTYPE_DEVELOPER_ASSIGNMENT)

    if filters.get("is_cancelled", False):
        query = query.where(developer_assignment.docstatus == 2)
    else:
        query = query.where(developer_assignment.docstatus == 1)

    if filters.get("developer", False):
        query = query.where(developer_assignment.developer == filters.get("developer"))

    return query
