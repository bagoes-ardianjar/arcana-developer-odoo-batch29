from odoo import models, fields, api

class dawamraja_library(models.Model):
    _name = 'dawamraja_library.transaction'

    name = fields.Char(string='Name')
    date_start = fields.Date(string='Date')
    date_finish = fields.Date(string='Date')
    status = fields.Selection([('progress', 'Progress'), ('done', 'Done')], string='Status')
    description = fields.Text(string='Description')

    # Many2one relationship with partner
    book_id = fields.Many2one('dawamraja_library.book', string='Book')
    partner_id = fields.Many2one('res.partner', string='Partner')