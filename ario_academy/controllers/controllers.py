# -*- coding: utf-8 -*-
# from odoo import http


# class ArioAcademy(http.Controller):
#     @http.route('/ario_academy/ario_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ario_academy/ario_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ario_academy.listing', {
#             'root': '/ario_academy/ario_academy',
#             'objects': http.request.env['ario_academy.ario_academy'].search([]),
#         })

#     @http.route('/ario_academy/ario_academy/objects/<model("ario_academy.ario_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ario_academy.object', {
#             'object': obj
#         })
