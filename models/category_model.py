from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CategoryModel(models.Model):
    _name = 'bar_app.category_model'
    _description = 'This is a category model.'
    _rec_name = 'complete_name'
    _order = 'complete_name'
    _sql_constraints = [('bar_app_categoryname_uniq','UNIQUE (name)','There cannot be two catgorys with the same name!!')]
    
    name = fields.Char(string="Category",help="Name of the category",required=True,index=True)
    complete_name = fields.Char(string="Complete name",compute="_complete_name", recursive=True,store=True)
    photo = fields.Binary(string="Foto")
    product = fields.Many2many("bar_app.product_model", string="Product", relation="product2category")
    parent_id = fields.Many2one("bar_app.category_model", string="Category parent", index=True, ondelete="cascade")
    description = fields.Char(string="Description",help="Description of the category")

    @api.constrains("name")
    def _checkLength(self):
        if len(self.name) < 1:
            raise ValidationError("The length of the name category must be less than 1 caracters.")

    @api.depends("name","parent_id.complete_name")
    def _complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' %(category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name