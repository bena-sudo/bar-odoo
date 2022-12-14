# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json, request


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

    # ADD CATEGORY
    @http.route('/bar_app/addCategory', auth='public', type="json", method="POST")
    def addCategory(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.category_model"].sudo().create(
                response)
            data = {"status": 201, "id": result.id}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
        return data

    # GET CATEGORY BY ID
    @http.route('/bar_app/getCategory/<int:id>', auth='public', type="http")
    def getCategoryById(self, id=None, **kw):
        if id:
            domain = [{"id", "=", id}]
        else:
            domain = []
        taskdata = http.request.env["bar_app.category_model"].sudo().search_read(
            domain, ["name", "product", "description"])
        data = {"status": 200,
                "data": taskdata}
        return http.Response(json.dumps(data).encode("utf8"), mimetype="application/json")

    # UPDATE CATEGORY
    @http.route('/bar_app/updateCategory', auth="public", type="json", method="PUT")
    def updateCategory(self, **kw):
        response = request.jsonrequest
        domain = [("id", "=", response["id"])]
        try:
            x = http.request.env["bar_app.category_model"].sudo().search(
                domain)
            updated = x.sudo().write(response)
            if (updated):
                data = {"status": 200, "result": x.id}
            else:
                data = {"status": 400, "result": "Category not modified"}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

    # DELETE CATEGORY
    @http.route('/bar_app/deleteCategory', auth="public", type="json", method="DELETE")
    def deleteCat(self, **kw):
        response = request.jsonrequest
        domain = [("id", "=", response["id"])]
        try:
            x = http.request.env["task_app.category_model"].sudo().search(
                domain).unlink()
            data = {"status": 200, "result": "Category deleted"}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

# INGREDEINT
    # GET INGREDIENTS
    @http.route('/bar_app/getAllIngredients', auth='public', type="http")
    def ingredient(self, **kw):
        tdata = http.request.env["bar_app.ingredient_model"].sudo(
        ).search_read([], ["name", "products", "description"])
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