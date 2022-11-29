from odoo import models, fields, api

class LineModel(models.Model):
    _name = 'bar_app.line_model'
    _description = 'This is a line model.'

    order = fields.Many2one("bar_app.order_model",string="Order",requiered=True)
    cuantity = fields.Integer(string="Cuantity",help="Cuantity of the product.")
    product = fields.Many2one("bar_app.product_model", string="Products", requiered=True)
    description = fields.Html(string="Description",help="Description of the product")
