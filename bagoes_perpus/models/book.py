from odoo import models, fields, api

class bagoes_perpus(models.Model):
    _name = 'bagoes_perpus.book'

    name = fields.Char(string='Name')
    total = fields.Float(string='Total')
    avalaible = fields.Integer(string='Avalaible', compute='_compute_avalaible')
    transaction_len = fields.Integer(string='Transaction Length', compute='_compute_transaction_len', store=False)
    description = fields.Text(string='Description')
    transaction_ids = fields.One2many('bagoes_perpus.transaction', 'book_id', string='Transactions')

    @api.depends('total', 'transaction_ids')
    def _compute_avalaible(self):
        for record in self:
            record.avalaible = record.total - len(record.transaction_ids.filtered(lambda r: r.status == 'progress'))
    def _compute_transaction_len(self):
        for record in self:
            record.transaction_len = len(record.transaction_ids)

    
        


