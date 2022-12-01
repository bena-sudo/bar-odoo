from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TableModel(models.Model):
    _name = 'bar_app.table_model'
    _description = 'This is a table model.'

    table = fields.Text(string="Table",help="Number of the table",requiered=True,index=True)
    orders = fields.One2many("bar_app.order_model", "table" , string="Orders", requiered=True)
    description = fields.Html(string="Description",help="Description of the table")
    