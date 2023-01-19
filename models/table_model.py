from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TableModel(models.Model):
    _name = 'bar_app.table_model'
    _description = 'This is a table model.'
    _rec_name = 'table'

    table = fields.Text(string="Table",help="Number of the table",required=True,index=True)
    numclients = fields.Integer(string="Number clients",help="Numbers of the clients.",default=1,required=True)
    client = fields.Text(string="Client",help="Name of the client.",required=True)
    waiter = fields.Text(string="Waiter",help="Name of the waiter.",required=True)
    orders = fields.One2many("bar_app.order_model", "table" , string="Orders", required=True)
    description = fields.Html(string="Description",help="Description of the table")
    