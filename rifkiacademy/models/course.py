# -*- coding: utf-8 -*-

from odoo import models, fields, api


class course(models.Model):
    _name = 'rifkiacademy.course'
    _description = 'rifkiacademy.course'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')

    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
