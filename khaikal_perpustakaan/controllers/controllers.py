# -*- coding: utf-8 -*-
# from odoo import http


# class KhaikalPerpustakaan(http.Controller):
#     @http.route('/khaikal_perpustakaan/khaikal_perpustakaan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/khaikal_perpustakaan/khaikal_perpustakaan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('khaikal_perpustakaan.listing', {
#             'root': '/khaikal_perpustakaan/khaikal_perpustakaan',
#             'objects': http.request.env['khaikal_perpustakaan.khaikal_perpustakaan'].search([]),
#         })

#     @http.route('/khaikal_perpustakaan/khaikal_perpustakaan/objects/<model("khaikal_perpustakaan.khaikal_perpustakaan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('khaikal_perpustakaan.object', {
#             'object': obj
#         })
