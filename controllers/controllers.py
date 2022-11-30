# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json


class BarApp(http.Controller):
    @http.route('/bar_app/category', auth='public',type="http")
    def category(self, **kw):
        tdata = http.request.env["bar_app.category_model"].sudo().search_read([],["name","product","description"])
        data = {"status":200,
                "data":tdata }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")


    @http.route('/bar_app/product', auth='public',type="http")
    def product(self, **kw):
        tdata = http.request.env["bar_app.product_model"].sudo().search_read([],["name","price","category","ingredients","description"])
        data = {"status":200,
                "data":tdata }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar_app/ingredient', auth='public',type="http")
    def ingredient(self, **kw):
        tdata = http.request.env["bar_app.ingredient_model"].sudo().search_read([],["name","products","description"])
        data = {"status":200,
                "data":tdata }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

#     @http.route('/task_app/task_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_app/task_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_app.listing', {
#             'root': '/task_app/task_app',
#             'objects': http.request.env['task_app.task_app'].search([]),
#         })

#     @http.route('/task_app/task_app/objects/<model("task_app.task_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_app.object', {
#             'object': obj
#         })
