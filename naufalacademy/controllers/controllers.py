# -*- coding: utf-8 -*-
# from odoo import http


# class naufalacademy(http.Controller):
#     @http.route('/naufalacademy/naufalacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/naufalacademy/naufalacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('naufalacademy.listing', {
#             'root': '/naufalacademy/naufalacademy',
#             'objects': http.request.env['naufalacademy.naufalacademy'].search([]),
#         })

#     @http.route('/naufalacademy/naufalacademy/objects/<model("naufalacademy.naufalacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('naufalacademy.object', {
#             'object': obj
#         })
