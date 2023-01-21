# -*- coding: utf-8 -*-
# from odoo import http


# class Dawamraja(http.Controller):
#     @http.route('/dawamraja/dawamraja', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dawamraja/dawamraja/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dawamraja.listing', {
#             'root': '/dawamraja/dawamraja',
#             'objects': http.request.env['dawamraja.dawamraja'].search([]),
#         })

#     @http.route('/dawamraja/dawamraja/objects/<model("dawamraja.dawamraja"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dawamraja.object', {
#             'object': obj
#         })
