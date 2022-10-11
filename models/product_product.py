from odoo import fields, models, api
from datetime import date, datetime

class Product(models.Model):
    _inherit = "account.invoice"


    def update_date(self):
        for line in self:
            obj=self.env["pos.order"].search([("name","=",line.origin)],limit=1)
            if obj:
                #date1=datetime.strptime(obj.date_order,'%Y/%m/%d')
                date3=obj.date_order.date()
                #date2=fields.Date.to_string(date3)
                line.date_invoice=date3
                line.date_due=date3
                line.move_id.date=date3
            



class SaleOrder(models.Model):
    _inherit='sale.order'
 
    sale=fields.Date(string="prueba")
  
    def check(self):
        for line in self:
            if line.confirmation_date:
                #date1=datetime.strptime(line.confirmation_date,'%d/%m/%Y')
                date2=line.confirmation_date.date()
                line.sale=date2
            else:
                line.sale=False 



    

    