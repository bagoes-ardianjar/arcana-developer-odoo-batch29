# -*- coding: utf-8 -*-

from odoo import models, fields, api


class course(models.Model):
    _name = 'rifkiacademy.course'
    _description = 'rifkiacademy.course'

    name = fields.Char('Title', required=True)
    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('rifkiacademy.session', 'course_id', string='Sessions')
    description = fields.Text('Description')

    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
