import frappe
from frappe.model.document import Document


class lead(Document):
    def after_insert(self):
     x= frappe.new_doc("deal")
     x.deal_name= self.name1
     x.status=self.status
     x.lead=self.name
     x.lead_owner=self.oowner
     x.save()
    def on_trash(self):
      y=frappe.get_list("deal",filters={"lead":self.name})
      x = frappe.get_doc("deal",y[0])
      x.lead = None
      x.save()
      delete(y[0]["name"])
def delete(z):
      frappe.delete_doc("deal",z)
