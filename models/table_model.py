from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TableModel(models.Model):
    _name = 'bar_app.table_model'
    _description = 'This is a table model.'
    _rec_name = 'table'

    table = fields.Text(string="Table",help="Information of the table",required=True,index=True)
    orders = fields.One2many("bar_app.order_model", "table" , string="Orders")
    description = fields.Char(string="Description",help="Description of the table")
    state = fields.Boolean(string="State",default=False)

    def changeState(self):
        if(self.state):
            self.state = False
        else:
            self.state = True
    