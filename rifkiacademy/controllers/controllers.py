# -*- coding: utf-8 -*-
# from odoo import http


# class Rifkiacademy(http.Controller):
#     @http.route('/rifkiacademy/rifkiacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rifkiacademy/rifkiacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rifkiacademy.listing', {
#             'root': '/rifkiacademy/rifkiacademy',
#             'objects': http.request.env['rifkiacademy.rifkiacademy'].search([]),
#         })

#     @http.route('/rifkiacademy/rifkiacademy/objects/<model("rifkiacademy.rifkiacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rifkiacademy.object', {
#             'object': obj
#         })
