# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json, request


class BarApp(http.Controller):
# CATEGORY
    # GET CATEGORYS
    @http.route(['/bar_app/getAllCategorys','/bar_app/getCategory/<int:id>'],auth='public', type='http')
    def getCategory(self,id=None, **kw):
        if id:
            domain = [("id", "=", id)]
        else:
            domain=[]
        taskdata = http.request.env["bar_app.category_model"].sudo().search_read(domain,["name","product","description"])
        data={ "status":200,"data":taskdata }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

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
    def deleteCategory(self, **kw):
        response = request.jsonrequest
        domain = [("id", "=", response["id"])]
        try:
            x = http.request.env["bar_app.category_model"].sudo().search(domain).unlink()
            data = {"status": 200, "result": "Category deleted"}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

# INGREDEINT
    # GET INGREDIENTS
    @http.route(['/bar_app/getAllIngredients','/bar_app/getIngredient/<int:id>'], auth='public', type="http")
    def getIngredient(self, id=None, **kw):
        if id:
            domain = [("id", "=", id)]
        else:
            domain = []
        taskdata = http.request.env["bar_app.ingredient_model"].sudo().search_read(domain, ["name", "products", "description"])
        data = {"status": 200,"data": taskdata}
        return http.Response(json.dumps(data).encode("utf8"), mimetype="application/json")

	# ADD INGREDIENT
    @http.route('/bar_app/addIngredient', auth='public', type="json", method="POST")
    def addIngredient(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.ingredient_model"].sudo().create(
                response)
            data = {"status": 201, "id": result.id}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
        return data

	# UPDATE INGREDIENT
    @http.route('/bar_app/updateIngredient', auth="public", type="json", method="PUT")
    def updateIngredient(self, **kw):
        response = request.jsonrequest
        domain = [("id", "=", response["id"])]
        try:
            x = http.request.env["bar_app.ingredient_model"].sudo().search(
                domain)
            updated = x.sudo().write(response)
            if (updated):
                data = {"status": 200, "result": x.id}
            else:
                data = {"status": 400, "result": "Ingredient not modified"}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

	# DELETE INGREDIENT
    @http.route('/bar_app/deleteIngredient', auth="public", type="json", method="DELETE")
    def deleteIngredient(self, **kw):
        response = request.jsonrequest
        domain = [("id", "=", response["id"])]
        try:
            x = http.request.env["bar_app.ingredient_model"].sudo().search(
                domain).unlink()
            data = {"status": 200, "result": "Ingredient deleted"}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

# PRODUCT
    # GET PRODUCTS
    @http.route(['/bar_app/getAllProducts','/bar_app/getProduct/<int:idprod>'],auth='public', type='http')
    def getProduct(self,idprod=None, **kw):
        if id:
            domain = [("id","=",idprod)]
        else:
            domain=[]
        taskdata = http.request.env["bar_app.product_model"].sudo().search_read(domain,["name","currency_id","price","category","ingredients","description"])
        data={ "status":200,"data":taskdata }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    # ADD PRODUCT
    @http.route('/bar_app/addProduct', auth='public', type="json", method="POST")
    def addProduct(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar_app.product_model"].sudo().create(response)
            data = {"status": 201, "id": result.id}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
        return data

    # UPDATE PRODUCT
    @http.route('/bar_app/updateProduct', auth="public", type="json", method="PUT")
    def updateProduct(self, **kw):
        response = request.jsonrequest
        domain = [("id", "=", response["id"])]
        try:
            x = http.request.env["bar_app.product_model"].sudo().search(domain)
            updated = x.sudo().write(response)
            if (updated):
                data = {"status": 200, "result": x.id}
            else:
                data = {"status": 400, "result": "Product not modified"}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

    # DELETE PRODUCT
    @http.route('/bar_app/deleteProduct', auth="public", type="json", method="DELETE")
    def deleteProduct(self, **kw):
        response = request.jsonrequest
        domain = [("id", "=", response["id"])]
        try:
            x = http.request.env["bar_app.product_model"].sudo().search(domain).unlink()
            data = {"status": 200, "result": "Product deleted"}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data