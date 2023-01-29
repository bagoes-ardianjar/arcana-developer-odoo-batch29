# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dudenacademy(models.TransientModel):
    _name = 'wizard.attendees'

    session_id = fields.Many2one('dudenacademy.session', string='Session')
    partner_ids = fields.Many2many('res.partner', string='Attendees')

    def process(self):
        for rec in self:
            rec.session_id.partner_ids |= rec.partner_ids
        return True
