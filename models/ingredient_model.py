from odoo import models, fields, api
from odoo.exceptions import ValidationError

class IngredientModel(models.Model):
    _name = 'bar_app.ingredient_model'
    _description = 'This is a ingredient model.'
    _sql_constraints = [('bar_app_ingredientname_uniq','UNIQUE (name)','There cannot be two ingredients with the same name!!')]

    name = fields.Text(string="Product name",help="Name of the product",required=True,index=True)
    products = fields.Many2many("bar_app.product_model", string="Products", relation="product2ingredient")
    description = fields.Char(string="Description",help="Description of the ingredient")

    @api.constrains("name")
    def _checkLength(self):
        if len(self.name) < 2:
            raise ValidationError("The length of the name ingredient must be less than 2 caracters.")