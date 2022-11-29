from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductModel(models.Model):
    _name = 'bar_app.product_model'
    _description = 'This is a product model.'
    _sql_constraints = [('bar_app_productname_uniq','UNIQUE (name)','There cannot be two products with the same name!!')]

    name = fields.Text(string="Product name",help="Name of the product",requiered=True,index=True)
    currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self:self.env.user.company_id.currency_id)
    price = fields.Monetary(string="Price",help="Price of the product")
    category = fields.Many2one("bar_app.category_model", string="Category")
    ingredients = fields.Many2many("bar_app.ingredient_model", string="Ingredients", relation="product2ingredient")
    description = fields.Html(string="Description",help="Description of the product")

    @api.constrains("name")
    def _checkLength(self):
        if len(self.name) < 5:
            raise ValidationError("The length of the name product must be less than 5 caracters.")

    @api.constrains("price")
    def _checkValue(self):
        if self.price <= 0:
            raise ValidationError("The value of the price product must be less than 0.")
    
