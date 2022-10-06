from odoo import fields, models, api
from datetime import date

class Product(models.Model):
    _inherit = "account.invoice"


    def update_date(self):
        for line in self:
            obj=self.env["pos.order"].search([("name","=",line.origin)],limit=1)
            date1=date(fields.Datetime.from_string(obj.date_order))
            date2=fields.Date.to_string(date1)
            line.date_invoice=date2
            line.date_due=date2
            



  



    

    