from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CategoryModel(models.Model):
    _name = 'bar_app.category_model'
    _description = 'This is a category model.'
    _sql_constraints = [('bar_app_categoryname_uniq','UNIQUE (name)','There cannot be two catgoris with the same name!!')]
    
    name = fields.Char(string="Category",help="Name of the category",requiered=True,index=True)
    photo = fields.Binary(string="Foto",help="Password of the student")
    product = fields.One2many("bar_app.product_model", "category", string="Product")
    description = fields.Html(string="Description",help="Description of the category")

    @api.constrains("name")
    def _checkLength(self):
        if len(self.name) < 5:
            raise ValidationError("The length of the name category must be less than 5 caracters.")