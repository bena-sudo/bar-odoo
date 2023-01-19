from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class InvoiceModel(models.Model):
    _name = 'bar_app.invoice_model'
    _description = 'This is a order model.'
    _rec_name = 'reference'

    reference = fields.Integer(string="Invoice number",index=True,default = lambda self : self._generateRef())
    client = fields.Char(string="Client",help="Client name",required=True)
    creationdate = fields.Date(srting="Date",help="Date",redonly=1,default=lambda self: datetime.today())
    lines = fields.One2many("bar_app.line_invoice_model", "lineId" , string="Lines")
    bprice = fields.Float(string="Base price",compute="_getBasePrice",store=True)
    vat = fields.Selection([ ('0','0'),('4','4'),('10','10'),('21','21'),],string='VAT',help="VAT number % to add to base price",default="10")
    tprice = fields.Float(string="Total price",compute="_getTotalPrice",store=True)
    state = fields.Char(String="state",default="D")

    @api.depends('lines')
    def _getBasePrice(self):
        self.bprice = 0
        for line in self.lines:
            self.bprice += line.cuantity * line.product.price

    @api.depends('bprice','vat')
    def _getTotalPrice(self):
        self.tprice = self.bprice * (int(self.vat)/100) + self.bprice
        
    def confirmInvoice(self):    
        self.state = 'C'

    def _generateRef(self):
        ids = self.env["bar_app.invoice_model"].sudo().search_read([],["reference"])
        if len(ids) > 0:
            id = ids[-1]
            return int(id['reference'])+1    
        return 1