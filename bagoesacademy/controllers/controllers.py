# -*- coding: utf-8 -*-
# from odoo import http


# class Bagoesacademy(http.Controller):
#     @http.route('/bagoesacademy/bagoesacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bagoesacademy/bagoesacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bagoesacademy.listing', {
#             'root': '/bagoesacademy/bagoesacademy',
#             'objects': http.request.env['bagoesacademy.bagoesacademy'].search([]),
#         })

#     @http.route('/bagoesacademy/bagoesacademy/objects/<model("bagoesacademy.bagoesacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bagoesacademy.object', {
#             'object': obj
#         })
