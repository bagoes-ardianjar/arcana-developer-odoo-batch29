# -*- coding: utf-8 -*-

from odoo import models, fields, api


class khaikal_perpustakaan_book(models.Model):
    _name = 'khaikal_perpustakaan.book'
    _description = 'khaikal_perpustakaan.book'

    name = fields.Char()
    total = fields.Float()
    transaction_ids = fields.One2many('khaikal_perpustakaan.transaction', string='Transaction', inverse_name='book_id')
    description = fields.Text()
    available_book = fields.Float('Available Book', compute='count_transaction', store=True)
    
    @api.depends('transaction_ids','total')
    def count_transaction(self):
        for rec in self:
            rec.available_book = rec.total - len(rec.transaction_ids.sudo().search([('state','=','progres')]))
