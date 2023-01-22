from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor =  fields.Boolean(string='Is Instructor')
    session_ids = fields.Many2many('dawamraja.session', string='Session')