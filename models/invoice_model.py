from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class InvoiceModel(models.Model):
    _name = 'bar_app.invoice_model'
    _description = 'This is a order model.'

    ref = fields.Integer(String="Ref",help="Number of the invoise",requiered=True,index=True)
    creationdate = fields.Datetime(srting="Date",help="Date",requiered=True,default=lambda self: datetime.now())
    lines = fields.One2many("bar_app.line_model", "cuantity" , string="Lines", requiered=True)
    bprice = fields.Float(string="Base price",compute="_getBasePrice",store=True)
    vat = fields.Integer(string="VAT",help="IVA")
    tprice = fields.Float(string="Total price",compute="_getTotalPrice",store=True)
    
    @api.constrains("numclients")
    def _checkValue(self):
        if self.numclients <= 0:
            raise ValidationError("The value of the number client order must be less than 0.")

    @api.depends("lines")
    def _getBasePrice(self):
        self.bprice = 0
        for line in self.lines:
            self.bprice += line.cuantity * line.product.price

    @api.depends("bprice","vat")
    def _getTotalPrice(self):
        self.tprice = self.bprice * (self.vat/100) + self.bprice
        