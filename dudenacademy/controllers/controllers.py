# -*- coding: utf-8 -*-
# from odoo import http


# class Dudenacademy(http.Controller):
#     @http.route('/dudenacademy/dudenacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dudenacademy/dudenacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dudenacademy.listing', {
#             'root': '/dudenacademy/dudenacademy',
#             'objects': http.request.env['dudenacademy.dudenacademy'].search([]),
#         })

#     @http.route('/dudenacademy/dudenacademy/objects/<model("dudenacademy.dudenacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dudenacademy.object', {
#             'object': obj
#         })
