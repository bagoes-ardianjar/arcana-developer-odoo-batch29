from odoo import models, fields, api

class dawamraja_library(models.Model):
    _name = 'dawamraja_library.book'

    name = fields.Char(string='Name')
    quatity = fields.Integer(string='Quantity')
    # Compute the number of books available
    avalaible = fields.Integer(string='Avalaible', compute='_compute_avalaible')
    transaction_len = fields.Integer(string='Transaction Length', compute='_compute_transaction_len', store=False)


    description = fields.Text(string='Description')
    # One2many relationship with transaction
    transaction_ids = fields.One2many('dawamraja_library.transaction', 'book_id', string='Transactions')

    @api.depends('quatity', 'transaction_ids')
    def _compute_avalaible(self):
        for record in self:
            record.avalaible = record.quatity - len(record.transaction_ids.filtered(lambda r: r.status == 'borrowed'))
    def _compute_transaction_len(self):
        for record in self:
            record.transaction_len = len(record.transaction_ids)

    
        


