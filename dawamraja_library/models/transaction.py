from odoo import models, fields, api
from odoo.exceptions import ValidationError

class dawamraja_library(models.Model):
    _name = 'dawamraja_library.transaction'

    name = fields.Char(string='Name', required=True)
    date_start = fields.Date(string='Date', required=True)
    date_finish = fields.Date(string='Date')
    status = fields.Selection([('progress', 'Progress'), ('done', 'Done')], string='Status')
    description = fields.Text(string='Description')

    # Many2one relationship with partner
    book_id = fields.Many2one('dawamraja_library.book', string='Book')
    partner_id = fields.Many2one('res.partner', string='Partner')

    @api.constrains('name')
    def _check_name_unique(self):
        if self.search([('name', '=', self.name), ('id', '!=', self.id)]):
            raise ValidationError("Transaction Name must be unique")