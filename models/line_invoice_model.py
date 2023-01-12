from odoo import models, fields, api

class LineInvoiceModel(models.Model):
    _name = 'bar_app.line_invoice_model'
    _description = 'This is a line invoice model.'

    lineId = fields.Many2one("bar_app.invoice_model", string="Reference")
    cuantity = fields.Integer(string="Cuantity",help="Cuantity of the product.")
    product = fields.Many2one("bar_app.product_model", string="Product", default=1)
    description = fields.Html(string="Description",help="Description of the product")
