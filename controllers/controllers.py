# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json


class BarApp(http.Controller):
# CATEGORY
        # GET CATEGORYS
        @http.route('/bar_app/getAllCategorys', auth='public', type="http")
        def category(self, **kw):
                tdata = http.request.env["bar_app.category_model"].sudo(
                ).search_read([], ["name", "product", "description"])
                data = {"status": 200,
                        "data": tdata}
                return http.Response(json.dumps(data).encode("utf8"), mimetype="application/json")

# PRODUCT
        # GET PRODUCTS
        @http.route('/bar_app/getAllProducts', auth='public', type="http")
        def product(self, **kw):
                tdata = http.request.env["bar_app.product_model"].sudo().search_read(
                [], ["name", "price", "category", "ingredients", "description"])
                data = {"status": 200,
                        "data": tdata}
                return http.Response(json.dumps(data).encode("utf8"), mimetype="application/json")

# INGREDEINT
        # GET INGREDIENTS
        @http.route('/bar_app/getAllIngredients', auth='public', type="http")
        def ingredient(self, **kw):
                tdata = http.request.env["bar_app.ingredient_model"].sudo(
                ).search_read([], ["name", "products", "description"])
                data = {"status": 200,
                        "data": tdata}
                return http.Response(json.dumps(data).encode("utf8"), mimetype="application/json")
