# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'dudenacademy.course'
    _description = 'dudenacademy.course'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
