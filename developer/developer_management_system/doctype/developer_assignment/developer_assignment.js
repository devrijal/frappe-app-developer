// Copyright (c) 2024, Rijal Tanjung  and contributors
// For license information, please see license.txt

frappe.ui.form.on("Developer Assignment", {
  refresh: function (frm) {
    frm.events.set_assignment_time(frm);
  },
  set_assignment_time: function (frm) {
    if (frm.doc.docstatus > 0 || frm.doc.assignment_time) {
      return;
    }

    frm.set_value("assignment_time", frappe.datetime.now_time());
  },
});
