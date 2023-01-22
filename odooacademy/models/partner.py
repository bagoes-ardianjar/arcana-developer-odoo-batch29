# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    session_ids = fields.Many2many('odooacademy.session', string='Sessions')
    is_instructor = fields.Boolean('Is Instructor')


    

