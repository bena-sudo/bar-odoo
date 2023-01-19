from odoo import models, fields, api

class LineModel(models.Model):
    _name = 'bar_app.line_model'
    _description = 'This is a line model.'

    order = fields.Many2one("bar_app.order_model",string="Order")
    cuantity = fields.Integer(string="Cuantity",help="Cuantity of the product.",default=1,required=True)
    product = fields.Many2one("bar_app.product_model", string="Product",required=True)
    description = fields.Html(string="Description",help="Description of the product")
