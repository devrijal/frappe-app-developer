// Copyright (c) 2024, Rijal Tanjung  and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Developer Weekly Assignment"] = {
  filters: [
    {
      fieldname: "from_date",
      label: __("From Date"),
      fieldtype: "Date",
      default: frappe.datetime.add_days(frappe.datetime.get_today(), -7),
      reqd: 1,
    },
    {
      fieldname: "to_date",
      label: __("To Date"),
      fieldtype: "Date",
      default: frappe.datetime.get_today(),
      reqd: 1,
    },
    {
      fieldname: "developer",
      label: __("Developer"),
      fieldtype: "Link",
      options: "Developer",
    },
  ],
};
