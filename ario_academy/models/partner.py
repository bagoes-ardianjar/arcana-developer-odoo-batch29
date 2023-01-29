# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    session_ids = fields.Many2many('ario_academy.session', string='Sessions')
    is_instructor = fields.Boolean('Is Instructor')