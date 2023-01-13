from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class OrderModel(models.Model):
    _name = 'bar_app.order_model'
    _description = 'This is a order model.'

    order = fields.Integer(String="Reference",help="Number of the order",requiered=True,index=True)
    table = fields.Many2one("bar_app.table_model", string="Table")
    creationdate = fields.Date(srting="Date",help="Date",requiered=True,default=lambda self: datetime.now())
    lines = fields.One2many("bar_app.line_model", "order" , string="Products", requiered=True)
    tprice = fields.Float(string="Total price",compute="_getTotalPrice",store=True)
    
    @api.constrains("numclients")
    def _checkValue(self):
        if self.numclients <= 0:
            raise ValidationError("The value of the number client order must be less than 0.")

    @api.depends("lines")
    def _getTotalPrice(self):
        self.tprice = 0
        for line in self.lines:
            self.tprice += line.cuantity * line.product.price