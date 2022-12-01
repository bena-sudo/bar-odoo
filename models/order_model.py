from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class OrderModel(models.Model):
    _name = 'bar_app.order_model'
    _description = 'This is a order model.'

    order = fields.Integer(String="Reference",help="Number of the order",requiered=True,index=True)
    table = fields.Many2one("bar_app.table_model", string="Table")
    creationdate = fields.Datetime(srting="Date",help="Date",requiered=True,default=lambda self: datetime.now())
    numclients = fields.Integer(string="Number clients",help="Numbers of the clients.",requiered=True)
    client = fields.Text(string="Client",help="Name of the client.",requiered=True)
    waiter = fields.Text(string="Waiter",help="Name of the waiter.",requiered=True)
    lines = fields.One2many("bar_app.line_model", "cuantity" , string="Products", requiered=True)
    tprice = fields.Float(string="Total price",help="Total price of the order.")
    
    @api.constrains("numclients")
    def _checkValue(self):
        if self.numclients <= 0:
            raise ValidationError("The value of the number client order must be less than 0.")