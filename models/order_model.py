from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class OrderModel(models.Model):
    _name = 'bar_app.order_model'
    _description = 'This is a order model.'
    _rec_name = 'order'

    order = fields.Integer(string="Order number",index=True,default = lambda self : self._generateOrder())
    table = fields.Many2one("bar_app.table_model", string="Table")
    numclients = fields.Integer(string="Number clients",help="Numbers of the clients.",default=1,required=True)
    client = fields.Text(string="Client",help="Name of the client.",required=True)
    waiter = fields.Text(string="Waiter",help="Name of the waiter.",required=True,default=lambda self : self.env.user.name)
    creationdate = fields.Date(srting="Date",help="Date",default=lambda self: datetime.now())
    lines = fields.One2many("bar_app.line_model", "order" , string="Products")
    tprice = fields.Float(string="Total price",compute="_getTotalPrice",store=True)
    state = fields.Char(String="state",default="D")

    @api.constrains("numclients")
    def _checkValue(self):
        if self.numclients <= 0:
            raise ValidationError("The value of the number client order must be less than 0.")

    @api.depends("lines")
    def _getTotalPrice(self):
        self.tprice = 0
        for line in self.lines:
            self.tprice += line.cuantity * line.product.price

    def _generateOrder(self):
        ids = self.env["bar_app.order_model"].sudo().search_read([],["order"])
        if len(ids) > 0:
            id = ids[-1]
            return int(id['order'])+1    
        return 1

    def confirmInvoice(self):    
        self.state = 'C'
        invoice = {}
        invoice["client"] = self.client
        invoice["creationdate"] = self.creationdate
        inv = self.env["bar_app.invoice_model"].sudo().create(invoice)
        
        for l in self.lines:
            line = {}
            line["lineId"] = inv.id
            line["cuantity"] = l.cuantity
            line["product"] = l.product.id
            line["description"] = l.description
            self.env["bar_app.line_invoice_model"].sudo().create(line)

    @api.onchange("table")
    def _changeClient(self):    
        self.client = self.table.table