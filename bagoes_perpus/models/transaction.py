from odoo import models, fields, api

class bagoes_perpus(models.Model):
    _name = 'bagoes_perpus.transaction'

    name = fields.Char(string='Name')
    date_start = fields.Date(string='Date')
    date_finish = fields.Date(string='Date')
    status = fields.Selection([('progress', 'Progress'), ('done', 'Done')], string='Status')
    description = fields.Text(string='Description')
    book_id = fields.Many2one('bagoes_perpus.book', string='Book')
    partner_id = fields.Many2one('res.partner', string='Partner')