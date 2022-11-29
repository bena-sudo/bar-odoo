from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OrderModel(models.Model):
    _name = 'bar_app.order_model'
    _description = 'This is a order model.'

    table = fields.Text(string="Table",help="Number of the table",requiered=True,index=True)
    numclients = fields.Integer(string="Number clients",help="Numbers of the clients.",requiered=True)
    client = fields.Text(string="Client",help="Name of the client.")
    waiter = fields.Text(string="Waiter",help="Name of the waiter.",requiered=True)
    products = fields.Many2many("bar_app.product_model", string="Products", requiered=True, relation="product2order")
    tprice = fields.Float(string="Total price",help="Total price of the order.")
    
    @api.constrains("table")
    def _checkValue(self):
        if self.table <= 0:
            raise ValidationError("The value of the table order must be less than 0.")

    @api.constrains("numclients")
    def _checkValue(self):
        if self.numclients <= 0:
            raise ValidationError("The value of the number client order must be less than 0.")