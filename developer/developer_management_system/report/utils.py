""" Developer App report helpers"""

from frappe import _
from developer.constants import FIELDTYPE_CURRENCY, FIELDTYPE_INTEGER, FIELDTYPE_FLOAT


def get_column(
    label: str, fieldname: str, fieldtype: str, options: str = None, width: int = None
) -> dict:
    """Get report column builder

    Args:
        label (str): _description_
        fieldname (str): _description_
        fieldtype (str): _description_
        options (str, optional): _description_. Defaults to None.
        width (int, optional): _description_. Defaults to None.

    Returns:
        dict: _description_
    """
    align_right_column_types = (FIELDTYPE_CURRENCY, FIELDTYPE_INTEGER, FIELDTYPE_FLOAT)
    column = dict(
        label=_(label),
        fieldname=fieldname,
        fieldtype=fieldtype,
        options=options,
        width=width,
        align="right" if fieldtype in align_right_column_types else "left",
    )
    return column
